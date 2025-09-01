from flask import render_template, request, jsonify, session
import yaml
import os
from questions.competences import (
    COMPETENCES_QUESTIONS, 
    get_competences_with_count, 
    get_next_competence_number, 
    reorder_competences, 
    generate_competence_template
)
from .competences_ai import (
    generate_competency_suggestions, 
    evaluate_and_order_competences,
    add_suggested_competence
)
from .main import check_previous_steps_completed, save_yaml_data, get_session_filename
from config.pages_config import get_navigation_info, get_page_config

def register_competences_routes(app):
    """Register competences routes with the Flask app"""
    
    @app.route('/competences')
    def competences():
        # Check if previous steps are completed
        completed, message = check_previous_steps_completed(['etape_1_public_cible', 'etape_2_contraintes'])
        if not completed:
            return render_template('error.html', message=f"Veuillez d'abord compléter les étapes précédentes. {message}")
        
        # Load previous data from YAML file
        public_cible_data = None
        contraintes_data = None
        if 'session_id' in session:
            filename = get_session_filename()
            filepath = os.path.join('output', filename)
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        yaml_data = yaml.safe_load(f) or {}
                        public_cible_data = yaml_data.get('etape_1_public_cible', {})
                        contraintes_data = yaml_data.get('etape_2_contraintes', {})
                except:
                    pass
        
        # Get competence count from session or default to 0 (start with no competences)
        competence_count = session.get('competence_count', 0)
        competences = get_competences_with_count(competence_count)
        
        nav_info = get_navigation_info('competences')
        page_config = get_page_config('competences')
        return render_template('competences.html', 
                             competences=competences,
                             public_cible_data=public_cible_data,
                             contraintes_data=contraintes_data,
                             nav_info=nav_info,
                             header_gradient=page_config.get('header_gradient', 'var(--gradient-success)'),
                             header_title='🎯 Compétences Visées',
                             header_description='Formulation des compétences visées pour le scénario CMO')

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

    # Legacy endpoint /get_verb_suggestions removed. Use /get_bloom_verbs instead.

    @app.route('/get_bloom_verbs/<path:niveau>')
    def get_bloom_verbs(niveau):
        """Get Bloom taxonomy verbs for a specific level"""
        try:
            # Debug: print the received niveau parameter
            print(f"DEBUG: Received niveau parameter: '{niveau}'")
            print(f"DEBUG: Type of niveau: {type(niveau)}")
            
            # URL decode the niveau parameter if needed
            from urllib.parse import unquote
            decoded_niveau = unquote(niveau)
            print(f"DEBUG: Decoded niveau: '{decoded_niveau}'")
            
            # Use the decoded niveau
            niveau = decoded_niveau
            # Map niveau to bloom taxonomy keys
            niveau_mapping = {
                # Sélections combinées (cognitif + quelques affectifs pertinents)
                'Haut : Créer / Évaluer / Analyser': ['creer', 'evaluer', 'analyser', 'caracteriser', 'organiser'],
                'Moyen : Appliquer / Comprendre': ['appliquer', 'comprendre', 'valoriser', 'repondre'],
                'Bas : Se rappeler': ['se_rappeler', 'recevoir']
            }
            
            print(f"DEBUG: Available niveaux: {list(niveau_mapping.keys())}")
            print(f"DEBUG: Looking for niveau: '{niveau}'")
            
            bloom_taxonomy = COMPETENCES_QUESTIONS.get('bloom_taxonomy', {})
            selected_levels = niveau_mapping.get(niveau, [])
            
            print(f"DEBUG: Selected levels: {selected_levels}")
            
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
            # Read optional context from the request (selected/workshop competences)
            client_payload = request.get_json(silent=True) or {}
            # Load formation data from YAML file
            if 'session_id' not in session:
                return jsonify({
                    'success': False,
                    'error': 'Aucune session active. Veuillez recommencer le questionnaire.'
                })
            
            filename = get_session_filename()
            filepath = os.path.join('output', filename)
            
            if not os.path.exists(filepath):
                return jsonify({
                    'success': False,
                    'error': 'Fichier de données non trouvé. Veuillez recommencer le questionnaire.'
                })
            
            # Load complete YAML data
            with open(filepath, 'r', encoding='utf-8') as f:
                yaml_data = yaml.safe_load(f) or {}
            
            # Merge client context into YAML data so the prompt can avoid duplicates
            if client_payload:
                yaml_data['selected_competences'] = client_payload.get('selected_competences', [])
                yaml_data['workshop_competences'] = client_payload.get('workshop_competences', [])

            # Pass the enriched data to the AI function
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

    @app.route('/submit_competences', methods=['POST'])
    def submit_competences():
        data = request.get_json()
        
        # Load existing data from YAML file
        existing_data = {}
        if 'session_id' in session:
            filename = get_session_filename()
            filepath = os.path.join('output', filename)
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
        
        # Preserve existing evaluation_competences data if it exists
        existing_competences = existing_data.get('etape_4_competences', {})
        if 'evaluation_competences' in existing_competences:
            competences_data['evaluation_competences'] = existing_competences['evaluation_competences']
        
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
                filepath = os.path.join('output', filename)
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
                # Load current YAML data to update etape_4_competences
                if 'session_id' in session:
                    filename = get_session_filename()
                    filepath = os.path.join('output', filename)
                    if os.path.exists(filepath):
                        with open(filepath, 'r', encoding='utf-8') as f:
                            yaml_data = yaml.safe_load(f) or {}
                        
                        # Add evaluation_competences as a subsection within etape_4_competences
                        if 'etape_4_competences' not in yaml_data:
                            yaml_data['etape_4_competences'] = {}
                        
                        yaml_data['etape_4_competences']['evaluation_competences'] = result['evaluation']
                        
                        # Save the updated data
                        with open(filepath, 'w', encoding='utf-8') as f:
                            yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
                        
                        filename = get_session_filename()
                
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
                filepath = os.path.join('output', filename)
                if os.path.exists(filepath):
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            yaml_data = yaml.safe_load(f) or {}
                    except:
                        yaml_data = {}
            
            # Get the suggested competence from evaluation data (now within etape_4_competences)
            competences_data = yaml_data.get('etape_4_competences', {})
            evaluation_data = competences_data.get('evaluation_competences', {})
            suggested_competence = evaluation_data.get('competence_complementaire', {})
            
            if not suggested_competence:
                return jsonify({
                    'success': False,
                    'error': 'Aucune compétence suggérée trouvée'
                })
            
            # Add the suggested competence using the AI helper function
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
