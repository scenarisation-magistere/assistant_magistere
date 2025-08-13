import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import yaml # Added for YAML parsing

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


def generate_competency_suggestions(formation_data):
    """
    Generate competency suggestions using OpenAI GPT based on formation data.
    """
    # Extract relevant information from the correct YAML structure
    # formation_data should be the complete YAML data, not just a subset
    public_cible_data = formation_data.get('etape_1_public_cible', {})
    contraintes_data = formation_data.get('etape_2_contraintes', {})
    
    # Extract from public_cible structure
    public_cible = public_cible_data.get('public_cible', {})
    contexte_formation = public_cible_data.get('contexte_formation', {})
    
    titre = contexte_formation.get('titre', '')
    objectif = contexte_formation.get('objectif_general', '')
    type_public = public_cible.get('type', '')
    niveau = public_cible.get('niveau_expertise', '')
    profil = public_cible.get('profil', '')
    besoins = public_cible.get('besoins_specifiques', [])

    # Prompt for GPT
    prompt = f"""
En tant qu'expert en formation et en pédagogie, générez 6 compétences visées pour une formation Magistère basée sur les informations suivantes :

**Contexte de la formation :**
- Titre : {titre}
- Objectif général : {objectif}

**Public cible :**
- Type de public : {type_public}
- Niveau d'expertise : {niveau}
- Profil du groupe : {profil}
- Besoins spécifiques : {', '.join(besoins) if isinstance(besoins, list) else besoins}

**Instructions :**
1. Générez exactement 6 compétences visées
2. Chaque compétence doit suivre la taxonomie de Bloom révisée
3. Utilisez des verbes d'action observables et mesurables
4. Adaptez le niveau aux caractéristiques du public cible
5. Assurez-vous que les compétences sont cohérentes avec l'objectif de formation
6. Les compétences doivent être cohérentes avec le profil du groupe cible
7. Les competences sont retournées classées par niveau de compétence (de bas à haut)

**Format de réponse attendu (JSON) :**
{{
    "competences": [
        {{
            "titre": "Titre court et descriptif de la compétence",
            "idees_cles": "mots-clés et concepts principaux",
            "niveau": "Haut/Moyen/Bas",
            "verbes_suggere": ["verbe1", "verbe2", "verbe3"],
            "formulation": "Formulation complète de la compétence"
        }},
        ...
    ]
}}

Répondez uniquement en JSON valide, sans texte supplémentaire.
"""

    # Call OpenAI API
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Tu es un expert en formation et en pédagogie spécialisé dans la formulation de compétences visées pour les formations Magistère. Tu réponds toujours en JSON valide."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=OPENAI_MAX_TOKENS,
        temperature=OPENAI_TEMPERATURE
    )

    # Extract JSON
    content = response.choices[0].message.content.strip()
    try:
        # Remove JSON code block markers if present
        content = content.replace('```json', '').replace('```', '')
        suggestions = json.loads(content)
        return {
            'success': True,
            'suggestions': suggestions.get('competences', []),
            'raw_response': content
        }
    except json.JSONDecodeError:
        return {
            'success': False,
            'error': 'Impossible de parser la réponse JSON',
            'raw_response': content
        }

def generate_verb_suggestions_for_level(niveau):
    """
    Generate verb suggestions for a specific cognitive level
    """
    verb_suggestions = {
        'Haut': [
            'créer', 'concevoir', 'structurer', 'synthétiser', 'planifier', 
            'juger', 'justifier', 'analyser', 'comparer', 'différencier',
            'évaluer', 'développer', 'organiser', 'construire', 'produire'
        ],
        'Moyen': [
            'appliquer', 'utiliser', 'démontrer', 'résoudre', 'expliquer',
            'illustrer', 'interpréter', 'reformuler', 'classifier', 'exemplifier',
            'exécuter', 'implémenter', 'calculer', 'prédire', 'modéliser'
        ],
        'Bas': [
            'définir', 'nommer', 'décrire', 'identifier', 'rappeler',
            'lister', 'reconnaître', 'énumérer', 'reproduire', 'citer',
            'mémoriser', 'localiser', 'sélectionner', 'reconnaître', 'reproduire'
        ]
    }
    
    return verb_suggestions.get(niveau, [])

def evaluate_and_order_competences(yaml_data):
    """
    Evaluate and order competences using GPT-4 based on pedagogical coherence
    """
    try:
        # Extract competences data from the correct structure
        competences_data = yaml_data.get('etape_4_competences', {})
        formulations = competences_data.get('formulations_competences', [])
        
        # Extract other context data from the correct structure
        public_cible_data = yaml_data.get('etape_1_public_cible', {})
        contraintes_data = yaml_data.get('etape_2_contraintes', {})
        
        # Build competences details from the saved structure
        competences_details = []
        for i in range(1, len(formulations) + 1):
            competence_key = f'competence_{i}'
            if competence_key in competences_data:
                competences_details.append({
                    'code': f'C{i}',
                    'idees_cles': competences_data[competence_key].get('idees_cles', ''),
                    'niveau': competences_data[competence_key].get('niveau', ''),
                    'verbes': competences_data[competence_key].get('verbes', ''),
                    'formulation': competences_data[competence_key].get('formulation', '')
                })
        
        # Check if we have competences to evaluate
        if not competences_details:
            return {
                'success': False,
                'error': 'Aucune compétence trouvée dans les données YAML',
                'fallback': {
                    'ordre_competences': [],
                    'avis_global': 'Aucune compétence à évaluer - données manquantes',
                    'points_amelioration': ['Vérifier que les compétences ont été correctement sauvegardées']
                }
            }
        
        # Prepare competences data for the prompt
        competences_yaml = ""
        for comp in competences_details:
            competences_yaml += f"""  {comp['code']}:
    idees_cles: {comp['idees_cles']}
    niveau: {comp['niveau']}
    verbes: {comp['verbes']}
    formulation: {comp['formulation']}
"""
        
        # Extract context data from the correct structure
        public_cible = public_cible_data.get('public_cible', {})
        contexte_formation = public_cible_data.get('contexte_formation', {})
        
        # Prepare the prompt
        prompt = f"""En tant qu'expert en pédagogie et en conception de formation, évaluez et ordonnez les compétences suivantes selon les principes de l'alignement pédagogique de Biggs et de la progressivité cognitive.

**Instructions :**
1. Évaluez chaque compétence pour sa pertinence par rapport au public cible et aux objectifs
2. Vérifiez la cohérence du niveau (bas, moyen, haut) avec la logique de progression pédagogique
3. Identifiez les redondances, manques ou formulations floues
4. Classez les compétences selon l'alignement pédagogique de Biggs (objectifs → activités → évaluations)
5. Assurez la progressivité implicite (du plus simple au plus complexe)
6. IMPORTANT : Utilisez les codes existants (C1, C2, C3, etc.) et réordonnez-les selon la logique pédagogique
7. ATTENTION PROGRESSION : Vérifiez que la difficulté croît progressivement. Si vous identifiez des gaps (sauts de difficulté, manque de point d'entrée, ou niveau élevé manquant), suggérez des compétences appropriées
8. **OBLIGATOIRE** : Si vous identifiez un gap, proposez UNE compétence complémentaire spécifique et prête à être ajoutée

**Données de contexte :**
- Public cible : {public_cible.get('type', 'Non spécifié')}
- Niveau d'expertise : {public_cible.get('niveau_expertise', 'Non spécifié')}
- Titre formation : {contexte_formation.get('titre', 'Non spécifié')}
- Objectif général : {contexte_formation.get('objectif_general', 'Non spécifié')}

**Compétences à évaluer et ordonner :**
```yaml
{competences_yaml}
```

**Format de réponse attendu (YAML) :**
Vous devez réordonner les compétences existantes en utilisant leurs codes actuels (C1, C2, C3, etc.) selon la logique pédagogique. Par exemple, si C3 est plus simple que C1, mettez C3 en premier.

```yaml
ordre_competences:
  - code: C3
    formulation: "[formulation exacte de la compétence C3]"
    justification: "[pourquoi C3 doit être en première position]"
    pertinence: "élevée/moyenne/faible"
  - code: C1
    formulation: "[formulation exacte de la compétence C1]"
    justification: "[pourquoi C1 doit être en deuxième position]"
    pertinence: "élevée/moyenne/faible"
  - code: C2
    formulation: "[formulation exacte de la compétence C2]"
    justification: "[pourquoi C2 doit être en troisième position]"
    pertinence: "élevée/moyenne/faible"
avis_global: |
  [Analyse synthétique sur la cohérence pédagogique globale et l'alignement avec Biggs]
points_amelioration:
  - "[Amélioration 1]"
  - "[Amélioration 2]"
  - "[Si gap détecté] Suggestion d'ajouter une compétence pour [type de gap : passerelle/point d'entrée/niveau élevé]"
competence_complementaire:
  titre: "[Titre de la compétence complémentaire suggérée]"
  niveau: "[niveau de la compétence]"
  idees_cles: "[idées clés pour cette compétence]"
  verbes: "[verbes d'action appropriés]"
  formulation: "[formulation complète de la compétence]"
  justification: "[pourquoi cette compétence est nécessaire : passerelle entre compétences, point d'entrée manquant, niveau élevé requis, etc.]"
  position_suggeree: "[position recommandée dans la séquence : début/milieu/fin]"
```

**Règles importantes :**
- Utilisez TOUS les codes existants (C1, C2, C3, etc.)
- Réordonnez-les selon la logique pédagogique
- Gardez les formulations exactes des compétences
- Justifiez chaque position dans l'ordre
- **Vérifiez la progression de difficulté** : bas → moyen → haut
- **Si gap détecté** : suggérez UNE compétence complémentaire dans `competence_complementaire` selon le type de gap :
  - **Passerelle** : pour combler un saut entre deux compétences
  - **Point d'entrée** : pour faciliter l'accès aux premières compétences
  - **Niveau élevé** : pour compléter la progression vers des compétences avancées
- **IMPORTANT** : Proposez toujours une compétence complémentaire prête à être ajoutée, même si elle n'est pas strictement nécessaire
- **Niveaux de difficulté** :
  - Bas : identifier, reconnaître, décrire, définir
  - Moyen : appliquer, utiliser, créer, analyser
  - Haut : évaluer, synthétiser, concevoir, innover

Répondez uniquement en YAML valide, sans texte supplémentaire."""

        # Call OpenAI API
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "Vous êtes un expert en pédagogie et en conception de formation. Votre rôle est d'évaluer et d'ordonner les compétences selon les principes de l'alignement pédagogique de Biggs et de la progressivité cognitive. Répondez toujours en YAML valide."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        
        # Extract the response
        evaluation_text = response.choices[0].message.content.strip()
        print(f"=== AI Response ===\n{evaluation_text}")
        
        # Try to parse YAML from the response
        try:
            # Extract YAML part from the response
            yaml_start = evaluation_text.find('```yaml')
            yaml_end = evaluation_text.find('```', yaml_start + 7)
            
            if yaml_start != -1 and yaml_end != -1:
                yaml_content = evaluation_text[yaml_start + 7:yaml_end].strip()
                evaluation_data = yaml.safe_load(yaml_content)
            else:
                # Fallback: try to parse the entire response as YAML
                evaluation_data = yaml.safe_load(evaluation_text)
                
            # Validate the structure
            if not evaluation_data:
                raise yaml.YAMLError("Empty YAML data")
                
            # Ensure required fields exist
            if 'ordre_competences' not in evaluation_data:
                evaluation_data['ordre_competences'] = []
            if 'avis_global' not in evaluation_data:
                evaluation_data['avis_global'] = 'Avis global non disponible'
            if 'points_amelioration' not in evaluation_data:
                evaluation_data['points_amelioration'] = ['Points d\'amélioration non disponibles']
                
        except yaml.YAMLError as e:
            print(f"YAML parsing error: {e}")
            # If YAML parsing fails, create a structured response
            evaluation_data = {
                'ordre_competences': [],
                'avis_global': f"Erreur de parsing YAML: {e}\n\nRéponse brute: {evaluation_text}",
                'points_amelioration': ['Erreur de parsing YAML - voir avis global']
            }
        
        return {
            'success': True,
            'evaluation': evaluation_data,
            'raw_response': evaluation_text
        }
        
    except Exception as e:
        print(f"Exception in evaluate_and_order_competences: {e}")
        import traceback
        traceback.print_exc()
        return {
            'success': False,
            'error': str(e),
            'fallback': {
                'ordre_competences': [],
                'avis_global': f"Erreur lors de l'évaluation : {str(e)}",
                'points_amelioration': ['Erreur technique - évaluation impossible']
            }
        }

def add_suggested_competence(yaml_data, suggested_competence):
    """
    Add a suggested competence to the YAML data
    """
    try:
        # Get current competences data
        competences_data = yaml_data.get('etape_4_competences', {})
        formulations = competences_data.get('formulations_competences', [])
        
        # Determine the new competence number
        new_competence_num = len(formulations) + 1
        new_competence_key = f'competence_{new_competence_num}'
        
        # Add the new competence to formulations
        formulations.append(suggested_competence['formulation'])
        competences_data['formulations_competences'] = formulations
        
        # Add the detailed competence data
        competences_data[new_competence_key] = {
            'titre': suggested_competence.get('titre', ''),
            'idees_cles': suggested_competence.get('idees_cles', ''),
            'niveau': suggested_competence.get('niveau', ''),
            'verbes': suggested_competence.get('verbes', ''),
            'formulation': suggested_competence.get('formulation', ''),
            'position_suggeree': suggested_competence.get('position_suggeree', ''),
            'justification': suggested_competence.get('justification', ''),
            'ajoutee_via_suggestion': True  # Flag to indicate this was added via suggestion
        }
        
        # Update the YAML data
        yaml_data['etape_4_competences'] = competences_data
        
        return {
            'success': True,
            'message': f'Compétence C{new_competence_num} ajoutée avec succès',
            'competence_ajoutee': {
                'code': f'C{new_competence_num}',
                'titre': suggested_competence.get('titre', ''),
                'formulation': suggested_competence.get('formulation', ''),
                'position_suggeree': suggested_competence.get('position_suggeree', '')
            }
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Erreur lors de l\'ajout de la compétence : {str(e)}'
        }

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
        
        # Initialize referentiels_par_section if not exists
        if 'referentiels_par_section' not in yaml_data:
            yaml_data['referentiels_par_section'] = []
        
        # Add or update referentiel
        section_num = referentiel_data.get('section')
        existing_index = None
        
        for i, ref in enumerate(yaml_data['referentiels_par_section']):
            if ref.get('section') == section_num:
                existing_index = i
                break
        
        if existing_index is not None:
            yaml_data['referentiels_par_section'][existing_index] = referentiel_data
        else:
            yaml_data['referentiels_par_section'].append(referentiel_data)
        
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
        referentiel = None
        for ref in yaml_data.get('referentiels_par_section', []):
            if ref.get('section') == section_num:
                referentiel = ref
                break
        
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
