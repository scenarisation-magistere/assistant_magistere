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
    """Placeholder for the next step - Contenus par section"""
    return render_template('contenus.html', step=5, total_steps=5)

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