from flask import render_template, session, redirect, url_for, request, jsonify
import re
import io
import zipfile
import base64
import yaml
import os
from datetime import datetime
from config.pages_config import get_navigation_info, get_page_config
from helpers.ai_helpers import generate_ai_response, generate_gemini_response

from helpers.session_yaml import (
    get_session_filename,
    load_yaml_data,
    check_previous_steps_completed,
)

OUTPUT_DIR = 'output'
DEBUG_DIR = 'debug'
for p in (OUTPUT_DIR, DEBUG_DIR):
    if not os.path.exists(p):
        os.makedirs(p)

 

def generate_macrodesign_recap(yaml_data):
    """
    Generate the complete macrodesign recap from all YAML data
    """
    try:
        # Extract data from each step
        public_cible = yaml_data.get('etape_1_public_cible', {})
        contraintes = yaml_data.get('etape_2_contraintes', {})
        competences = yaml_data.get('etape_4_competences', {})
        referentiels = yaml_data.get('etape_5_referentiels', {})
        contenus = yaml_data.get('etape_5_contenu', {})
        
        # Build macrodesign_generalites
        # Normalize public cible fields based on current YAML structure
        type_de_public = public_cible.get('type_de_public', []) or []
        if isinstance(type_de_public, list):
            type_de_public_str = ", ".join([str(x) for x in type_de_public])
        else:
            type_de_public_str = str(type_de_public)

        niveaux_scolaires = public_cible.get('niveaux_scolaires', []) or []
        if isinstance(niveaux_scolaires, list):
            niveaux_scolaires_str = ", ".join([str(x) for x in niveaux_scolaires])
        else:
            niveaux_scolaires_str = str(niveaux_scolaires)

        niveau_expertise = public_cible.get('niveau_expertise', []) or []
        if isinstance(niveau_expertise, list):
            niveau_expertise_str = ", ".join([str(x) for x in niveau_expertise])
        else:
            niveau_expertise_str = str(niveau_expertise)

        profil_public = public_cible.get('type_de_formation', '')
        precisions_public = public_cible.get('type_de_formation_precisions', '')
        profil_combined = (profil_public + (f" — {precisions_public}" if precisions_public else '')).strip()

        besoins_specifiques_value = public_cible.get('besoins_specifiques', '')

        # Build filtered contraintes only from keys that actually exist in YAML
        contraintes_keys = [
            'type_parcours', 'hybridation', 'temps_total', 'autonomie', 'animation',
            'calendrier', 'horaires', 'nombre_participants', 'exigences_institutionnelles', 'restrictions_techniques'
        ]
        contraintes_filtrees = {}
        for key in contraintes_keys:
            value = contraintes.get(key)
            if value is not None and value != '':
                contraintes_filtrees[key] = value

        macrodesign_generalites = {
            'titre_formation': public_cible.get('titre_formation', '[ ]'),
            'public_cible': {
                'type': type_de_public_str or '[ ]',
                'profil': profil_combined or '[ ]',
                'niveau_expertise': niveau_expertise_str or '[ ]',
                'niveaux_scolaires': niveaux_scolaires_str or '[ ]',
                'besoins_specifiques': str(besoins_specifiques_value) if besoins_specifiques_value else ''
            },
            'contraintes_formation': contraintes_filtrees,
            'scenario_hybride': {
                'reference': 'CMO',
                'structure': [
                    'Accueil',
                    'Apprentissage 1',
                    'Apprentissage 2',
                    'Apprentissage 3',
                    'Apprentissage 4',
                    'Classe virtuelle',
                    'Forum général',
                    'Évaluation finale'
                ]
            },
            'competences_visees': [],
            'referentiels_autoevaluation_complet': []
        }
        
        # Extract competences
        if competences:
            # Get detailed competences
            detailed_competences = {}
            i = 1
            while f'competence_{i}' in competences:
                comp_data = competences[f'competence_{i}']
                code = f'C{i}'
                detailed_competences[code] = {
                    'id': code,
                    'formulation': comp_data.get('formulation', f'[Compétence {i}]')
                }
                i += 1
            
            # Get ordered competences
            evaluation_data = competences.get('evaluation_competences', {})
            if evaluation_data and 'ordre_competences' in evaluation_data:
                for ordered_comp in evaluation_data['ordre_competences']:
                    code = ordered_comp.get('code', '')
                    if code in detailed_competences:
                        macrodesign_generalites['competences_visees'].append({
                            'id': code,
                            'formulation': detailed_competences[code]['formulation']
                        })
                    else:
                        macrodesign_generalites['competences_visees'].append({
                            'id': code,
                            'formulation': ordered_comp.get('formulation', f'[Compétence {code}]')
                        })
            
            # Extract referentiels for each available section key
            for section_key, section_data in referentiels.items():
                if not str(section_key).startswith('section_'):
                    continue
                # Get section number from data or key
                section_num = section_data.get('section') or section_key.replace('section_', '')

                competence_text = section_data.get('competence', '[ ]')
                # Try to find matching competence id by formulation
                competence_id = next((c['id'] for c in macrodesign_generalites['competences_visees'] if c.get('formulation') == competence_text), '')
                if not competence_id:
                    # fallback: try to guess by index order
                    competence_id = f"C{len(macrodesign_generalites['referentiels_autoevaluation_complet']) + 1}"

                referentiel_entry = {
                    'section': section_num,
                    'competence_id': competence_id,
                    'competence': competence_text,
                    'niveaux': []
                }

                niveaux_list = section_data.get('niveaux', []) or []
                for level in niveaux_list:
                    referentiel_entry['niveaux'].append({
                        'niveau': level.get('degre', ''),
                        'label': level.get('libelle', '[ ]'),
                        'indicateurs': [
                            level.get('observable_qualitatif', '[ ]'),
                            level.get('observable_quantitatif', '[ ]')
                        ],
                        'badge': level.get('badge', '')
                    })

                referentiel_entry['badge_criteres'] = ''
                referentiel_entry['modalites_preuve'] = ''

                macrodesign_generalites['referentiels_autoevaluation_complet'].append(referentiel_entry)
        
        # Build contenus_par_section
        contenus_par_section = []
        
        if contenus and 'contenus_par_section' in contenus:
            # Use the AI-generated contenus
            for section_data in contenus['contenus_par_section']:
                contenus_par_section.append({
                    'section': section_data.get('section', '') or '',
                    'type_section': section_data.get('type_de_section', ''),
                    'competence_visee': section_data.get('competences_visees', ''),
                    'ressource': section_data.get('ressource', ''),
                    'intention_ressource': section_data.get('intention_ressource', ''),
                    'activite_1': section_data.get('activite_1', ''),
                    'intention_activite_1': section_data.get('intention_activite_1', ''),
                    'activite_2': section_data.get('activite_2', ''),
                    'intention_activite_2': section_data.get('intention_activite_2', ''),
                    'justification': section_data.get('justification_activite_s', '') or section_data.get('justification_ressource', '')
                })
        else:
            # Create default structure
            default_sections = [
                {'section': 1, 'type': 'Accueil'},
                {'section': 2, 'type': 'Apprentissage'},
                {'section': 3, 'type': 'Apprentissage'},
                {'section': 4, 'type': 'Apprentissage'},
                {'section': 5, 'type': 'Apprentissage'},
                {'section': 6, 'type': 'Classe virtuelle (BBB)'},
                {'section': 7, 'type': 'Forum général'},
                {'section': 8, 'type': 'Évaluation'}
            ]
            
            for section_info in default_sections:
                contenus_par_section.append({
                    'section': section_info['section'],
                    'type_section': section_info['type'],
                    'competence_visee': '',
                    'ressource': '',
                    'intention_ressource': '',
                    'activite_1': '',
                    'intention_activite_1': '',
                    'activite_2': '',
                    'intention_activite_2': '',
                    'justification': ''
                })
        
        return {
            'macrodesign_generalites': macrodesign_generalites,
            'contenus_par_section': contenus_par_section
        }
        
    except Exception as e:
        print(f"Error generating macrodesign recap: {e}")
        return None

def generate_export_format(recap_data, format_type):
    """
    Generate export in the specified format
    """
    try:
        if format_type == 'markdown':
            return generate_markdown_export(recap_data)
        elif format_type == 'csv':
            return generate_csv_export(recap_data)
        elif format_type == 'csv_referentiels':
            return generate_csv_referentiels(recap_data)
        elif format_type == 'csv_referentiels_zip':
            return generate_csv_referentiels_zip_base64(recap_data)
        elif format_type in ['csv_activites_simple', 'csv_activites_simplifie', 'csv_activites_simplified']:
            return generate_csv_activites(recap_data, simplified=True)
        elif format_type in ['csv_activites_complet', 'csv_activites_full']:
            return generate_csv_activites(recap_data, simplified=False)
        elif format_type in ['markdown_recap', 'md_recap']:
            return generate_markdown_recap(recap_data)
        else:
            return None
    except Exception as e:
        print(f"Error generating export: {e}")
        return None

def generate_markdown_export(recap_data):
    """
    Generate Markdown export with two tables
    """
    generalites = recap_data['macrodesign_generalites']
    contenus = recap_data['contenus_par_section']
    
    # Table 1: Generalités
    markdown = "## 📋 Généralités de la Formation\n\n"
    markdown += "| titre_formation | public_type | public_profil | public_niveau | besoins_spec1 | besoins_spec2 | type_parcours | hybridation | temps_total | autonomie | animation | calendrier | horaires | nb_participants |\n"
    markdown += "|-----------------|-------------|---------------|---------------|---------------|---------------|---------------|-------------|-------------|-----------|-----------|------------|----------|-----------------|\n"
    
    markdown += f"| {generalites.get('titre_formation', '[ ]')} | "
    markdown += f"{generalites.get('public_cible', {}).get('type', '[ ]')} | "
    markdown += f"{generalites.get('public_cible', {}).get('profil', '[ ]')} | "
    markdown += f"{generalites.get('public_cible', {}).get('niveau_expertise', '[ ]')} | "
    markdown += f"{generalites.get('public_cible', {}).get('besoins_specifiques', ['[ ]', '[ ]'])[0]} | "
    markdown += f"{generalites.get('public_cible', {}).get('besoins_specifiques', ['[ ]', '[ ]'])[1]} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('type_parcours', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('hybridation', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('temps_total', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('autonomie', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('animation', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('calendrier', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('horaires', '[ ]')} | "
    markdown += f"{generalites.get('contraintes_formation', {}).get('nombre_participants', '[ ]')} |\n\n"
    
    # Table 2: Sections
    markdown += "## 📚 Contenus par Section\n\n"
    markdown += "| section | titre | competence | intentions | ressource | activite_1 | activite_2 | discussion | badge | modalite |\n"
    markdown += "|---------|-------|------------|------------|-----------|------------|------------|------------|-------|----------|\n"
    
    for section in contenus:
        section_num = section.get('section', '')
        titre = section.get('type_section', '')
        competence = section.get('competence_visee', '')
        intentions = section.get('intention_ressource', '')
        ressource = section.get('ressource', '')
        activite_1 = section.get('activite_1', '')
        activite_2 = section.get('activite_2', '')
        discussion = section.get('justification', '')
        badge = 'Réussite si atteinte du degré 3' if section_num in ['2', '3', '4', '5'] else ''
        modalite = 'Asynchrone' if section_num in ['1', '2', '3', '4', '5', '7', '8'] else 'Synchrone'
        
        markdown += f"| {section_num} | {titre} | {competence} | {intentions} | {ressource} | {activite_1} | {activite_2} | {discussion} | {badge} | {modalite} |\n"
    
    return markdown

def generate_csv_export(recap_data):
    """
    Generate CSV export with two tables
    """
    generalites = recap_data['macrodesign_generalites']
    contenus = recap_data['contenus_par_section']
    
    # Table 1: Generalités
    csv = "titre_formation;public_type;public_profil;public_niveau;besoins_spec1;besoins_spec2;type_parcours;hybridation;temps_total;autonomie;animation;calendrier;horaires;nb_participants\n"
    
    csv += f"{generalites.get('titre_formation', '[ ]')};"
    csv += f"{generalites.get('public_cible', {}).get('type', '[ ]')};"
    csv += f"{generalites.get('public_cible', {}).get('profil', '[ ]')};"
    csv += f"{generalites.get('public_cible', {}).get('niveau_expertise', '[ ]')};"
    csv += f"{generalites.get('public_cible', {}).get('besoins_specifiques', ['[ ]', '[ ]'])[0]};"
    csv += f"{generalites.get('public_cible', {}).get('besoins_specifiques', ['[ ]', '[ ]'])[1]};"
    csv += f"{generalites.get('contraintes_formation', {}).get('type_parcours', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('hybridation', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('temps_total', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('autonomie', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('animation', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('calendrier', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('horaires', '[ ]')};"
    csv += f"{generalites.get('contraintes_formation', {}).get('nombre_participants', '[ ]')}\n\n"
    
    # Table 2: Sections
    csv += "section;titre;competence;intentions;ressource;activite_1;activite_2;discussion;badge;modalite\n"
    
    for section in contenus:
        section_num = section.get('section', '')
        titre = section.get('type_section', '')
        competence = section.get('competence_visee', '')
        intentions = section.get('intention_ressource', '')
        ressource = section.get('ressource', '')
        activite_1 = section.get('activite_1', '')
        activite_2 = section.get('activite_2', '')
        discussion = section.get('justification', '')
        badge = 'Réussite si atteinte du degré 3' if section_num in ['2', '3', '4', '5'] else ''
        modalite = 'Asynchrone' if section_num in ['1', '2', '3', '4', '5', '7', '8'] else 'Synchrone'
        
        csv += f"{section_num};{titre};{competence};{intentions};{ressource};{activite_1};{activite_2};{discussion};{badge};{modalite}\n"
    
    return csv

def _sanitize_csv_value(value):
    try:
        text = str(value) if value is not None else ''
        return text.replace('\n', ' ').replace(';', ',').strip()
    except Exception:
        return ''

def generate_csv_referentiels(recap_data):
    """
    Generate CSV for referentiels (autoevaluation complet)
    """
    generalites = recap_data.get('macrodesign_generalites', {})
    referentiels = generalites.get('referentiels_autoevaluation_complet', [])

    header = "section;competence_id;competence;niveau;label;indicateur_qualitatif;indicateur_quantitatif;badge\n"
    rows = []
    for ref in referentiels:
        section = _sanitize_csv_value(ref.get('section', ''))
        competence_id = _sanitize_csv_value(ref.get('competence_id', ''))
        competence = _sanitize_csv_value(ref.get('competence', ''))
        niveaux = ref.get('niveaux', []) or []
        if niveaux:
            for level in niveaux:
                niveau_num = _sanitize_csv_value(level.get('niveau', ''))
                label = _sanitize_csv_value(level.get('label', ''))
                indicateurs = level.get('indicateurs', []) or []
                indic1 = _sanitize_csv_value(indicateurs[0] if len(indicateurs) > 0 else '')
                indic2 = _sanitize_csv_value(indicateurs[1] if len(indicateurs) > 1 else '')
                badge = _sanitize_csv_value(level.get('badge', ''))
                rows.append(f"{section};{competence_id};{competence};{niveau_num};{label};{indic1};{indic2};{badge}")
        else:
            rows.append(f"{section};{competence_id};{competence};;;;;")

    return header + "\n".join(rows)

def generate_csv_referentiels_zip_base64(recap_data):
    """
    Generate one CSV per competence/referential and return a base64-encoded ZIP content.
    This is useful when the consumer wants separate files grouped in a single download.
    """
    generalites = recap_data.get('macrodesign_generalites', {})
    referentiels = generalites.get('referentiels_autoevaluation_complet', [])

    header = "section;competence_id;competence;niveau;label;indicateur_qualitatif;indicateur_quantitatif;badge\n"
    memfile = io.BytesIO()
    with zipfile.ZipFile(memfile, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for ref in referentiels:
            section = _sanitize_csv_value(ref.get('section', ''))
            competence_id = _sanitize_csv_value(ref.get('competence_id', '')) or 'C?'
            competence = _sanitize_csv_value(ref.get('competence', ''))
            rows = []
            niveaux = ref.get('niveaux', []) or []
            if niveaux:
                for level in niveaux:
                    niveau_num = _sanitize_csv_value(level.get('niveau', ''))
                    label = _sanitize_csv_value(level.get('label', ''))
                    indicateurs = level.get('indicateurs', []) or []
                    indic1 = _sanitize_csv_value(indicateurs[0] if len(indicateurs) > 0 else '')
                    indic2 = _sanitize_csv_value(indicateurs[1] if len(indicateurs) > 1 else '')
                    badge = _sanitize_csv_value(level.get('badge', ''))
                    rows.append(f"{section};{competence_id};{competence};{niveau_num};{label};{indic1};{indic2};{badge}")
            else:
                rows.append(f"{section};{competence_id};{competence};;;;;")

            csv_text = header + "\n".join(rows)
            filename = f"referentiel_{competence_id}.csv"
            # Write with UTF-8 BOM for Excel compatibility
            zf.writestr(filename, ("\ufeff" + csv_text).encode('utf-8'))

    memfile.seek(0)
    return base64.b64encode(memfile.read()).decode('ascii')

def generate_csv_activites(recap_data, simplified=True):
    """
    Generate CSV for activities (contenus par section)
    simplified=True => reduced set of columns
    simplified=False => full details
    """
    contenus = recap_data.get('contenus_par_section', [])

    def compute_modalite(section_num):
        asynchrone_sections = ['1', '2', '3', '4', '5', '7', '8', '']
        return 'Asynchrone' if str(section_num) in asynchrone_sections else 'Synchrone'

    lines = []
    if simplified:
        header = "section;titre;competence;activite_1;activite_2;modalite\n"
        for s in contenus:
            section_num = _sanitize_csv_value(s.get('section', ''))
            titre = _sanitize_csv_value(s.get('type_section', ''))
            competence = _sanitize_csv_value(s.get('competence_visee', ''))
            activite_1 = _sanitize_csv_value(s.get('activite_1', ''))
            activite_2 = _sanitize_csv_value(s.get('activite_2', ''))
            modalite = _sanitize_csv_value(compute_modalite(section_num))
            lines.append(f"{section_num};{titre};{competence};{activite_1};{activite_2};{modalite}")
        return header + "\n".join(lines)
    else:
        header = "Section;Type de section;Compétence (id + formulation);Ressource (type);URL ressource;Intention ressource;Activité 1 (type);URL activité 1;Intention activité 1;Activité 2 (type);URL activité 2;Intention activité 2;Justification pédagogique;Modalité;Durée (min);Évaluation\n"

        def get_competence_str(n: int) -> str:
            generalites = recap_data.get('macrodesign_generalites', {})
            comps = generalites.get('competences_visees', []) or []
            for c in comps:
                if str(c.get('id', '')).strip().upper() == f"C{n}":
                    return f"C{n} — {c.get('formulation','')}"
            return ''

        accueil_duration = 10
        learning_durations = [35, 40, 35, 45]
        tail_durations = [45, 10, 10]

        # Helper to fetch AI section content by index: 0->S2, 1->S3, 2->S4, 3->S5
        def get_ai_section(idx: int):
            try:
                return contenus[idx]
            except Exception:
                return {}

        # S1 fixed
        lines.append(";".join([
            "S1",
            _sanitize_csv_value("Accueil"),
            _sanitize_csv_value(""),
            _sanitize_csv_value("Page"),
            "URL_A_COMPLETER",
            _sanitize_csv_value("Acquisition"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("Présentation générale, cadrage et attentes"),
            _sanitize_csv_value("asynchrone"),
            str(accueil_duration),
            _sanitize_csv_value("")
        ]))

        # S2..S(1+n_comp) map to AI content when present
        defaults = {
            2: {"type": "Apprentissage"},
            3: {"type": "Apprentissage"},
            4: {"type": "Apprentissage"},
            5: {"type": "Apprentissage"}
        }
        generalites = recap_data.get('macrodesign_generalites', {})
        comps = generalites.get('competences_visees', []) or []
        n_comp = min(4, max(len(comps), len(contenus)))
        for offset in range(2, 2 + n_comp):
            ai = get_ai_section(offset - 2)
            comp_str = get_competence_str(offset - 1)
            section_label = f"S{offset}"
            type_section = ai.get('type_section') or defaults[offset]["type"]
            ressource = ai.get('ressource', '')
            intention_ressource = ai.get('intention_ressource', '')
            act1 = ai.get('activite_1', '')
            act1_int = ai.get('intention_activite_1', '')
            act2 = ai.get('activite_2', '')
            act2_int = ai.get('intention_activite_2', '')
            justification = ai.get('justification', '')
            evaluation = 'auto_evaluation_4_degres' if comp_str else ''
            learn_idx = offset - 2
            learn_duration = learning_durations[learn_idx] if learn_idx < len(learning_durations) else learning_durations[-1]
            lines.append(";".join([
                section_label,
                _sanitize_csv_value(type_section),
                _sanitize_csv_value(comp_str),
                _sanitize_csv_value(ressource),
                "URL_A_COMPLETER",
                _sanitize_csv_value(intention_ressource),
                _sanitize_csv_value(act1),
                "URL_A_COMPLETER",
                _sanitize_csv_value(act1_int),
                _sanitize_csv_value(act2),
                "URL_A_COMPLETER",
                _sanitize_csv_value(act2_int),
                _sanitize_csv_value(justification),
                _sanitize_csv_value("asynchrone"),
                str(learn_duration),
                _sanitize_csv_value(evaluation)
            ]))

        # Tail sections begin after the last learning section
        tail_start = 2 + n_comp
        # Classe virtuelle (BBB)
        lines.append(";".join([
            f"S{tail_start}",
            _sanitize_csv_value("Classe virtuelle (BBB)"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("BigBlueButtonBN"),
            "URL_A_COMPLETER",
            _sanitize_csv_value("Discussion"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("synchrone"),
            str(tail_durations[0]),
            _sanitize_csv_value("")
        ]))

        # Forum général
        lines.append(";".join([
            f"S{tail_start+1}",
            _sanitize_csv_value("Forum général"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("Forum"),
            "URL_A_COMPLETER",
            _sanitize_csv_value("Discussion / Collaboration"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("asynchrone"),
            str(tail_durations[1]),
            _sanitize_csv_value("")
        ]))

        # Évaluation de satisfaction
        lines.append(";".join([
            f"S{tail_start+2}",
            _sanitize_csv_value("Évaluation de satisfaction"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("Sondage Magistère"),
            "URL_A_COMPLETER",
            _sanitize_csv_value("Enquête"),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value(""),
            _sanitize_csv_value("asynchrone"),
            str(tail_durations[2]),
            _sanitize_csv_value("evaluation_satisfaction")
        ]))

        return header + "\n".join(lines)

def generate_markdown_recap(recap_data):
    try:
        yaml_content = yaml.dump(recap_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        prompt = f"""
                Tu es un expert en ingénierie pédagogique et en communication.
                Je vais te fournir un fichier YAML décrivant une formation.

                Ta mission est de générer un résumé clair, chaleureux et engageant en HTML, directement intégrable dans une page existante (⚠️ pas de <html>, <head> ni <body>).

                Style et ton :

                Rédige dans un style clair, accessible et convivial.

                Ajoute un paragraphe d’introduction générale décrivant l’esprit et l’objectif de la formation.

                Avant chaque section, ajoute une phrase courte et amicale qui introduit la section.

                Utilise des émoticônes pour rendre le rendu vivant et chaleureux (🎯, 👩‍🏫, 📘, 🛠️, ✅…).

                Le HTML doit rester propre, sémantique et facile à styliser avec du CSS.

                Contenu et structure :

                <h1> Titre de la formation + paragraphe d’introduction 🌟

                <h2> Public cible 👥

                Phrase introductive : « Qui est concerné par cette formation ? »

                Présente les informations dans un tableau.

                <h2> Contraintes de formation 📋

                Phrase introductive : « Voici les aspects pratiques à connaître : »

                Utilise un tableau.

                <h2> Scénario hybride 🧩

                Phrase introductive : « Comment la formation sera structurée : »

                Affiche sous forme de liste ou tableau.

                <h2> Compétences visées 🎯

                Phrase introductive : « À l’issue de la formation, vous serez capable de… »

                Liste <ul> avec identifiants en gras.               

                Sortie attendue :

                Génère directement le bloc HTML complet à partir du YAML, prêt à copier-coller dans une page web existante. 

            YAML :
            {yaml_content}"""
        
        ai_output = generate_ai_response(prompt) or ""
        # Save raw prompt and response for debugging
        try:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open(os.path.join(DEBUG_DIR, f"recap_prompt_{ts}.txt"), 'w', encoding='utf-8') as f_pr:
                f_pr.write(prompt)
            with open(os.path.join(DEBUG_DIR, f"recap_response_{ts}.html"), 'w', encoding='utf-8') as f_rs:
                f_rs.write(ai_output)
        except Exception as e_dbg:
            print(f"Debug save failed: {e_dbg}")
        # Strip surrounding Markdown code fences like ```html ... ``` or ``` ... ```
        cleaned = ai_output.strip()
        if '```' in cleaned:
            fence_match = re.match(r"^\s*```(?:[a-zA-Z0-9_-]+)?\s*\n([\s\S]*?)\n\s*```\s*$", cleaned)
            if fence_match:
                cleaned = fence_match.group(1)
            else:
                # Fallback: remove leading fence line and trailing fence if present
                if cleaned.startswith('```'):
                    first_nl = cleaned.find('\n')
                    if first_nl != -1:
                        cleaned = cleaned[first_nl+1:]
                if cleaned.endswith('```'):
                    cleaned = cleaned[:-3]
                cleaned = cleaned.strip()
        # Save cleaned output too
        try:
            with open(os.path.join(DEBUG_DIR, f"recap_cleaned_{ts}.html"), 'w', encoding='utf-8') as f_cl:
                f_cl.write(cleaned)
        except Exception as e_dbg2:
            print(f"Debug save (cleaned) failed: {e_dbg2}")
        return cleaned
    except Exception as e:
        print(f"Error generating markdown recap via AI: {e}")
        return ""

def register_recap_routes(app):
    """Register recap routes with the Flask app"""
    
    @app.route('/recap', methods=['GET', 'POST'])
    def recap():
        if request.method == 'POST':
            # Handle form submission if needed
            data = request.form.to_dict()
            return redirect('/')
        
        # Check if all previous steps are completed
        completed, message = check_previous_steps_completed([
            'etape_1_public_cible', 
            'etape_2_contraintes', 
            'etape_4_competences', 
            'etape_5_referentiels', 
            'etape_5_contenu'
        ])
        if not completed:
            return render_template('error.html', message=f"Veuillez d'abord compléter toutes les étapes précédentes. {message}")
        
        nav_info = get_navigation_info('recap')
        page_config = get_page_config('recap')
        
        # Load and generate recap data
        yaml_data = load_yaml_data()
        print(f"YAML data loaded: {yaml_data is not None}")
        
        recap_data = None
        if yaml_data:
            recap_data = generate_macrodesign_recap(yaml_data)
            print(f"Recap data generated: {recap_data is not None}")
            if recap_data:
                print(f"Generalites: {len(recap_data.get('macrodesign_generalites', {}).get('competences_visees', []))} competences")
                print(f"Contenus: {len(recap_data.get('contenus_par_section', []))} sections")
        
        return render_template('recap.html', 
                             nav_info=nav_info,
                             header_gradient=page_config.get('header_gradient', 'var(--gradient-gray)'),
                             recap_data=recap_data,
                             header_title='📋 Récapitulatif Macrodesign',
                             header_description='Synthèse complète de votre formation prête pour le microdesign')

    @app.route('/generate_export', methods=['POST'])
    def generate_export():
        try:
            data = request.get_json()
            format_type = data.get('format', 'markdown')
            
            # Load YAML data and generate recap
            yaml_data = load_yaml_data()
            if not yaml_data:
                return jsonify({
                    'success': False,
                    'error': 'Aucune donnée trouvée'
                })
            
            recap_data = generate_macrodesign_recap(yaml_data)
            if not recap_data:
                return jsonify({
                    'success': False,
                    'error': 'Erreur lors de la génération du récapitulatif'
                })
            
            # Generate export
            export_content = generate_export_format(recap_data, format_type)
            if not export_content:
                return jsonify({
                    'success': False,
                    'error': 'Erreur lors de la génération de l\'export'
                })
            
            return jsonify({
                'success': True,
                'export_content': export_content,
                'format': format_type
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/download_yaml', methods=['GET'])
    def download_yaml():
        try:
            yaml_data = load_yaml_data()
            if not yaml_data:
                return jsonify({
                    'success': False,
                    'error': 'Aucune donnée trouvée'
                })
            
            # Generate recap data
            recap_data = generate_macrodesign_recap(yaml_data)
            if not recap_data:
                return jsonify({
                    'success': False,
                    'error': 'Erreur lors de la génération du récapitulatif'
                })
            
            # Convert to YAML string
            yaml_content = yaml.dump(recap_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            return jsonify({
                'success': True,
                'yaml_content': yaml_content
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })
