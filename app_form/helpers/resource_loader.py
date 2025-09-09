import os
import json

def load_questions_from_json(filename: str):
    try:
        with open(os.path.join('ressources', filename), 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

def load_verbs_taxonomy():
    try:
        with open('./ressources/verbs_taxonomy.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('verbs_taxonomy', {})
    except Exception as e:
        print(f"Error loading verbs taxonomy: {str(e)}")
        return {}

def load_rag_resources():
    """Return the raw text of the RAG resource table JSON file"""
    try:
        rag_file_path = os.path.join('ressources', 'Tableau_Activites_Ressources.json')
        if os.path.exists(rag_file_path):
            with open(rag_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            print(f"RAG file not found: {rag_file_path}")
            return ""
    except Exception as e:
        print(f"Error loading RAG resources: {e}")
        return ""


