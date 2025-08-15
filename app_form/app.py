from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import yaml
import os
import re
import requests
import json
from datetime import datetime

# Import questions from separate files
from questions.public_cible import QUESTIONS_PUBLIC_CIBLE
from questions.contraintes import QUESTIONS_CONTRAINTES
from questions.scenario import CMO_SCENARIO
from questions.competences import COMPETENCES_QUESTIONS, get_competences_with_count, get_next_competence_number, reorder_competences, generate_competence_template

# Import AI helpers
from ai_helpers import generate_competency_suggestions, generate_verb_suggestions_for_level, evaluate_and_order_competences

# Import referentiels functions
from questions.referentiels import referentiels_page, generate_referentiel, save_referentiel, update_referentiel

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

# Create output directory if it doesn't exist
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Generate a unique session ID for this run
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

def check_migration_warning(type_parcours):
    """Check if migration warning should be displayed"""
    if not type_parcours:
        return False
    
    migration_keywords = ['migration', 'migrer', 'migrer un parcours', 'migration parcours']
    type_parcours_lower = type_parcours.lower()
    
    for keyword in migration_keywords:
        if keyword in type_parcours_lower:
            return True
    return False

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

@app.route('/')
def index():
    return render_template('public_cible.html', questions=QUESTIONS_PUBLIC_CIBLE, step=1, total_steps=5)

@app.route('/contraintes')
def contraintes():
    # Check if public_cible step is completed
    completed, message = check_previous_steps_completed(['etape_1_public_cible'])
    if not completed:
        return render_template('error.html', message=f"Veuillez d'abord compléter l'étape Public Cible. {message}")
    
    return render_template('contraintes.html', questions=QUESTIONS_CONTRAINTES, step=2, total_steps=5)

@app.route('/scenario')
def scenario():
    # Check if previous steps are completed
    completed, message = check_previous_steps_completed(['etape_1_public_cible', 'etape_2_contraintes'])
    if not completed:
        return render_template('error.html', message=f"Veuillez d'abord compléter les étapes précédentes. {message}")
    
    return render_template('scenario.html', scenario=CMO_SCENARIO, step=3, total_steps=5)

@app.route('/competences')
def competences():
    # Check if previous steps are completed
    completed, message = check_previous_steps_completed(['etape_1_public_cible', 'etape_2_contraintes', 'etape_3_scenario'])
    if not completed:
        return render_template('error.html', message=f"Veuillez d'abord compléter les étapes précédentes. {message}")
    
    # Load previous data from YAML file
    public_cible_data = None
    if 'session_id' in session:
        filename = get_session_filename()
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    yaml_data = yaml.safe_load(f) or {}
                    public_cible_data = yaml_data.get('etape_1_public_cible', {})
            except:
                pass
    
    # Get competence count from session or default to 0 (start with no competences)
    competence_count = session.get('competence_count', 0)
    competences = get_competences_with_count(competence_count)
    
    return render_template('competences.html', 
                         competences=competences,
                         verb_suggestions=COMPETENCES_QUESTIONS['verb_suggestions'],
                         public_cible_data=public_cible_data,
                         step=4, 
                         total_steps=5)

@app.route('/add_competence', methods=['POST'])
def add_competence():
    """Add a new competence to the form"""
    try:
        # Get current competence count from session
        competence_count = session.get('competence_count', 0)
        new_count = competence_count + 1
        
        # Update session
        session['competence_count'] = new_count
        
        # Generate new competence template with proper numbering
        new_competence = generate_competence_template(new_count)
        
        return jsonify({
            'success': True,
            'competence': new_competence,
            'competence_count': new_count
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/remove_competence', methods=['POST'])
def remove_competence():
    """Remove a competence from the form"""
    try:
        data = request.get_json()
        competence_number = data.get('competence_number')
        
        # Get current competence count from session
        competence_count = session.get('competence_count', 0)
        
        if competence_count <= 0:
            return jsonify({
                'success': False,
                'error': 'Aucune compétence à supprimer'
            })
        
        new_count = competence_count - 1
        session['competence_count'] = new_count
        
        return jsonify({
            'success': True,
            'competence_count': new_count
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/reorder_competences', methods=['POST'])
def reorder_competences_route():
    """Reorder competences to ensure sequential numbering"""
    try:
        data = request.get_json()
        current_competences = data.get('competences', [])
        
        # Reorder competences
        reordered_competences = reorder_competences(current_competences)
        
        # Update session count
        session['competence_count'] = len(reordered_competences)
        
        return jsonify({
            'success': True,
            'competences': reordered_competences,
            'competence_count': len(reordered_competences)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/get_verb_suggestions/<niveau>')
def get_verb_suggestions(niveau):
    """Get verb suggestions for a specific cognitive level"""
    try:
        suggestions = generate_verb_suggestions_for_level(niveau)
        return jsonify({
            'success': True,
            'suggestions': suggestions,
            'niveau': niveau
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/get_bloom_verbs/<niveau>')
def get_bloom_verbs(niveau):
    """Get Bloom taxonomy verbs for a specific level"""
    try:
        from questions.competences import COMPETENCES_QUESTIONS
        
        # Map niveau to bloom taxonomy keys
        niveau_mapping = {
            'Haut : Créer / Évaluer / Analyser': ['creer', 'evaluer', 'analyser', 'caracteriser', 'organiser'],
            'Moyen : Appliquer / Comprendre': ['appliquer', 'comprendre', 'valoriser', 'repondre'],
            'Bas : Se rappeler': ['se_rappeler', 'recevoir']
        }
        
        bloom_taxonomy = COMPETENCES_QUESTIONS.get('bloom_taxonomy', {})
        selected_levels = niveau_mapping.get(niveau, [])
        
        result = {}
        for level in selected_levels:
            if level in bloom_taxonomy:
                result[level] = bloom_taxonomy[level]
        
        return jsonify({
            'success': True,
            'bloom_verbs': result,
            'niveau': niveau
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/generate_ai_suggestions', methods=['POST'])
def generate_ai_suggestions():
    """Generate AI suggestions for competencies based on formation data"""
    try:
        # Load formation data from YAML file
        if 'session_id' not in session:
            return jsonify({
                'success': False,
                'error': 'Aucune session active. Veuillez recommencer le questionnaire.'
            })
        
        filename = get_session_filename()
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if not os.path.exists(filepath):
            return jsonify({
                'success': False,
                'error': 'Fichier de données non trouvé. Veuillez recommencer le questionnaire.'
            })
        
        # Load complete YAML data
        with open(filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f) or {}
        
        # Pass the complete YAML data to the AI function
        result = generate_competency_suggestions(yaml_data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'suggestions': result['suggestions'],
                'message': 'Suggestions générées avec succès !'
            })
        else:
            return jsonify({
                'success': False,
                'error': result['error']
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erreur lors de la génération des suggestions : {str(e)}'
        })

@app.route('/submit_public_cible', methods=['POST'])
def submit_public_cible():
    data = request.get_json()
    
    # Store in session for later use
    session['public_cible_data'] = data
    
    # Generate YAML data for this step
    yaml_data = {
        'public_cible': {
            'type': data.get('type_de_public', []),
            'profil': data.get('profil_groupe', ''),
            'niveau_expertise': data.get('niveau_expertise', ''),
            'besoins_specifiques': data.get('besoins_specifiques', []),
            'recommandations': [
                'À compléter ou à reformuler en fonction du profil et des besoins'
            ]
        },
        'contexte_formation': {
            'titre': data.get('titre_formation', ''),
            'objectif_general': data.get('objectif_general', '')
        }
    }
    
    # Save to file
    filename = save_yaml_data(yaml_data, 'etape_1_public_cible')
    
    return jsonify({
        'success': True,
        'message': f'Données du public cible sauvegardées dans {filename}. Redirection vers les contraintes...',
        'yaml_data': yaml_data,
        'filename': filename,
        'redirect': '/contraintes'
    })

@app.route('/submit_contraintes', methods=['POST'])
def submit_contraintes():
    data = request.get_json()
    
    # Check for migration warning
    migration_warning = check_migration_warning(data.get('type_parcours', ''))
    
    # Store complete data in session
    session['complete_data'] = {
        'public_cible': session.get('public_cible_data', {}),
        'contraintes': data
    }
    
    # Generate YAML data for this step - only save contraintes data
    yaml_data = {
        'contraintes_formation': {
            'type_parcours': data.get('type_parcours', ''),
            'temps_total': data.get('temps_total', ''),
            'autonomie': data.get('autonomie', ''),
            'animation': data.get('animation', ''),
            'calendrier': data.get('calendrier', ''),
            'horaires': data.get('horaires', ''),
            'nombre_participants': data.get('nombre_participants', ''),
            'exigences_institutionnelles': data.get('exigences_institutionnelles', ''),
            'restrictions_techniques': data.get('restrictions_techniques', ''),
            'exemple_associe': '001C_Exemple_Contraintes_Formation.md'
        }
    }
    
    # Save to file
    filename = save_yaml_data(yaml_data, 'etape_2_contraintes')
    
    return jsonify({
        'success': True,
        'message': f'Données des contraintes sauvegardées dans {filename}. Redirection vers le scénario CMO...',
        'yaml_data': yaml_data,
        'migration_warning': migration_warning,
        'filename': filename,
        'redirect': '/scenario'
    })

@app.route('/submit_scenario', methods=['POST'])
def submit_scenario():
    """Submit scenario step - this is mainly informational but we save the acknowledgment"""
    data = request.get_json()
    
    # Generate YAML data for this step
    yaml_data = {
        'scenario_cmo': {
            'title': CMO_SCENARIO['title'],
            'description': CMO_SCENARIO['description'],
            'features': CMO_SCENARIO['features'],
            'sections': CMO_SCENARIO['sections'],
            'constraints': CMO_SCENARIO['constraints'],
            'acknowledged': True,
            'timestamp': datetime.now().isoformat()
        }
    }
    
    # Save to file
    filename = save_yaml_data(yaml_data, 'etape_3_scenario')
    
    return jsonify({
        'success': True,
        'message': f'Scénario CMO sauvegardé dans {filename}. Redirection vers les compétences...',
        'yaml_data': yaml_data,
        'filename': filename,
        'redirect': '/competences'
    })

@app.route('/submit_competences', methods=['POST'])
def submit_competences():
    data = request.get_json()
    
    # Load existing data from YAML file
    existing_data = {}
    if 'session_id' in session:
        filename = get_session_filename()
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    existing_data = yaml.safe_load(f) or {}
            except:
                existing_data = {}
    
    # Generate YAML data for competencies
    competences_data = {
        'formulations_competences': []
    }
    
    # Count competences from the data
    competence_count = 0
    for key in data.keys():
        if key.startswith('formulation_'):
            competence_count = max(competence_count, int(key.split('_')[1]))
    
    # Extract formulations for each competence
    for i in range(1, competence_count + 1):
        formulation = data.get(f'formulation_{i}', '')
        if formulation:
            competences_data['formulations_competences'].append(formulation)
    
    # Add detailed data for each competence
    for i in range(1, competence_count + 1):
        competence_key = f'competence_{i}'
        competences_data[competence_key] = {
            'titre': data.get(f'titre_{i}', ''),
            'idees_cles': data.get(f'idees_cles_{i}', ''),
            'niveau': data.get(f'niveau_{i}', ''),
            'verbes': data.get(f'verbes_{i}', ''),
            'formulation': data.get(f'formulation_{i}', '')
        }
    
    # Update session competence count
    session['competence_count'] = competence_count
    
    # Save the competences data
    filename = save_yaml_data(competences_data, 'etape_4_competences')
    
    # Combine with existing data for response
    complete_yaml_data = existing_data.copy()
    complete_yaml_data['etape_4_competences'] = competences_data
    
    return jsonify({
        'success': True,
        'message': f'Compétences visées sauvegardées dans {filename}. Questionnaire terminé !',
        'yaml_data': complete_yaml_data,
        'filename': filename
    })

@app.route('/evaluate_and_order_competences', methods=['POST'])
def evaluate_and_order_competences_route():
    """Evaluate and order competences using the current YAML data."""
    try:
        # Load current YAML data
        yaml_data = {}
        if 'session_id' in session:
            filename = get_session_filename()
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        yaml_data = yaml.safe_load(f) or {}
                except:
                    yaml_data = {}
        
        # Evaluate and order competences
        result = evaluate_and_order_competences(yaml_data)

        print(result)
        
        if result['success']:
            # Save only the evaluation data, not the complete data
            filename = save_yaml_data(result['evaluation'], 'evaluation_competences')
            
            return jsonify({
                'success': True,
                'evaluation': result['evaluation'],
                'filename': filename,
                'message': 'Évaluation et ordonnancement des compétences terminé !'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Erreur lors de l\'évaluation'),
                'fallback': result.get('fallback', {})
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/add_suggested_competence', methods=['POST'])
def add_suggested_competence_route():
    """Add the suggested competence from AI evaluation to the competences data"""
    try:
        # Load current YAML data
        yaml_data = {}
        if 'session_id' in session:
            filename = get_session_filename()
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        yaml_data = yaml.safe_load(f) or {}
                except:
                    yaml_data = {}
        
        # Get the suggested competence from evaluation data
        evaluation_data = yaml_data.get('evaluation_competences', {})
        suggested_competence = evaluation_data.get('competence_complementaire', {})
        
        if not suggested_competence:
            return jsonify({
                'success': False,
                'error': 'Aucune compétence suggérée trouvée'
            })
        
        # Add the suggested competence using the AI helper function
        from ai_helpers import add_suggested_competence
        result = add_suggested_competence(yaml_data, suggested_competence)
        
        if result['success']:
            # Save the updated data
            filename = save_yaml_data(yaml_data['etape_4_competences'], 'etape_4_competences')
            
            return jsonify({
                'success': True,
                'message': result['message'],
                'competence_ajoutee': result['competence_ajoutee'],
                'filename': filename
            })
        else:
            return jsonify({
                'success': False,
                'error': result['error']
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erreur lors de l\'ajout de la compétence : {str(e)}'
        })

@app.route('/referentiels')
def referentiels():
    """Handle the referentiels page"""
    # Check if previous steps are completed
    completed, message = check_previous_steps_completed(['etape_1_public_cible', 'etape_2_contraintes', 'etape_3_scenario', 'etape_4_competences'])
    if not completed:
        return render_template('error.html', message=f"Veuillez d'abord compléter les étapes précédentes. {message}")
    return referentiels_page()

@app.route('/generate_referentiel', methods=['POST'])
def generate_referentiel_route():
    """Generate a referentiel for a specific section"""
    return generate_referentiel()

@app.route('/save_referentiel', methods=['POST'])
def save_referentiel_route():
    """Save the referentiel to YAML"""
    return save_referentiel()

@app.route('/update_referentiel', methods=['POST'])
def update_referentiel_route():
    """Update an existing referentiel based on user feedback"""
    return update_referentiel()

@app.route('/contenus')
def contenus():
    """Contenus pédagogiques page - selection of intentions, resources and activities"""
    # Get sections from session data
    sections = []
    if 'session_id' in session:
        filename = get_session_filename()
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    yaml_data = yaml.safe_load(f) or {}
                
                if 'ordre_competences' in yaml_data:
                    sections = yaml_data['ordre_competences'].get('sections', [])
            except Exception as e:
                print(f"Erreur lors du chargement des sections: {str(e)}")
    
    # Get existing contenus
    existing_contenus = []
    if 'session_id' in session:
        filename = get_session_filename()
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    yaml_data = yaml.safe_load(f) or {}
                
                if 'contenus_sections' in yaml_data:
                    existing_contenus = yaml_data['contenus_sections']
            except Exception as e:
                print(f"Erreur lors du chargement des contenus existants: {str(e)}")
    
    return render_template('contenus.html', 
                         step=6, 
                         total_steps=7, 
                         sections=sections,
                         existing_contenus=existing_contenus)

@app.route('/export')
def export():
    """Final export page - allows selection of any YAML file for export"""
    return render_template('export.html', step=7, total_steps=7)

@app.route('/get_available_files')
def get_available_files():
    """Get list of available YAML files in the output directory"""
    try:
        files = []
        if os.path.exists(OUTPUT_DIR):
            for filename in os.listdir(OUTPUT_DIR):
                if filename.endswith('.yaml') or filename.endswith('.yml'):
                    filepath = os.path.join(OUTPUT_DIR, filename)
                    # Get file modification time
                    mtime = os.path.getmtime(filepath)
                    date_str = datetime.fromtimestamp(mtime).strftime('%d/%m/%Y %H:%M')
                    files.append({
                        'filename': filename,
                        'date': date_str
                    })
        
        # Sort files by modification time (newest first)
        files.sort(key=lambda x: x['date'], reverse=True)
        
        return jsonify({
            'success': True,
            'files': files
        })
    except Exception as e:
        return jsonify({'success': False, 'error': f'Erreur lors du chargement de la liste: {str(e)}'})

@app.route('/get_file_data', methods=['POST'])
def get_file_data():
    """Get data from a specific YAML file"""
    try:
        data = request.get_json()
        filename = data.get('filename')
        
        if not filename:
            return jsonify({'success': False, 'error': 'Nom de fichier manquant'})
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if not os.path.exists(filepath):
            return jsonify({'success': False, 'error': 'Fichier non trouvé'})
        
        with open(filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f) or {}
        
        return jsonify({
            'success': True,
            'data': yaml_data
        })
    except Exception as e:
        return jsonify({'success': False, 'error': f'Erreur lors du chargement: {str(e)}'})

@app.route('/get_session_data')
def get_session_data():
    """Get all session data for the export page"""
    if 'session_id' not in session:
        return jsonify({'success': False, 'error': 'Aucune session active'})
    
    filename = get_session_filename()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if not os.path.exists(filepath):
        return jsonify({'success': False, 'error': 'Fichier non trouvé'})
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f) or {}
        
        return jsonify({
            'success': True,
            'data': yaml_data
        })
    except Exception as e:
        return jsonify({'success': False, 'error': f'Erreur lors du chargement: {str(e)}'})



@app.route('/export_data', methods=['POST'])
def export_data():
    """Export data in the requested format"""
    try:
        data = request.get_json()
        format_type = data.get('format', 'markdown')
        generation_type = data.get('generation', 'gpt4')
        yaml_data = data.get('data', {})
        
        if format_type == 'markdown':
            if generation_type == 'gpt4':
                content = generate_markdown_export(yaml_data)
            else:
                content = generate_markdown_fallback(yaml_data)
            filename = f"macrodesign_formation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            mimetype = 'text/markdown'
        elif format_type == 'yaml':
            content = yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
            filename = f"macrodesign_formation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"
            mimetype = 'application/x-yaml'
        else:
            return jsonify({'success': False, 'error': 'Format non supporté'}), 400
        
        from flask import send_file
        from io import BytesIO
        
        # Create file-like object
        file_obj = BytesIO(content.encode('utf-8'))
        file_obj.seek(0)
        
        return send_file(
            file_obj,
            mimetype=mimetype,
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/generate_contenus', methods=['POST'])
def generate_contenus():
    """Generate contenus for a section based on competence"""
    try:
        data = request.get_json()
        section_num = data.get('section_num')
        competence = data.get('competence')
        
        if not section_num or not competence:
            return jsonify({'success': False, 'error': 'Données manquantes'})
        
        # Import OpenAI client
        from openai import OpenAI
        import os
        
        # Initialize OpenAI client
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Create prompt for contenus generation
        prompt = f"""
Tu es un expert en pédagogie et en conception de formation. Tu dois sélectionner automatiquement les contenus pédagogiques pour une section d'apprentissage basée sur la compétence suivante.

Compétence de la section {section_num} : {competence}

Selon les règles ABC Learning Design et les prompts A_010a et A_010b, tu dois sélectionner :

1. **Intention secondaire ABC** selon le type de compétence :
   - Mémorisation/compréhension → Acquisition (déjà incluse)
   - Application/entraînement → Entraînement
   - Restitution/réalisation → Production
   - Réflexion/posture → Discussion
   - Coopération/co-construction → Collaboration
   - Exploration/investigation → Enquête

2. **Ressource principale** (1 seule, type "Ressource" ou "Ressource H5P", priorité recommandation=3)

3. **Activité principale** (obligatoire, type "Activité" ou "Activité H5P", priorité recommandation=3)

4. **Activité secondaire** (optionnelle si utile, même critères)

5. **Discussion contextualisée** pour le forum

6. **Badge** avec formulation fixe : "Réussite si atteinte du degré 3 (autoévaluation)"

Pour chaque sélection, fournis une justification pédagogique.

Retourne un objet JSON avec cette structure :
{{
    "section": {section_num},
    "intention_secondaire": "Nom de l'intention",
    "ressource_principale": {{
        "id": "ID de la ressource",
        "type": "Type de ressource",
        "nom": "Nom de la ressource"
    }},
    "activite_principale": {{
        "id": "ID de l'activité",
        "type": "Type d'activité",
        "nom": "Nom de l'activité"
    }},
    "activite_secondaire": {{
        "id": "ID de l'activité",
        "type": "Type d'activité",
        "nom": "Nom de l'activité"
    }},
    "discussion": "Description de la discussion contextualisée",
    "justification_intention": "Justification de l'intention choisie",
    "justification_ressource": "Justification de la ressource choisie",
    "justification_activite1": "Justification de l'activité principale",
    "justification_activite2": "Justification de l'activité secondaire"
}}

Note : Pour les ressources et activités, utilise des exemples réalistes basés sur des outils pédagogiques courants (Moodle, H5P, etc.).
"""
        
        # Call GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un expert en pédagogie qui sélectionne des contenus pédagogiques selon les règles ABC Learning Design."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        # Extract the generated contenus
        contenus_content = response.choices[0].message.content.strip()
        
        # Parse JSON response
        import json
        try:
            contenus_data = json.loads(contenus_content)
            return jsonify({
                'success': True,
                'contenus': contenus_data
            })
        except json.JSONDecodeError:
            # Fallback to manual generation
            return jsonify({
                'success': True,
                'contenus': generate_contenus_fallback(section_num, competence)
            })
        
    except Exception as e:
        print(f"Erreur lors de la génération des contenus: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

def generate_contenus_fallback(section_num, competence):
    """Fallback manual contenus generation"""
    return {
        "section": section_num,
        "intention_secondaire": "Entraînement",
        "ressource_principale": {
            "id": "RES001",
            "type": "Ressource H5P",
            "nom": "Vidéo interactive avec quiz"
        },
        "activite_principale": {
            "id": "ACT001",
            "type": "Activité H5P",
            "nom": "Exercice d'application"
        },
        "activite_secondaire": {
            "id": "ACT002",
            "type": "Activité",
            "nom": "Devoir à rendre"
        },
        "discussion": f"Partagez vos expériences et difficultés rencontrées dans l'acquisition de la compétence : {competence}",
        "justification_intention": "Intention Entraînement pour permettre l'application pratique",
        "justification_ressource": "Ressource interactive adaptée à l'apprentissage",
        "justification_activite1": "Activité principale pour valider la compétence",
        "justification_activite2": "Activité complémentaire pour approfondir"
    }

@app.route('/save_contenus', methods=['POST'])
def save_contenus():
    """Save contenus to YAML file"""
    try:
        data = request.get_json()
        contenus = data.get('contenus')
        
        if not contenus:
            return jsonify({'success': False, 'error': 'Données manquantes'})
        
        if 'session_id' not in session:
            return jsonify({'success': False, 'error': 'Aucune session active'})
        
        filename = get_session_filename()
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Load existing data
        yaml_data = {}
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                yaml_data = yaml.safe_load(f) or {}
        
        # Initialize contenus_sections if not exists
        if 'contenus_sections' not in yaml_data:
            yaml_data['contenus_sections'] = []
        
        # Add or update contenus
        section_num = contenus.get('section')
        existing_index = None
        
        for i, existing in enumerate(yaml_data['contenus_sections']):
            if existing.get('section') == section_num:
                existing_index = i
                break
        
        if existing_index is not None:
            yaml_data['contenus_sections'][existing_index] = contenus
        else:
            yaml_data['contenus_sections'].append(contenus)
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        return jsonify({'success': True})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def generate_markdown_export(yaml_data):
    """Generate complete markdown export using GPT-4"""
    try:
        # Import OpenAI client
        from openai import OpenAI
        import os
        
        # Initialize OpenAI client
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Create a comprehensive prompt for GPT-4
        prompt = f"""
Tu es un expert en pédagogie et en conception de formation. Tu dois créer un document Markdown professionnel et complet pour un macrodesign pédagogique basé sur les données suivantes.

Voici les données du macrodesign au format YAML :

```yaml
{yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True, sort_keys=False)}
```

Crée un document Markdown complet et professionnel qui :

1. **Structure claire** : Utilise une hiérarchie de titres appropriée (# pour le titre principal, ## pour les sections principales, ### pour les sous-sections)
2. **Formatage riche** : Utilise les emojis appropriés, le gras, l'italique, les listes à puces et numérotées
3. **Contenu complet** : Inclus toutes les informations importantes des données YAML
4. **Style professionnel** : Rédige un document qui pourrait être utilisé dans un contexte professionnel de formation
5. **Organisation logique** : Structure le document de manière logique et pédagogique

Le document doit inclure :
- Un titre principal attractif
- Une section d'informations générales avec public cible, contraintes, et contexte
- Une section détaillée sur les compétences visées
- Une section complète sur les référentiels d'autoévaluation avec tous les niveaux
- Un pied de page professionnel

Utilise des emojis appropriés pour rendre le document visuellement attractif.
Assure-toi que le document soit bien structuré et facile à lire.

Retourne uniquement le contenu Markdown, sans commentaires supplémentaires.
"""
        
        # Call GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un expert en pédagogie et en rédaction de documents de formation. Tu crées des documents Markdown professionnels et bien structurés."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=4000
        )
        
        # Extract the generated markdown
        markdown_content = response.choices[0].message.content.strip()
        
        # Add timestamp at the beginning
        timestamp = f"*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}*"
        if markdown_content.startswith("#"):
            # Insert timestamp after the first line
            lines = markdown_content.split('\n', 1)
            markdown_content = f"{lines[0]}\n{timestamp}\n{lines[1] if len(lines) > 1 else ''}"
        
        return markdown_content
        
    except Exception as e:
        # Fallback to manual generation if GPT-4 fails
        print(f"Erreur lors de la génération avec GPT-4: {str(e)}")
        return generate_markdown_fallback(yaml_data)

def generate_markdown_fallback(yaml_data):
    """Fallback manual markdown generation if GPT-4 fails"""
    lines = []
    
    # Header
    lines.append("# Macrodesign Pédagogique")
    lines.append(f"*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}*")
    lines.append("")
    
    # General information
    lines.append("## 📋 Informations Générales")
    lines.append("")
    
    if 'etape_1_public_cible' in yaml_data:
        pc = yaml_data['etape_1_public_cible']
        if 'public_cible' in pc:
            pc_data = pc['public_cible']
            lines.append("### Public Cible")
            lines.append(f"- **Type:** {pc_data.get('type', 'Non défini')}")
            lines.append(f"- **Profil:** {pc_data.get('profil', 'Non défini')}")
            lines.append(f"- **Niveau d'expertise:** {pc_data.get('niveau_expertise', 'Non défini')}")
            if pc_data.get('besoins_specifiques'):
                lines.append(f"- **Besoins spécifiques:** {pc_data['besoins_specifiques']}")
            lines.append("")
        
        if 'contexte_formation' in pc:
            ctx = pc['contexte_formation']
            lines.append("### Contexte de Formation")
            lines.append(f"- **Titre:** {ctx.get('titre', 'Non défini')}")
            lines.append(f"- **Objectif général:** {ctx.get('objectif_general', 'Non défini')}")
            lines.append("")
    
    if 'etape_2_contraintes' in yaml_data:
        cont = yaml_data['etape_2_contraintes']
        if 'contraintes_formation' in cont:
            cf = cont['contraintes_formation']
            lines.append("### Contraintes de Formation")
            lines.append(f"- **Type de parcours:** {cf.get('type_parcours', 'Non défini')}")
            lines.append(f"- **Temps total:** {cf.get('temps_total', 'Non défini')}")
            lines.append(f"- **Autonomie:** {cf.get('autonomie', 'Non défini')}")
            lines.append(f"- **Animation:** {cf.get('animation', 'Non défini')}")
            lines.append(f"- **Calendrier:** {cf.get('calendrier', 'Non défini')}")
            lines.append(f"- **Horaires:** {cf.get('horaires', 'Non défini')}")
            lines.append(f"- **Nombre de participants:** {cf.get('nombre_participants', 'Non défini')}")
            lines.append("")
    
    if 'etape_3_scenario' in yaml_data:
        scen = yaml_data['etape_3_scenario']
        if 'scenario_cmo' in scen:
            sc = scen['scenario_cmo']
            lines.append("### Scénario Pédagogique")
            lines.append(f"- **Titre:** {sc.get('title', 'Non défini')}")
            lines.append(f"- **Description:** {sc.get('description', 'Non défini')}")
            
            if sc.get('sections'):
                lines.append("- **Structure:**")
                for section in sc['sections']:
                    lines.append(f"  - **Section {section.get('number', '?')}:** {section.get('type', 'Non défini')} - {section.get('content', 'Non défini')} ({section.get('modality', 'Non défini')})")
            lines.append("")
    
    # Competences
    if 'etape_4_competences' in yaml_data:
        comp = yaml_data['etape_4_competences']
        lines.append("## 🎯 Compétences Visées")
        lines.append("")
        
        if 'formulations_competences' in comp:
            competences = comp['formulations_competences']
            for i, competence in enumerate(competences, 1):
                lines.append(f"### Compétence {i}")
                lines.append(f"**Formulation:** {competence}")
                lines.append("")
        
        # Add detailed competence information if available
        for i in range(1, 4):  # Check for competence_1, competence_2, competence_3
            comp_key = f'competence_{i}'
            if comp_key in comp:
                comp_data = comp[comp_key]
                lines.append(f"#### Détails Compétence {i}")
                if comp_data.get('titre'):
                    lines.append(f"**Titre:** {comp_data['titre']}")
                if comp_data.get('idees_cles'):
                    lines.append(f"**Idées clés:** {comp_data['idees_cles']}")
                if comp_data.get('niveau'):
                    lines.append(f"**Niveau:** {comp_data['niveau']}")
                if comp_data.get('verbes'):
                    lines.append(f"**Verbes d'action:** {comp_data['verbes']}")
                lines.append("")
    
    # Referentiels
    if 'referentiels_par_section' in yaml_data:
        refs = yaml_data['referentiels_par_section']
        lines.append("## 📊 Référentiels d'Autoévaluation")
        lines.append("")
        
        for referentiel in refs:
            section_num = referentiel.get('section', 'Non défini')
            lines.append(f"### Section {section_num}")
            lines.append(f"**Compétence évaluée:** {referentiel.get('competence', 'Non défini')}")
            lines.append("")
            lines.append("**Degrés de maîtrise:**")
            
            niveaux = referentiel.get('niveaux', [])
            for niveau in niveaux:
                degre = niveau.get('degre', '')
                libelle = niveau.get('libelle', '')
                badge = niveau.get('badge', 'non')
                badge_text = " (Badge)" if badge == 'oui' else ""
                lines.append(f"{degre}. {libelle}{badge_text}")
                
                # Add observables if available
                if niveau.get('observable_qualitatif'):
                    lines.append(f"   - *Qualitatif:* {niveau['observable_qualitatif']}")
                if niveau.get('observable_quantitatif'):
                    lines.append(f"   - *Quantitatif:* {niveau['observable_quantitatif']}")
                lines.append("")
            
            # Add CUA adaptations if available
            if referentiel.get('adaptations_cua'):
                lines.append("**Adaptations CUA:**")
                for adaptation in referentiel['adaptations_cua']:
                    if isinstance(adaptation, dict):
                        lines.append(f"- **Besoin:** {adaptation.get('besoin', 'Non défini')}")
                        lines.append(f"  **Adaptation:** {adaptation.get('adaptation', 'Non défini')}")
                    else:
                        lines.append(f"- {adaptation}")
                lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("*Document généré automatiquement par l'Assistant IA Magistère*")
    lines.append("*Communauté Magistère Occitanie (CMO)*")
    
    return "\n".join(lines)

@app.route('/download_yaml')
def download_yaml():
    """Download the YAML file for the current session"""
    if 'session_id' not in session:
        return jsonify({'error': 'Aucune session active'}), 400
    
    filename = get_session_filename()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if not os.path.exists(filepath):
        return jsonify({'error': 'Fichier non trouvé'}), 404
    
    # For now, just return the file path
    # In a real implementation, you would use send_file
    return jsonify({
        'success': True,
        'message': f'Fichier disponible : {filename}',
        'filepath': filepath
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 