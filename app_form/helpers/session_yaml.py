import os
from datetime import datetime
import yaml
from flask import session

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
        except Exception:
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
    except Exception:
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
    except Exception:
        return False, "Erreur lors du chargement des données"
    
    for step in required_steps:
        if step not in yaml_data:
            return False, f"Étape {step} non complétée"
    
    return True, "OK"


