#!/usr/bin/env python3
"""
Script de test pour vérifier la configuration OpenAI
"""

import os
from dotenv import load_dotenv

def test_openai_config():
    """Test de la configuration OpenAI"""
    print("🔍 Test de la configuration OpenAI...")
    
    # 1. Test du chargement du fichier .env
    print("\n1. Test du chargement du fichier .env")
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print(f"✅ Clé API trouvée: {api_key[:10]}...{api_key[-4:]}")
    else:
        print("❌ Clé API non trouvée")
        print("   Vérifiez que le fichier .env existe et contient OPENAI_API_KEY=votre_cle")
        return False
    
    # 2. Test de la création du client OpenAI
    print("\n2. Test de la création du client OpenAI")
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        print("✅ Client OpenAI créé avec succès")
    except Exception as e:
        print(f"❌ Erreur lors de la création du client: {e}")
        return False
    
    # 3. Test d'un appel API simple
    print("\n3. Test d'un appel API simple")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Réponds simplement 'Test réussi'"}
            ],
            max_tokens=10
        )
        content = response.choices[0].message.content.strip()
        print(f"✅ Appel API réussi: {content}")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de l'appel API: {e}")
        return False

def test_ai_helpers():
    """Test du module ai_helpers"""
    print("\n🔍 Test du module ai_helpers...")
    
    try:
        from ai_helpers import generate_competency_suggestions
        
        # Test avec des données fictives
        test_data = {
            'contexte_formation': {
                'titre': 'Formation Test',
                'objectif_general': 'Objectif de test'
            },
            'public_cible': {
                'type': ['Enseignants'],
                'niveau_expertise': 'Moyen',
                'profil': 'Groupe homogène',
                'besoins_specifiques': ['Besoins de test']
            }
        }
        
        print("✅ Module ai_helpers importé avec succès")
        print("   (Le test complet nécessite une clé API valide)")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'import du module: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Test de la configuration OpenAI pour l'application Flask")
    print("=" * 60)
    
    # Test de la configuration
    config_ok = test_openai_config()
    
    # Test du module
    module_ok = test_ai_helpers()
    
    print("\n" + "=" * 60)
    if config_ok and module_ok:
        print("✅ Tous les tests sont passés ! L'application devrait fonctionner.")
    else:
        print("❌ Certains tests ont échoué. Vérifiez la configuration.")
        print("\n📋 Checklist:")
        print("   □ Fichier .env créé (renommez env_template.txt)")
        print("   □ Clé API OpenAI ajoutée dans .env")
        print("   □ Dépendances installées: pip install -r requirements.txt")
        print("   □ Clé API valide et active sur OpenAI Platform") 