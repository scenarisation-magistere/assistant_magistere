from flask import request, jsonify, session, render_template, redirect
from .main import save_yaml_data, check_migration_warning
from questions.contraintes import QUESTIONS_CONTRAINTES
from config.pages_config import get_navigation_info, get_page_config

def register_contraintes_routes(app):
    """Register contraintes routes with the Flask app"""
    
    @app.route('/contraintes', methods=['GET', 'POST'])
    def contraintes():
        if request.method == 'POST':
            # Handle form submission (ensure free-text clarifications saved without labels)
            form = request.form
            nombre_participants = form.get('nombre_participants', '')
            animation = form.get('animation', '')
            exigences_value = form.get('exigences_institutionnelles', '')
            exigences_text = (form.get('exigences_institutionnelles_text', '') or '').strip()
            restrictions_value = form.get('restrictions_techniques', '')
            restrictions_text = (form.get('restrictions_techniques_text', '') or '').strip()

            # Prefer free-text when provided; else if selected is a label requiring text but none given, store empty
            if exigences_text:
                exigences_value = exigences_text
            elif exigences_value == 'Exigence institutionnelle particulière':
                exigences_value = ''
            if restrictions_text:
                restrictions_value = restrictions_text
            elif restrictions_value == 'Restriction technique':
                restrictions_value = ''

            data = {
                'nombre_participants': nombre_participants,
                'animation': animation,
                'exigences_institutionnelles': exigences_value,
                'restrictions_techniques': restrictions_value
            }

            filename = save_yaml_data(data, 'etape_2_contraintes')
            return redirect('/competences')
        
        nav_info = get_navigation_info('contraintes')
        page_config = get_page_config('contraintes')
        return render_template('contraintes.html', 
                             questions=QUESTIONS_CONTRAINTES, 
                             nav_info=nav_info,
                             header_gradient=page_config.get('header_gradient', 'var(--gradient-danger)'),
                             header_title='⚙️ Contraintes Formation',
                             header_description='Précisez les contraintes temporelles, organisationnelles et techniques')

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
        
        # Prefer saving only the free-text clarification when present (client may have merged "Option : text")
        def extract_free_text(merged_value: str) -> str:
            if not merged_value:
                return ''
            parts = merged_value.split(' : ', 1)
            if len(parts) == 2 and parts[1].strip():
                return parts[1].strip()
            return merged_value.strip()

        exigences_raw = (data.get('exigences_institutionnelles') or '').strip()
        restrictions_raw = (data.get('restrictions_techniques') or '').strip()
        exigences_text = (data.get('exigences_institutionnelles_text') or '').strip()
        restrictions_text = (data.get('restrictions_techniques_text') or '').strip()

        # Prefer explicit *_text fields when provided; otherwise extract from merged value if any
        exigences_value = exigences_text if exigences_text else extract_free_text(exigences_raw)
        restrictions_value = restrictions_text if restrictions_text else extract_free_text(restrictions_raw)

        # If the selected option is the "requires text" label but no text was provided, store empty
        if exigences_value == 'Exigence institutionnelle particulière' or (
            exigences_raw == 'Exigence institutionnelle particulière' and exigences_value == exigences_raw
        ):
            exigences_value = ''
        if restrictions_value == 'Restriction technique' or (
            restrictions_raw == 'Restriction technique' and restrictions_value == restrictions_raw
        ):
            restrictions_value = ''

        # Generate YAML data for this step - flat structure aligned with questions
        yaml_data = {
            'nombre_participants': data.get('nombre_participants', ''),
            'animation': data.get('animation', ''),
            'exigences_institutionnelles': exigences_value,
            'restrictions_techniques': restrictions_value
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
