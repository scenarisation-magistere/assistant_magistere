from flask import request, jsonify, session
from .main import save_yaml_data

def register_public_cible_routes(app):
    """Register public cible routes with the Flask app"""
    
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
