from flask import request, jsonify, session, render_template, redirect
from helpers.session_yaml import save_yaml_data
from config.pages_config import get_navigation_info, get_page_config
from helpers.resource_loader import load_questions_from_json

def register_public_cible_routes(app):
    """Register public cible routes with the Flask app"""
    
    @app.route('/public-cible', methods=['GET', 'POST'])
    def public_cible():
        if request.method == 'POST':
            # Handle form submission
            data = {}
            for key in request.form.keys():
                values = request.form.getlist(key)
                if len(values) > 1:
                    data[key] = values
                else:
                    data[key] = values[0] if values else ''
            # Attach merged info for type_de_formation for convenience
            if data.get('type_de_formation_text'):
                data['type_de_formation_precisions'] = data.get('type_de_formation_text')
            save_yaml_data(data, 'etape_1_public_cible')
            return redirect('/contraintes')
        
        nav_info = get_navigation_info('public_cible')
        page_config = get_page_config('public_cible')
        questions_public_cible = load_questions_from_json('public_cible.json')
        return render_template('public_cible.html', 
                             questions=questions_public_cible, 
                             nav_info=nav_info,
                             header_gradient=page_config.get('header_gradient', 'var(--gradient-primary)'),
                             header_title='🧭 Titre, objectif et public cible',
                             header_description='Déterminez le titre, l’objectif général et les caractéristiques du public cible de votre formation')

    @app.route('/submit_public_cible', methods=['POST'])
    def submit_public_cible():
        data = request.get_json()
        
        # Store in session for later use
        session['public_cible_data'] = data
        
        # Pass lists as-is from client
        type_de_public_list = data.get('type_de_public', [])
        niveaux_scolaires_list = data.get('niveaux_scolaires', [])
        niveau_expertise_list = data.get('niveau_expertise', [])
        besoins_specifiques_raw = data.get('besoins_specifiques', [])

        # Replace target option with only the free-text value if provided
        def replace_with_free_text(options_list, text_value, target_option_label):
            text_value = (text_value or '').strip()
            if not text_value:
                return options_list
            filtered = [opt for opt in options_list if opt != target_option_label]
            filtered.append(text_value)
            return filtered

        # Apply for type_de_public (Autre)
        type_de_public_list = replace_with_free_text(
            type_de_public_list,
            data.get('type_de_public_text'),
            'Autre (à préciser)'
        )

        # Replace 'Autre (à préciser)' for besoins_specifiques with free text (supports radio or checkbox)
        bs_text = (data.get('besoins_specifiques_text') or '').strip()
        if bs_text:
            if isinstance(besoins_specifiques_raw, list):
                tmp = []
                replaced = False
                for v in besoins_specifiques_raw:
                    if v == 'Autre (à préciser)' and not replaced:
                        tmp.append(bs_text)
                        replaced = True
                    else:
                        tmp.append(v)
                besoins_specifiques_value = tmp
            elif isinstance(besoins_specifiques_raw, str):
                besoins_specifiques_value = bs_text if besoins_specifiques_raw == 'Autre (à préciser)' else besoins_specifiques_raw
            else:
                besoins_specifiques_value = besoins_specifiques_raw
        else:
            besoins_specifiques_value = besoins_specifiques_raw

        # Generate YAML data for this step aligned with questions (flat structure)
        yaml_data = {
            'titre_formation': data.get('titre_formation', ''),
            'objectif_general': data.get('objectif_general', ''),
            'type_de_public': type_de_public_list,
            'type_de_formation': data.get('type_de_formation', ''),
            'type_de_formation_precisions': data.get('type_de_formation_text', ''),
            'niveaux_scolaires': niveaux_scolaires_list,
            'niveau_expertise': niveau_expertise_list,
            'besoins_specifiques': besoins_specifiques_value
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
