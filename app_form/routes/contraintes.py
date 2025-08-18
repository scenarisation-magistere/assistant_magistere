from flask import request, jsonify, session
from .main import save_yaml_data, check_migration_warning

def register_contraintes_routes(app):
    """Register contraintes routes with the Flask app"""
    
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
