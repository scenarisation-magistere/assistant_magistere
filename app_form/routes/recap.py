from flask import render_template, session, redirect, url_for, request, jsonify
import yaml
import os
from datetime import datetime
from config.pages_config import get_navigation_info, get_page_config
from ai_helpers import generate_ai_response, generate_gemini_response

# Create output directory if it doesn't exist
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_session_filename():
    """Generate a unique filename for this session"""
    if 'session_id' not in session:
        session['session_id'] = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"formation_{session['session_id']}.yaml"

def load_yaml_data():
    """Load data from YAML file"""
    if 'session_id' not in session:
        return None
    
    filename = get_session_filename()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if not os.path.exists(filepath):
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except:
        return None

def check_previous_steps_completed(required_steps):
    """Check if all required previous steps are completed"""
    if 'session_id' not in session:
        return False, "Aucune session active"
    
    filename = get_session_filename()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if not os.path.exists(filepath):
        return False, "Aucun fichier de données trouvé"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f) or {}
    except:
        return False, "Erreur lors du chargement des données"
    
    for step in required_steps:
        if step not in yaml_data:
            return False, f"Étape {step} non complétée"
    
    return True, "OK"

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
        macrodesign_generalites = {
            'titre_formation': public_cible.get('titre_formation', '[ ]'),
            'public_cible': {
                'type': public_cible.get('type_public', '[ ]'),
                'profil': public_cible.get('profil_public', '[ ]'),
                'niveau_expertise': public_cible.get('niveau_expertise', '[ ]'),
                'besoins_specifiques': [
                    public_cible.get('besoin_specifique_1', '[ ]'),
                    public_cible.get('besoin_specifique_2', '[ ]')
                ]
            },
            'contraintes_formation': {
                'type_parcours': contraintes.get('type_parcours', '[ ]'),
                'hybridation': contraintes.get('hybridation', '[ ]'),
                'temps_total': contraintes.get('temps_total', '[ ]'),
                'autonomie': contraintes.get('autonomie', '[ ]'),
                'animation': contraintes.get('animation', '[ ]'),
                'calendrier': contraintes.get('calendrier', '[ ]'),
                'horaires': contraintes.get('horaires', '[ ]'),
                'nombre_participants': contraintes.get('nombre_participants', '[ ]')
            },
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
            
            # Extract referentiels for each section
            sections = [2, 3, 4, 5]
            for section_num in sections:
                section_key = f'section_{section_num}'
                if section_key in referentiels:
                    section_data = referentiels[section_key]
                    competence_id = f'C{section_num - 1}' if section_num > 1 else 'C1'
                    
                    referentiel_entry = {
                        'section': section_num,
                        'competence_id': competence_id,
                        'competence': next((comp['formulation'] for comp in macrodesign_generalites['competences_visees'] if comp['id'] == competence_id), '[ ]'),
                        'niveaux': []
                    }
                    
                    # Extract levels
                    for level_num in range(1, 5):
                        level_key = f'niveau_{level_num}'
                        if level_key in section_data:
                            level_data = section_data[level_key]
                            referentiel_entry['niveaux'].append({
                                'niveau': level_num,
                                'label': level_data.get('label', '[ ]'),
                                'indicateurs': [
                                    level_data.get('indicateur_1', '[ ]'),
                                    level_data.get('indicateur_2', '[ ]')
                                ]
                            })
                    
                    referentiel_entry['badge_criteres'] = section_data.get('badge_criteres', '[ ]')
                    referentiel_entry['modalites_preuve'] = section_data.get('modalites_preuve', '[ ]')
                    
                    macrodesign_generalites['referentiels_autoevaluation_complet'].append(referentiel_entry)
        
        # Build contenus_par_section
        contenus_par_section = []
        
        if contenus and 'contenus_par_section' in contenus:
            # Use the AI-generated contenus
            for section_data in contenus['contenus_par_section']:
                contenus_par_section.append({
                    'section': section_data.get('section', ''),
                    'type_section': section_data.get('type_de_section', ''),
                    'competence_visee': section_data.get('competences_visees', ''),
                    'ressource': section_data.get('ressource', ''),
                    'intention_ressource': section_data.get('intention_ressource', ''),
                    'activite_1': section_data.get('activite_1', ''),
                    'intention_activite_1': section_data.get('intention_activite_1', ''),
                    'activite_2': section_data.get('activite_2', ''),
                    'intention_activite_2': section_data.get('intention_activite_2', ''),
                    'justification': section_data.get('justification_activite_s', '')
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
    Generate export in the specified format (Markdown or CSV)
    """
    try:
        if format_type == 'markdown':
            return generate_markdown_export(recap_data)
        elif format_type == 'csv':
            return generate_csv_export(recap_data)
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
