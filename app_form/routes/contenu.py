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

def save_yaml_data(data, step_name):
    """Save data to YAML file, updating existing file if it exists"""
    filename = get_session_filename()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Load existing data if file exists
    existing_data = {}
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                existing_data = yaml.safe_load(f) or {}
        except:
            existing_data = {}
    
    # Update with new data
    existing_data[step_name] = data
    existing_data['last_updated'] = datetime.now().isoformat()
    existing_data['current_step'] = step_name
    
    # Save updated data
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(existing_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    return filename

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

def load_rag_resources():
    """
    Load RAG resources for contenus generation
    """
    try:
        # Load the R_03_Tableau_Activites_Ressources.md file
        rag_file_path = os.path.join('ressources', 'Tableau_Activites_Ressources.json')
        
        if os.path.exists(rag_file_path):
            with open(rag_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            print(f"RAG file not found: {rag_file_path}")
            return ""
            
    except Exception as e:
        print(f"Error loading RAG resources: {e}")
        return ""

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
    > **IMPORTANT — L'ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L'INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
    > **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N'EST AUTORISÉE.**  
    > **TOUTES LES RÉPONSES DOIVENT ÊTRE FOURNIES INTÉGRALEMENT EN MARKDOWN BRUT, DANS UN SEUL BLOC TRIPLE BACKTICKS, SANS TEXTE EN DEHORS.**

    ## BUT TECHNIQUE
    Générer automatiquement, pour les sections S2 à S5, un tableau complet des contenus pédagogiques à partir :  
    - du bloc `ordre_competences` validé,  
    - du fichier Markdown `R_03_Tableau_Activites_Ressources.md` (col.1 = id, col.2 = type, col.3 = nom, col.4 = recommandation),  
    - des règles ABC Learning Design définies ci-dessous.

    ## COMPÉTENCES À TRAITER
    {yaml.dump(competences, default_flow_style=False, allow_unicode=True)}

    ## RESSOURCES RAG DISPONIBLES
    {rag_resources}

    ## RÈGLES DE FILTRAGE ET DE SÉLECTION PÉDAGOGIQUE

    1. **Priorité pédagogique générale**  
       - Privilégier : **Acquisition**, **Collaboration**, **Discussion**, **Pratique**.  
       - **Production** et **Enquête** restent présentes mais de façon secondaire.

    2. **Filtrage par recommandation et compétences visées**  
       - Priorité aux entrées avec `recommandation = 3`.  
       - Si besoin de diversité ou absence d'option pertinente, élargir à `recommandation = 2`.  
       - Tenir compte du type de **compétences visées** pour aligner le choix sur le scénario CMO et les intentions ABC Learning Design.  
       - Déterminer l'intention des ressources et activités à partir de la formulation de la compétence ou des verbes d'action :  
         - **Acquisition** → mémoriser, identifier, définir, comprendre  
         - **Entraînement** → appliquer, s'entraîner, mettre en œuvre  
         - **Production** → réaliser, produire, concevoir  
         - **Discussion** → discuter, argumenter, échanger, analyser un point de vue  
         - **Collaboration** → coopérer, co-construire, travailler en groupe  
         - **Enquête** → explorer, enquêter, rechercher

    3. **Filtrage par type de ressource ou activité**  
       - **Ressource principale** : `Ressource` ou `Ressource H5P` avec intention **Acquisition**.  
       - **Activité 1** : `Activité` ou `Activité H5P`, intention en cohérence avec la compétence visée.  
       - **Activité 2** (optionnelle) : uniquement si valeur ajoutée pédagogique et intention complémentaire.  
       - **Activités externes** autorisées si pertinence claire, avec justification RGPD/hébergement si nécessaire.

    4. **Justification obligatoire**  
       - Expliquer la pertinence pédagogique des activités par rapport à la compétence et au modèle ABC Learning Design.

    ## FORMAT DE SORTIE

    - L'assistant produit **uniquement** un tableau Markdown brut dans un seul bloc triple backticks, puis un bloc YAML reprenant exactement les données du tableau.
    - Colonnes du tableau (ordre fixe) :  
      | Section | Type de section | Compétences visées | Ressource | Intention ressource | Activité 1 | Intention activité 1 | Activité 2 | Intention activité 2 | Justification activité(s) |

    **IMPORTANT** : Dans le YAML, utiliser les noms de champs suivants exactement :
    - `section` (pas "Section")
    - `type_de_section` (pas "Type de section")
    - `competences_visees` (pas "Compétences visées")
    - `ressource` (pas "Ressource")
    - `intention_ressource` (pas "Intention ressource")
    - `activite_1` (pas "Activité 1")
    - `intention_activite_1` (pas "Intention activité 1")
    - `activite_2` (pas "Activité 2")
    - `intention_activite_2` (pas "Intention activité 2")
    - `justification_activite_s` (pas "justification_activites" ou "Justification activité(s)")
    
    **IMPORTANT** : Utiliser des chaînes vides `""` au lieu de `null` pour les champs vides.

    **Règles de remplissage** :  
    - **S1 – Accueil** : Type = Accueil, autres colonnes chaînes vides `""`.  
    - **S2 à S5 – Apprentissage** :  
      - Compétences visées = depuis `ordre_competences`.  
      - Ressource, activités et intentions = selon règles ci-dessus.  
      - Justification = obligatoire pour activités.  
    - **S6 – Classe virtuelle (BBB)** : Activité 1 = BigBlueButtonBN, Intention = Discussion.  
    - **S7 – Forum général** : Activité 1 = Forum, Intention = Discussion / Collaboration.  
    - **S8 – Évaluation** : Activité 1 = Sondage Magistère, Intention = Enquête.

    Merci de générer le tableau et le YAML selon ces règles.
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
                    'section': safe_get(section, 'section', 'Section'),
                    'type_de_section': safe_get(section, 'type_de_section', 'Type de section'),
                    'competences_visees': safe_get(section, 'competences_visees', 'Compétences visées'),
                    'ressource': safe_get(section, 'ressource', 'Ressource'),
                    'intention_ressource': safe_get(section, 'intention_ressource', 'Intention ressource'),
                    'activite_1': safe_get(section, 'activite_1', 'Activité 1'),
                    'intention_activite_1': safe_get(section, 'intention_activite_1', 'Intention activité 1'),
                    'activite_2': safe_get(section, 'activite_2', 'Activité 2'),
                    'intention_activite_2': safe_get(section, 'intention_activite_2', 'Intention activité 2'),
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
