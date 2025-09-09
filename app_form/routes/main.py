from flask import render_template, session, redirect, url_for, request, jsonify
import yaml
import os
from datetime import datetime

 

# Import navigation config
from config.pages_config import get_navigation_info, get_page_by_step, PAGES_CONFIG, get_page_config
from helpers.session_yaml import get_session_filename, save_yaml_data, check_previous_steps_completed

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

def register_main_routes(app):
    """Register main routes with the Flask app"""
    
    # Add context processor for navigation helpers
    @app.context_processor
    def inject_navigation_helpers():
        def get_page_name_by_step(step):
            page_name = get_page_by_step(step)
            if page_name:
                return PAGES_CONFIG[page_name]['name']
            return f'Étape {step}'
        
        return dict(get_page_name_by_step=get_page_name_by_step)
    
    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/presentation')
    def presentation():
        return render_template('presentation.html')

    @app.route('/start-journey')
    def start_journey():
        return redirect('/public-cible')

    

    @app.route('/load-journey')
    def load_journey():
        return render_template('load_journey.html')

    @app.route('/app-status')
    def app_status():
        """Display app startup timestamp and status"""
        startup_time = app.config.get('STARTUP_TIMESTAMP', 'Unknown')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template('app_status.html', 
                             startup_time=startup_time,
                             current_time=current_time)

    




