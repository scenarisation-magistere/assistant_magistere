from flask import render_template, session, redirect, url_for, request, jsonify
import yaml
import os
from datetime import datetime
from config.pages_config import get_navigation_info, get_page_config
from helpers.ai_helpers import generate_gemini_response
import json
from helpers.session_yaml import (
    get_session_filename,
    save_yaml_data,
    load_yaml_data,
    check_previous_steps_completed,
)
from helpers.resource_loader import load_rag_resources

def generate_contenus_with_ai(competences_data):
    """
    Generate contenus using AI according to A_010_Contenus_Par_Section.md logic
    """
    try:
        # Load the RAG resources for contenus generation
        rag_resources = load_rag_resources()
        
        # Extract competences from the etape_4_competences structure
        competences = extract_competences_from_etape4(competences_data)
        
        # Prepare the prompt for AI generation
        prompt = prepare_contenus_prompt(competences, rag_resources)

        # Save the prompt for debugging
        debug_prompt_path = os.path.join('debug', 'contenus_prompt.txt')
        os.makedirs('debug', exist_ok=True)
        
        try:
            with open(debug_prompt_path, 'w', encoding='utf-8') as f:
                f.write(prompt)
            print(f"Saved contenus prompt to {debug_prompt_path}")
        except Exception as e:
            print(f"Error saving debug prompt: {e}")
        
        # Generate AI response
        ai_response = generate_gemini_response(prompt)

        # Save response for debugging
        debug_response_path = os.path.join('debug', 'contenus_response.txt')
        try:
            with open(debug_response_path, 'w', encoding='utf-8') as f:
                f.write(ai_response)
            print(f"Saved AI response to {debug_response_path}")
        except Exception as e:
            print(f"Error saving debug response: {e}")
        
        # Parse the AI response to extract contenus
        contenus = parse_ai_contenus_response(ai_response)
        
        return contenus
        
    except Exception as e:
        print(f"Error in generate_contenus_with_ai: {e}")
        # Fallback to mock data
        return generate_mock_contenus(competences_data)

 

def extract_competences_from_etape4(competences_data):
    """
    Extract competences from the etape_4_competences structure
    Combines detailed competence information with ordered competences
    """
    competences = []
    
    # Get detailed competence information from individual competence_X entries
    detailed_competences = {}
    i = 1
    while f'competence_{i}' in competences_data:
        comp_data = competences_data[f'competence_{i}']
        code = f'C{i}'
        detailed_competences[code] = {
            'code': code,
            'titre': comp_data.get('titre', ''),
            'niveau': comp_data.get('niveau', ''),
            'idees_cles': comp_data.get('idees_cles', ''),
            'verbes': comp_data.get('verbes', ''),
            'formulation': comp_data.get('formulation', '')
        }
        i += 1
    
    # Get ordered competences from evaluation_competences if available
    evaluation_data = competences_data.get('evaluation_competences', {})
    
    if evaluation_data and 'ordre_competences' in evaluation_data:
        # Merge detailed information with order information
        for ordered_comp in evaluation_data['ordre_competences']:
            code = ordered_comp.get('code', '')
            if code in detailed_competences:
                # Merge detailed info with order info
                merged_comp = {**detailed_competences[code], **ordered_comp}
                competences.append(merged_comp)
            else:
                # If no detailed info available, use order info as is
                competences.append(ordered_comp)
    else:
        # Fallback: use detailed competences in order
        competences = list(detailed_competences.values())
    
    return competences

def prepare_contenus_prompt(competences, rag_resources):
    """
    Prepare the AI prompt for contenus generation according to A_010_Contenus_Par_Section.md
    """
    
    prompt = f"""
        [INSTRUCTION_ASSISTANT] :
        > **IMPORTANT — L'ASSISTANT DOIT FOURNIR UNIQUEMENT DU JSON BRUT DANS UN SEUL BLOC TRIPLE BACKTICKS, SANS TEXTE EN DEHORS.**

        ## BUT TECHNIQUE
        Générer automatiquement un objet JSON par compétence à partir :  
        - des compétences à traiter (avec leur code C1, C2, …),
        - des activités et ressources disponibles,  
        - des règles ABC Learning Design ci-dessous.

        ----------------------------

        ## COMPÉTENCES À TRAITER
        {yaml.dump(competences, default_flow_style=False, allow_unicode=True)}

        ----------------------------

        ## LISTES DES ACTIVITÉS ET RESSOURCES DISPONIBLES
        {rag_resources}

        ----------------------------

        ## RÈGLES DE SÉLECTION

        1. **Priorités pédagogiques (CMO hybride — ABC Learning Design)**  
        Prioriser dans cet ordre : **Acquisition, Collaboration, Discussion, Pratique**.  
        → **Production** et **Enquête** seulement en complément si nécessaire.

        2. **Filtrage par recommandation (R_03)**  
        - Sélectionner d’abord les entrées avec `recommandation = 3`.  
        - Si nécessaire (diversité ou absence d’option pertinente), élargir à `recommandation = 2`.  
        - Tenir compte du **type** et de l’**intention** indiqués dans R_03.

        3. **Filtrage par type de ressource / activité (aligné sur R_03)**  
        - **Ressource principale** : toujours de type `Ressource` ou `Ressource H5P`.  
            - Intention = **Acquisition systématiquement**.  
            - Exemples : Page, Fichier, Ressource H5P (Course Presentation, Interactive Book…).  
        - **Activité 1** : de type `Activité` ou `Activité H5P`.  
            - Intention en cohérence avec la compétence visée.  
            - Exemple : si compétence = Collaboration → choisir activité collaborative (Forum, Atelier, Wiki, Padlet/H5P collaboratif…).  
        - **Activité 2** (optionnelle) : proposer seulement si la compétence est complexe/multifacette et nécessite deux angles pédagogiques.  
            - Ne pas ajouter si redondant ou sans valeur ajoutée claire.  
        - **Activités externes** : autorisées uniquement si clairement pertinentes, avec justification RGPD/hébergement explicite.

        4. **Justification obligatoire**  
        - Expliquer en 2–3 phrases max pourquoi :  
            - la **ressource** (intention Acquisition) est pertinente,  
            - l’**activité 1** correspond à la compétence,  
            - et éventuellement l’**activité 2** si présente.  
        - Justification pédagogique centrée sur l’alignement avec la compétence et les priorités ABC Learning Design.  
        - Éviter tout discours technique sur l’outil.

        ----------------------------

        ## FORMAT DE SORTIE

        - Réponse = JSON brut dans un seul bloc triple backticks.
        - Chaque compétence devient un objet JSON.
        - Champs obligatoires :
        - `code_competence` (ex: "C1")
        - `titre_competence`
        - `niveau_competence`
        - `competences_visees`
        - `ressource`
        - `intention_ressource`
        - `justification_ressource`
        - `activite_1`
        - `intention_activite_1`
        - `justification_activite_1`
        - `activite_2`
        - `intention_activite_2`
        - `justification_activite_2`
        - Utiliser `""` pour les champs vides.

        Merci de générer le JSON selon ces règles.
    """
    
    return prompt

def parse_ai_contenus_response(ai_response):
    """
    Parse the AI response to extract contenus data
    Returns the complete table data as expected by the frontend
    """
    try:
        def _normalize_value(value):
            if value is None:
                return ''
            try:
                # Convert lists/dicts to compact strings to avoid [object Object]
                if isinstance(value, (list, dict)):
                    return yaml.safe_dump(value, allow_unicode=True, default_flow_style=True).strip()
                return str(value)
            except Exception:
                return ''

        def _to_formatted_sections(raw_sections):
            formatted_sections_local = []

            for section in raw_sections:
                section = section or {}

                def safe_get(data, *keys):
                    for key in keys:
                        if key in data:
                            return _normalize_value(data[key])
                    return ''

                formatted_section_local = {
                    'code_competence': safe_get(section, 'code_competence', 'code', 'Code', 'competence_code'),
                    'titre_competence': safe_get(section, 'titre_competence', 'titre', 'title', 'Titre'),
                    'niveau_competence': safe_get(section, 'niveau_competence', 'niveau', 'level', 'Niveau'),
                    'section': safe_get(section, 'section', 'Section'),
                    'type_de_section': safe_get(section, 'type_de_section', 'Type de section'),
                    'competences_visees': safe_get(section, 'competences_visees', 'competence_visee', 'Compétences visées', 'Compétence visée'),
                    'ressource': safe_get(section, 'ressource', 'Ressource'),
                    'intention_ressource': safe_get(section, 'intention_ressource', 'Intention ressource'),
                    'justification_ressource': safe_get(section, 'justification_ressource', 'Justification ressource'),
                    'activite_1': safe_get(section, 'activite_1', 'Activité 1'),
                    'intention_activite_1': safe_get(section, 'intention_activite_1', 'Intention activité 1'),
                    'justification_activite_1': safe_get(section, 'justification_activite_1', 'Justification activité 1'),
                    'activite_2': safe_get(section, 'activite_2', 'Activité 2'),
                    'intention_activite_2': safe_get(section, 'intention_activite_2', 'Intention activité 2'),
                    'justification_activite_2': safe_get(section, 'justification_activite_2', 'Justification activité 2'),
                    'justification_activite_s': safe_get(section, 'justification_activite_s', 'justification_activites', 'Justification activité(s)')
                }

                # Ensure all keys exist and are strings
                for k in list(formatted_section_local.keys()):
                    formatted_section_local[k] = _normalize_value(formatted_section_local.get(k))

                formatted_sections_local.append(formatted_section_local)

            return formatted_sections_local

        # 1) Try YAML fenced blocks first (```yaml or ```yml or last code block looking like YAML)
        def extract_fenced_blocks(text):
            blocks = []
            fence = '```'
            idx = 0
            while True:
                start = text.find(fence, idx)
                if start == -1:
                    break
                lang_start = start + len(fence)
                newline = text.find('\n', lang_start)
                if newline == -1:
                    break
                lang = text[lang_start:newline].strip()
                end = text.find(fence, newline + 1)
                if end == -1:
                    break
                content = text[newline + 1:end]
                blocks.append((lang.lower(), content))
                idx = end + len(fence)
            return blocks

        fenced_blocks = extract_fenced_blocks(ai_response)

        # Try explicit YAML blocks first
        for lang, content in fenced_blocks:
            if lang in ('yaml', 'yml'):
                try:
                    contenus_data = yaml.safe_load(content)
                    if contenus_data is not None:
                        if isinstance(contenus_data, list):
                            return _to_formatted_sections(contenus_data)
                        if isinstance(contenus_data, dict):
                            if 'contenus_par_section' in contenus_data and isinstance(contenus_data['contenus_par_section'], list):
                                return _to_formatted_sections(contenus_data['contenus_par_section'])
                except Exception:
                    pass

        # If not found, attempt to parse any fenced block that looks like YAML (starts with '-' or 'section:')
        for lang, content in reversed(fenced_blocks):
            if lang in ('', 'markdown', 'md', 'text', 'txt', 'python', 'json', 'yaml', 'yml'):
                content_stripped = content.strip()
                if content_stripped.startswith('- ') or content_stripped.startswith('section:') or content_stripped.startswith('[') or content_stripped.startswith('{'):
                    # Try YAML first
                    try:
                        contenus_data = yaml.safe_load(content_stripped)
                        if contenus_data is not None:
                            if isinstance(contenus_data, list):
                                return _to_formatted_sections(contenus_data)
                            if isinstance(contenus_data, dict):
                                # Could be JSON/dict style with key
                                if 'contenus_par_section' in contenus_data and isinstance(contenus_data['contenus_par_section'], list):
                                    return _to_formatted_sections(contenus_data['contenus_par_section'])
                    except Exception:
                        pass
                    # Try JSON second
                    try:
                        import json
                        contenus_data = json.loads(content_stripped)
                        if isinstance(contenus_data, list):
                            return _to_formatted_sections(contenus_data)
                        if isinstance(contenus_data, dict):
                            if 'contenus_par_section' in contenus_data and isinstance(contenus_data['contenus_par_section'], list):
                                return _to_formatted_sections(contenus_data['contenus_par_section'])
                    except Exception:
                        pass

        # 2) If still nothing, try to parse Markdown table anywhere in the response
        def parse_markdown_table(text):
            lines = [ln.rstrip() for ln in text.splitlines()]
            # Find header line with pipes and required headers
            header_idx = -1
            for i, ln in enumerate(lines):
                if '|' in ln and 'Section' in ln and 'Type de section' in ln:
                    header_idx = i
                    break
            if header_idx == -1 or header_idx + 2 >= len(lines):
                return []
            header_line = lines[header_idx]
            separator_line = lines[header_idx + 1]
            if '---' not in separator_line:
                return []
            headers = [h.strip() for h in header_line.strip('|').split('|')]
            rows = []
            i = header_idx + 2
            while i < len(lines):
                ln = lines[i]
                if not ln.strip().startswith('|'):
                    i += 1
                    continue
                cells = [c.strip() for c in ln.strip().strip('|').split('|')]
                if len(cells) != len(headers):
                    i += 1
                    continue
                row = dict(zip(headers, cells))
                rows.append(row)
                i += 1
            # Map headers to expected keys
            mapped = []
            for row in rows:
                mapped.append({
                    'section': _normalize_value(row.get('Section', '')),
                    'type_de_section': _normalize_value(row.get('Type de section', '')),
                    'competences_visees': _normalize_value(row.get('Compétences visées', '')),
                    'ressource': _normalize_value(row.get('Ressource', '')),
                    'intention_ressource': _normalize_value(row.get('Intention ressource', '')),
                    'activite_1': _normalize_value(row.get('Activité 1', '')),
                    'intention_activite_1': _normalize_value(row.get('Intention activité 1', '')),
                    'activite_2': _normalize_value(row.get('Activité 2', '')),
                    'intention_activite_2': _normalize_value(row.get('Intention activité 2', '')),
                    'justification_activite_s': _normalize_value(row.get('Justification activité(s)', '')),
                })
            return mapped

        table_sections = parse_markdown_table(ai_response)
        if table_sections:
            return _to_formatted_sections(table_sections)

        # 3) As last resort, try to parse the entire response as YAML/JSON
        try:
            contenus_data = yaml.safe_load(ai_response)
            if isinstance(contenus_data, list):
                return _to_formatted_sections(contenus_data)
            if isinstance(contenus_data, dict) and 'contenus_par_section' in contenus_data:
                return _to_formatted_sections(contenus_data['contenus_par_section'])
        except Exception:
            pass
        try:
            import json
            contenus_data = json.loads(ai_response)
            if isinstance(contenus_data, list):
                return _to_formatted_sections(contenus_data)
            if isinstance(contenus_data, dict) and 'contenus_par_section' in contenus_data:
                return _to_formatted_sections(contenus_data['contenus_par_section'])
        except Exception:
            pass

        return []
    except Exception as e:
        print(f"Error parsing AI response: {e}")
        return []

def extract_competence_code(competence_formulation):
    """
    Extract competence code from formulation (e.g., "C1 - Identifier..." -> "C1")
    """
    import re
    match = re.match(r'^([A-Z]\d+)', competence_formulation)
    if match:
        return match.group(1)
    return None

def generate_mock_contenus(competences_data):
    """
    Generate mock contenus data as fallback
    Returns the same format as AI response for consistency
    """
    competences = extract_competences_from_etape4(competences_data)
    
    # Create mock sections following the same structure as AI response
    mock_sections = [
        {
            'section': 'S1',
            'type_de_section': 'Accueil',
            'competences_visees': '',
            'ressource': '',
            'intention_ressource': '',
            'activite_1': '',
            'intention_activite_1': '',
            'activite_2': '',
            'intention_activite_2': '',
            'justification_activite_s': ''
        }
    ]
    
    # Add learning sections for each competence
    for i, competence in enumerate(competences, 2):
        mock_sections.append({
            'section': f'S{i}',
            'type_de_section': 'Apprentissage',
            'competences_visees': f"{competence['code']} - {competence['formulation']}",
            'ressource': 'Page de contenu',
            'intention_ressource': 'Acquisition',
            'activite_1': 'Quiz interactif',
            'intention_activite_1': 'Pratique',
            'activite_2': 'Exercice interactif',
            'intention_activite_2': 'Production',
            'justification_activite_s': f'Ressource pour l\'acquisition de {competence["formulation"]}. Quiz pour valider la compréhension. Exercice pour appliquer les connaissances.'
        })
    
    # Add standard sections
    mock_sections.extend([
        {
            'section': f'S{len(competences) + 2}',
            'type_de_section': 'Classe virtuelle (BBB)',
            'competences_visees': '',
            'ressource': '',
            'intention_ressource': '',
            'activite_1': 'BigBlueButtonBN',
            'intention_activite_1': 'Discussion',
            'activite_2': '',
            'intention_activite_2': '',
            'justification_activite_s': ''
        },
        {
            'section': f'S{len(competences) + 3}',
            'type_de_section': 'Forum général',
            'competences_visees': '',
            'ressource': '',
            'intention_ressource': '',
            'activite_1': 'Forum',
            'intention_activite_1': 'Discussion / Collaboration',
            'activite_2': '',
            'intention_activite_2': '',
            'justification_activite_s': ''
        },
        {
            'section': f'S{len(competences) + 4}',
            'type_de_section': 'Évaluation',
            'competences_visees': '',
            'ressource': '',
            'intention_ressource': '',
            'activite_1': 'Sondage',
            'intention_activite_1': 'Enquête',
            'activite_2': '',
            'intention_activite_2': '',
            'justification_activite_s': ''
        }
    ])
    
    return mock_sections

def register_contenu_routes(app):
    """Register contenu routes with the Flask app"""
    
    @app.route('/contenu', methods=['GET', 'POST'])
    def contenu():
        if request.method == 'POST':
            # Handle form submission
            data = request.form.to_dict()
            filename = save_yaml_data(data, 'etape_5_contenu')
            return redirect('/')
        
        # Check if referentiels step is completed
        completed, message = check_previous_steps_completed(['etape_1_public_cible', 'etape_2_contraintes', 'etape_4_competences', 'etape_5_referentiels'])
        if not completed:
            return render_template('error.html', message=f"Veuillez d'abord compléter les étapes précédentes. {message}")
        
        nav_info = get_navigation_info('contenu')
        page_config = get_page_config('contenu')
        
        # Load competences data for display
        competences_data = load_yaml_data()
        
        # Extract competences for template display
        competences_for_display = None
        if competences_data and 'etape_4_competences' in competences_data:
            competences_for_display = extract_competences_from_etape4(competences_data['etape_4_competences'])
        
        return render_template('contenu.html', 
                             nav_info=nav_info,
                             header_gradient=page_config.get('header_gradient', 'var(--gradient-info)'),
                             competences_data=competences_data,
                             competences_for_display=competences_for_display,
                             header_title='📚 Contenus par Section',
                             header_description='Génération automatique des contenus pédagogiques pour chaque compétence')

    # API routes for contenu page
    @app.route('/get_competences_data', methods=['GET'])
    def get_competences_data():
        try:
            competences_data = load_yaml_data()
            if competences_data and 'etape_4_competences' in competences_data:
                # Extract competences in the format expected by the frontend
                etape3_data = competences_data['etape_4_competences']
                competences = extract_competences_from_etape4(etape3_data)
                print(competences)
                
                return jsonify({
                    'success': True,
                    'competences': {
                        'ordre_competences': competences
                    },
                    'etape3_data': etape3_data
                })
            else:
                return jsonify({
                    'success': False,
                    'error': 'Aucune donnée de compétences trouvée'
                })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/generate_contenus', methods=['POST'])
    def generate_contenus():
        try:
            # Load competences data
            competences_data = load_yaml_data()
            if not competences_data or 'etape_4_competences' not in competences_data:
                return jsonify({
                    'success': False,
                    'error': 'Aucune donnée de compétences trouvée'
                })
            
            # Generate contenus using AI
            contenus = generate_contenus_with_ai(competences_data['etape_4_competences'])
            
            return jsonify({
                'success': True,
                'contenus': contenus
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/save_contenus', methods=['POST'])
    def save_contenus():
        try:
            data = request.get_json()
            filename = save_yaml_data(data, 'etape_5_contenu')
            return jsonify({
                'success': True,
                'filename': filename
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/get_resources_catalog', methods=['GET'])
    def get_resources_catalog():
        try:
            rag_file_path = os.path.join('ressources', 'Tableau_Activites_Ressources.json')
            if not os.path.exists(rag_file_path):
                return jsonify({'success': False, 'error': 'Catalogue non trouvé'})
            with open(rag_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            # Ensure it's a list of dicts
            if not isinstance(data, list):
                return jsonify({'success': False, 'error': 'Format de catalogue invalide'})
            return jsonify({'success': True, 'items': data})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
