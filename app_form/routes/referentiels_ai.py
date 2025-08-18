import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import yaml

# Load environment variables
load_dotenv()

# Required OpenAI config
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '1000'))
OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))

# Check API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise EnvironmentError("❌ OPENAI_API_KEY is missing from environment variables")

# Create OpenAI client
client = OpenAI(api_key=api_key)


def generate_referentiel_suggestions(section_num, competence, besoins_specifiques):
    """
    Generate evaluation rubric (referentiel) suggestions using OpenAI GPT
    """
    # Prepare CUA adaptations based on specific needs
    adaptations_cua = ""
    if besoins_specifiques:
        adaptations_cua = "\n**Adaptations CUA nécessaires :**\n"
        for besoin in besoins_specifiques:
            adaptations_cua += f"- {besoin}\n"
    
    # Prompt for GPT
    prompt = f"""En tant qu'expert en pédagogie et en évaluation formative, générez un référentiel d'auto-évaluation pour la section {section_num} basé sur la compétence suivante :

**Compétence visée :**
{competence}

**Instructions :**
1. Créez un référentiel avec 4 degrés de progression : "Je débute", "Je progresse", "Je suis autonome", "Je maîtrise avec aisance"
2. Pour chaque degré, proposez :
   - Un indicateur qualitatif (type "Je suis capable de...")
   - Un indicateur quantitatif (score, fréquence, action réalisée)
3. Le badge "oui" est attribué si le degré 3 ("Je suis autonome") est atteint
4. Adaptez les indicateurs au niveau de la compétence et à la progression logique
5. Utilisez des verbes d'action observables et mesurables
6. Assurez-vous que la progression est claire et accessible

**Format de réponse attendu (JSON) :**
{{
    "section": {section_num},
    "competence": "{competence}",
    "niveaux": [
        {{
            "degre": 1,
            "libelle": "Je débute",
            "observable_qualitatif": "Je suis capable de...",
            "observable_quantitatif": "Score/Fréquence/Action",
            "badge": "non"
        }},
        {{
            "degre": 2,
            "libelle": "Je progresse",
            "observable_qualitatif": "Je suis capable de...",
            "observable_quantitatif": "Score/Fréquence/Action",
            "badge": "non"
        }},
        {{
            "degre": 3,
            "libelle": "Je suis autonome",
            "observable_qualitatif": "Je suis capable de...",
            "observable_quantitatif": "Score/Fréquence/Action",
            "badge": "oui"
        }},
        {{
            "degre": 4,
            "libelle": "Je maîtrise avec aisance",
            "observable_qualitatif": "Je suis capable de...",
            "observable_quantitatif": "Score/Fréquence/Action",
            "badge": "non"
        }}
    ],
    "adaptations_cua": [
        {{
            "besoin": "Nom du besoin spécifique",
            "adaptation": "Description de l'adaptation proposée"
        }}
    ]
}}

Répondez uniquement en JSON valide, sans texte supplémentaire."""

    # Call OpenAI API
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Tu es un expert en pédagogie et en évaluation formative spécialisé dans la création de référentiels d'auto-évaluation. Tu réponds toujours en JSON valide."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=OPENAI_MAX_TOKENS,
        temperature=0.7
    )

    # Extract JSON
    content = response.choices[0].message.content.strip()
    try:
        # Remove JSON code block markers if present
        content = content.replace('```json', '').replace('```', '')
        suggestions = json.loads(content)
        return {
            'success': True,
            'referentiel': suggestions,
            'raw_response': content
        }
    except json.JSONDecodeError:
        return {
            'success': False,
            'error': 'Impossible de parser la réponse JSON',
            'raw_response': content
        }


def save_referentiel_to_yaml(referentiel_data, session_data=None):
    """
    Save referentiel data to YAML file
    """
    try:
        # Load current YAML data from session
        if not session_data or 'session_id' not in session_data:
            return {
                'success': False,
                'error': 'Aucune session active'
            }
        
        # Generate filename from session
        session_id = session_data['session_id']
        yaml_file = f"output/formation_{session_id}.yaml"
        
        if not os.path.exists(yaml_file):
            return {
                'success': False,
                'error': 'Aucun fichier YAML trouvé'
            }
        
        with open(yaml_file, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
        
        # Initialize etape_5_referentiels if not exists
        if 'etape_5_referentiels' not in yaml_data:
            yaml_data['etape_5_referentiels'] = {}
        
        # Add or update referentiel directly under etape_5_referentiels
        section_num = referentiel_data.get('section')
        yaml_data['etape_5_referentiels'][f'section_{section_num}'] = referentiel_data
        
        # Save back to file
        with open(yaml_file, 'w', encoding='utf-8') as file:
            yaml.dump(yaml_data, file, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        return {
            'success': True,
            'message': f'Référentiel pour la section {section_num} sauvegardé avec succès'
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Erreur lors de la sauvegarde : {str(e)}'
        }


def update_referentiel_with_feedback(section_num, modifications, session_data=None):
    """
    Update referentiel based on user feedback
    """
    try:
        # Load current YAML data from session
        if not session_data or 'session_id' not in session_data:
            return {
                'success': False,
                'error': 'Aucune session active'
            }
        
        # Generate filename from session
        session_id = session_data['session_id']
        yaml_file = f"output/formation_{session_id}.yaml"
        
        if not os.path.exists(yaml_file):
            return {
                'success': False,
                'error': 'Aucun fichier YAML trouvé'
            }
        
        with open(yaml_file, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
        
        # Find existing referentiel
        referentiel = yaml_data.get('etape_5_referentiels', {}).get(f'section_{section_num}')
        
        if not referentiel:
            return {
                'success': False,
                'error': f'Référentiel pour la section {section_num} non trouvé'
            }
        
        # Apply modifications
        for modification in modifications:
            niveau = modification.get('niveau')
            field = modification.get('field')
            value = modification.get('value')
            
            if niveau and field and value is not None:
                for niveau_data in referentiel.get('niveaux', []):
                    if niveau_data.get('degre') == niveau:
                        niveau_data[field] = value
                        break
        
        # Save updated data
        with open(yaml_file, 'w', encoding='utf-8') as file:
            yaml.dump(yaml_data, file, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        return {
            'success': True,
            'referentiel': referentiel,
            'message': f'Référentiel pour la section {section_num} mis à jour avec succès'
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Erreur lors de la mise à jour : {str(e)}'
        }
