#!/usr/bin/env python3
"""
Test script for the contenu page functionality
"""

import os
import sys
import yaml
from datetime import datetime

# Add the app_form directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from routes.contenu import (
    generate_contenus_with_ai,
    generate_mock_contenus,
    extract_competence_code,
    parse_ai_contenus_response
)

def test_extract_competence_code():
    """Test the competence code extraction function"""
    print("Testing extract_competence_code...")
    
    test_cases = [
        ("C1 - Identifier les concepts clés", "C1"),
        ("C2 - Appliquer les méthodes", "C2"),
        ("C3 - Analyser les situations", "C3"),
        ("D1 - Évaluer les résultats", "D1"),
        ("Pas de code", None),
        ("", None)
    ]
    
    for formulation, expected in test_cases:
        result = extract_competence_code(formulation)
        status = "✅" if result == expected else "❌"
        print(f"  {status} '{formulation}' -> '{result}' (expected: '{expected}')")

def test_generate_mock_contenus():
    """Test the mock contenus generation"""
    print("\nTesting generate_mock_contenus...")
    
    # Mock competences data
    competences_data = {
        'ordre_competences': [
            {
                'code': 'C1',
                'formulation': 'C1 - Identifier les concepts clés'
            },
            {
                'code': 'C2',
                'formulation': 'C2 - Appliquer les méthodes'
            }
        ]
    }
    
    contenus = generate_mock_contenus(competences_data)
    
    print(f"  Generated contenus for {len(contenus)} competences:")
    for code, contenus_list in contenus.items():
        print(f"    {code}: {len(contenus_list)} contenus")
        for contenu in contenus_list:
            print(f"      - {contenu['type']}: {contenu['nom']} ({contenu['intention']})")

def test_parse_ai_contenus_response():
    """Test the AI response parsing"""
    print("\nTesting parse_ai_contenus_response...")
    
    # Mock AI response
    mock_ai_response = """
    ```yaml
    contenus_par_section:
      - section: 2
        type_section: Apprentissage
        competence_visee: C1 - Identifier les concepts clés
        ressource: Page de contenu
        intention_ressource: Acquisition
        activite_1: Quiz interactif
        intention_activite_1: Pratique
        activite_2: null
        intention_activite_2: null
        justification: Sélection basée sur la pertinence pédagogique
      - section: 3
        type_section: Apprentissage
        competence_visee: C2 - Appliquer les méthodes
        ressource: Ressource H5P
        intention_ressource: Acquisition
        activite_1: Exercice pratique
        intention_activite_1: Production
        activite_2: Discussion forum
        intention_activite_2: Discussion
        justification: Activités complémentaires pour renforcer l'apprentissage
    ```
    """
    
    contenus = parse_ai_contenus_response(mock_ai_response)
    
    print(f"  Parsed {len(contenus)} competences:")
    for code, contenus_list in contenus.items():
        print(f"    {code}: {len(contenus_list)} contenus")
        for contenu in contenus_list:
            print(f"      - {contenu['type']}: {contenu['nom']} ({contenu['intention']})")

def test_contenus_generation_workflow():
    """Test the complete contenus generation workflow"""
    print("\nTesting complete contenus generation workflow...")
    
    # Mock competences data
    competences_data = {
        'ordre_competences': [
            {
                'code': 'C1',
                'formulation': 'C1 - Identifier les concepts clés de l\'IA en éducation'
            },
            {
                'code': 'C2',
                'formulation': 'C2 - Appliquer les méthodes d\'intégration de l\'IA'
            },
            {
                'code': 'C3',
                'formulation': 'C3 - Évaluer l\'impact de l\'IA sur les apprentissages'
            }
        ]
    }
    
    # Test with mock generation (since we don't have AI API in test)
    contenus = generate_mock_contenus(competences_data)
    
    print(f"  Generated contenus for {len(contenus)} competences:")
    
    # Simulate the frontend workflow
    for code, contenus_list in contenus.items():
        print(f"\n  📋 {code}:")
        for i, contenu in enumerate(contenus_list, 1):
            print(f"    {i}. {contenu['type']}: {contenu['nom']}")
            print(f"       Intention: {contenu['intention']}")
            print(f"       Recommandation: {'★' * contenu['recommandation']}")
            print(f"       Description: {contenu['description']}")
    
    # Test section generation
    print(f"\n  📊 Sections générées:")
    sections = []
    
    # S1 - Accueil
    sections.append({
        'section': 1,
        'type_section': 'Accueil',
        'competence_visee': None,
        'ressource': None,
        'intention_ressource': None,
        'activite_1': None,
        'intention_activite_1': None,
        'activite_2': None,
        'intention_activite_2': None,
        'justification': None
    })
    
    # S2-S5 - Apprentissage
    for i, (code, contenus_list) in enumerate(contenus.items(), 2):
        if contenus_list:
            selected_contenu = contenus_list[0]  # Simulate selection
            sections.append({
                'section': i,
                'type_section': 'Apprentissage',
                'competence_visee': competences_data['ordre_competences'][i-2]['formulation'],
                'ressource': selected_contenu['type'] == 'Ressource' and selected_contenu['nom'] or 'Page',
                'intention_ressource': 'Acquisition',
                'activite_1': selected_contenu['type'] == 'Activité' and selected_contenu['nom'] or 'Activité H5P',
                'intention_activite_1': selected_contenu['intention'],
                'activite_2': None,
                'intention_activite_2': None,
                'justification': 'Sélection basée sur la pertinence pédagogique'
            })
    
    # S6 - Classe virtuelle
    sections.append({
        'section': 6,
        'type_section': 'Classe virtuelle (BBB)',
        'competence_visee': None,
        'ressource': None,
        'intention_ressource': None,
        'activite_1': 'BigBlueButtonBN',
        'intention_activite_1': 'Discussion',
        'activite_2': None,
        'intention_activite_2': None,
        'justification': None
    })
    
    # S7 - Forum
    sections.append({
        'section': 7,
        'type_section': 'Forum général',
        'competence_visee': None,
        'ressource': None,
        'intention_ressource': None,
        'activite_1': 'Forum',
        'intention_activite_1': 'Discussion / Collaboration',
        'activite_2': None,
        'intention_activite_2': None,
        'justification': None
    })
    
    # S8 - Évaluation
    sections.append({
        'section': 8,
        'type_section': 'Évaluation',
        'competence_visee': None,
        'ressource': None,
        'intention_ressource': None,
        'activite_1': 'Sondage Magistère',
        'intention_activite_1': 'Enquête',
        'activite_2': None,
        'intention_activite_2': None,
        'justification': None
    })
    
    for section in sections:
        print(f"    S{section['section']}: {section['type_section']}")
        if section['competence_visee']:
            print(f"      Compétence: {section['competence_visee']}")
        if section['ressource']:
            print(f"      Ressource: {section['ressource']} ({section['intention_ressource']})")
        if section['activite_1']:
            print(f"      Activité 1: {section['activite_1']} ({section['intention_activite_1']})")

def main():
    """Run all tests"""
    print("🧪 Testing Contenu Page Functionality")
    print("=" * 50)
    
    test_extract_competence_code()
    test_generate_mock_contenus()
    test_parse_ai_contenus_response()
    test_contenus_generation_workflow()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")

if __name__ == "__main__":
    main()
