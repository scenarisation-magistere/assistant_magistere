from flask import render_template, request, jsonify, session
import yaml
import os
from datetime import datetime
from ai_helpers import generate_referentiel_suggestions, save_referentiel_to_yaml, update_referentiel_with_feedback

def referentiels_page():
    """
    Handle the referentiels (evaluation rubrics) page
    """
    # Load YAML data from session
    if 'session_id' not in session:
        return render_template('error.html', message="Aucune session active. Veuillez d'abord compléter les étapes précédentes.")
    
    # Generate filename from session
    session_id = session['session_id']
    yaml_file = f"output/formation_{session_id}.yaml"
    
    if not os.path.exists(yaml_file):
        return render_template('error.html', message="Aucun fichier YAML trouvé. Veuillez d'abord compléter les étapes précédentes.")
    
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
    except Exception as e:
        return render_template('error.html', message=f"Erreur lors du chargement du fichier YAML: {str(e)}")
    
    # Extract required data
    competences_data = yaml_data.get('etape_4_competences', {})
    evaluation_data = yaml_data.get('evaluation_competences', {})
    
    # Try to get formulations from different possible locations
    formulations = competences_data.get('formulations_competences', [])
    ordre_competences = evaluation_data.get('ordre_competences', [])
    
    # If no formulations but we have ordre_competences, extract from there
    if not formulations and ordre_competences:
        formulations = [comp.get('formulation', '') for comp in ordre_competences if comp.get('formulation')]
    
    public_cible = yaml_data.get('etape_1_public_cible', {})
    besoins_specifiques = public_cible.get('public_cible', {}).get('besoins_specifiques', [])
    
    # Debug: Print the data structure
    print(f"Competences data: {competences_data}")
    print(f"Formulations: {formulations}")
    print(f"Formulations type: {type(formulations)}")
    print(f"Formulations length: {len(formulations) if formulations else 0}")
    
    # Prepare sections data (S2 to S5)
    sections = []
    
    # If no formulations, try to extract from individual competences
    if not formulations:
        print("No formulations found, trying to extract from individual competences...")
        for i in range(1, 10):  # Check up to 10 competences
            competence_key = f'competence_{i}'
            if competence_key in competences_data:
                formulation = competences_data[competence_key].get('formulation', '')
                titre = competences_data[competence_key].get('titre', '')
                if formulation:
                    sections.append({
                        'numero': i,  # Start from section 1
                        'competence': formulation,
                        'code': f'C{i}',
                        'title': titre if titre else extract_title(formulation)
                    })
                    print(f"Found competence {i}: {titre if titre else formulation[:50]}...")
    
    # If still no sections, create default sections
    if not sections:
        print("No competences found, creating default sections...")
        sections = [
            {
                'numero': 1,
                'competence': 'Compétence 1 - À définir',
                'code': 'C1',
                'title': 'Compétence 1'
            },
            {
                'numero': 2,
                'competence': 'Compétence 2 - À définir',
                'code': 'C2',
                'title': 'Compétence 2'
            },
            {
                'numero': 3,
                'competence': 'Compétence 3 - À définir',
                'code': 'C3',
                'title': 'Compétence 3'
            }
        ]
    
    def extract_title(competence_text):
        """Extract a meaningful title from competence description"""
        # Remove common prefixes
        prefixes_to_remove = [
            "Être capable de ",
            "Être capable d'",
            "Savoir ",
            "Pouvoir ",
            "Maîtriser ",
            "Connaître "
        ]
        
        title = competence_text
        for prefix in prefixes_to_remove:
            if title.startswith(prefix):
                title = title[len(prefix):]
                break
        
        # Capitalize first letter
        if title:
            title = title[0].upper() + title[1:]
        
        # Truncate if too long
        if len(title) > 40:
            title = title[:40] + "..."
            
        return title

    # If we have formulations, use them
    if formulations:
        sections = []
        for i, formulation in enumerate(formulations, 1):  # Start from section 1
            # Try to get the titre from the competence data
            competence_key = f'competence_{i}'
            titre = ''
            if competence_key in competences_data:
                titre = competences_data[competence_key].get('titre', '')
            
            sections.append({
                'numero': i,
                'competence': formulation,
                'code': f'C{i}',
                'title': titre if titre else extract_title(formulation)
            })
    # If we have ordre_competences but no formulations, use ordre_competences directly
    elif ordre_competences:
        sections = []
        for i, comp in enumerate(ordre_competences, 1):  # Start from section 1
            competence_text = comp.get('formulation', f'Compétence {i}')
            
            # Try to get the titre from the competence data
            competence_key = f'competence_{i}'
            titre = ''
            if competence_key in competences_data:
                titre = competences_data[competence_key].get('titre', '')
            
            sections.append({
                'numero': i,
                'competence': competence_text,
                'code': comp.get('code', f'C{i}'),
                'title': titre if titre else extract_title(competence_text)
            })
    
    print(f"Final sections: {sections}")
    
    # Check for existing referentiels
    existing_referentiels = yaml_data.get('referentiels_par_section', [])
    print(f"Existing referentiels: {existing_referentiels}")
    
    return render_template('referentiels.html', 
                         sections=sections,
                         besoins_specifiques=besoins_specifiques,
                         yaml_data=yaml_data,
                         existing_referentiels=existing_referentiels)

def generate_referentiel():
    """
    Generate a referentiel for a specific section using AI
    """
    data = request.get_json()
    section_num = data.get('section_num')
    competence = data.get('competence')
    besoins_specifiques = data.get('besoins_specifiques', [])
    
    # Generate referentiel using AI
    result = generate_referentiel_suggestions(section_num, competence, besoins_specifiques)
    
    return jsonify(result)

def save_referentiel():
    """
    Save the referentiel to YAML
    """
    data = request.get_json()
    referentiel_data = data.get('referentiel')
    
    # Save to YAML
    result = save_referentiel_to_yaml(referentiel_data, session)
    
    return jsonify(result)

def update_referentiel():
    """
    Update an existing referentiel based on user feedback
    """
    data = request.get_json()
    section_num = data.get('section_num')
    modifications = data.get('modifications')
    
    # Update referentiel using AI
    result = update_referentiel_with_feedback(section_num, modifications, session)
    
    return jsonify(result) 