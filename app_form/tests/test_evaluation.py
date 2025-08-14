#!/usr/bin/env python3
"""
Test simple pour vérifier que la fonction d'évaluation fonctionne
"""

import yaml
from ai_helpers import evaluate_and_order_competences

# Données de test plus réalistes
test_yaml_data = {
    'etape_1_public_cible': {
        'public_cible': {
            'type': 'Enseignants 2d degré',
            'profil': 'Groupe homogène',
            'niveau_expertise': 'Intermédiaire'
        },
        'contexte_formation': {
            'titre': 'Exploiter l\'Intelligence Artificielle pour Concevoir des Formations Innovantes',
            'objectif_general': 'Permettre aux professionnels de la formation de renforcer leurs compétences dans l\'utilisation des outils d\'intelligence artificielle pour concevoir, structurer et optimiser des parcours pédagogiques.'
        }
    },
    'etape_2_contraintes': {
        'contraintes_formation': {
            'type_parcours': 'Création d\'un nouvel espace',
            'temps_total': 'Entre 3h et 6h'
        }
    },
    'etape_4_competences': {
        'formulations_competences': [
            'À l\'issue de la formation, les participants seront capables d\'identifier divers outils d\'intelligence artificielle adaptés à la conception de formations.',
            'À l\'issue de la formation, les participants sauront décrire le fonctionnement des IA génératives, telles que ChatGPT, et leur application dans le contexte pédagogique.',
            'À l\'issue de la formation, les participants seront capables d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques variés, tels que des quiz et des fiches de synthèse.',
            'À l\'issue de la formation, les participants sauront personnaliser les parcours d\'apprentissage en utilisant des outils d\'intelligence artificielle, pour répondre aux besoins spécifiques des apprenants.'
        ],
        'competence_1': {
            'idees_cles': 'outils d\'IA, identification, formation',
            'niveau': 'Bas',
            'verbes': 'identifier, reconnaître, lister',
            'formulation': 'À l\'issue de la formation, les participants seront capables d\'identifier divers outils d\'intelligence artificielle adaptés à la conception de formations.'
        },
        'competence_2': {
            'idees_cles': 'IA génératives, fonctionnement, description',
            'niveau': 'Bas',
            'verbes': 'décrire, expliquer, illustrer',
            'formulation': 'À l\'issue de la formation, les participants sauront décrire le fonctionnement des IA génératives, telles que ChatGPT, et leur application dans le contexte pédagogique.'
        },
        'competence_3': {
            'idees_cles': 'création de contenus, outils d\'IA, pédagogie',
            'niveau': 'Moyen',
            'verbes': 'utiliser, appliquer, produire',
            'formulation': 'À l\'issue de la formation, les participants seront capables d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques variés, tels que des quiz et des fiches de synthèse.'
        },
        'competence_4': {
            'idees_cles': 'personnalisation, parcours d\'apprentissage, IA',
            'niveau': 'Moyen',
            'verbes': 'personnaliser, adapter, modifier',
            'formulation': 'À l\'issue de la formation, les participants sauront personnaliser les parcours d\'apprentissage en utilisant des outils d\'intelligence artificielle, pour répondre aux besoins spécifiques des apprenants.'
        }
    }
}

def test_evaluation():
    """Test de la fonction d'évaluation"""
    print("=== Test de la fonction d'évaluation ===")
    print(f"Nombre de compétences à évaluer : {len(test_yaml_data['etape_4_competences']['formulations_competences'])}")
    
    result = evaluate_and_order_competences(test_yaml_data)
    
    print(f"\nRésultat: {result['success']}")
    
    if result['success']:
        print("✅ Test réussi !")
        evaluation = result['evaluation']
        
        print(f"\nNombre de compétences ordonnées : {len(evaluation.get('ordre_competences', []))}")
        
        if 'ordre_competences' in evaluation:
            print("\n📋 Compétences ordonnées :")
            for comp in evaluation['ordre_competences']:
                print(f"  {comp['code']}: {comp['formulation'][:50]}...")
                print(f"    Pertinence: {comp['pertinence']}")
                print(f"    Justification: {comp['justification'][:100]}...")
                print()
        
        if 'avis_global' in evaluation:
            print(f"\n📊 Avis global : {evaluation['avis_global'][:200]}...")
        
        if 'points_amelioration' in evaluation:
            print(f"\n💡 Points d'amélioration : {len(evaluation['points_amelioration'])} points")
            for point in evaluation['points_amelioration']:
                print(f"  - {point}")
    else:
        print("❌ Test échoué !")
        print(f"Erreur: {result.get('error', 'Erreur inconnue')}")

if __name__ == '__main__':
    test_evaluation() 