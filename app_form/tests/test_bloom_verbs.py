#!/usr/bin/env python3
"""
Test script to debug Bloom taxonomy route
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from questions.competences import COMPETENCES_QUESTIONS
    
    print("✅ Successfully imported COMPETENCES_QUESTIONS")
    print(f"Bloom taxonomy keys: {list(COMPETENCES_QUESTIONS.get('bloom_taxonomy', {}).keys())}")
    
    # Test the mapping logic
    niveau_mapping = {
        'Haut : Créer / Évaluer / Analyser': ['creer', 'evaluer', 'analyser', 'caracteriser', 'organiser'],
        'Moyen : Appliquer / Comprendre': ['appliquer', 'comprendre', 'valoriser', 'repondre'],
        'Bas : Se rappeler': ['se_rappeler', 'recevoir']
    }
    
    test_niveau = 'Moyen : Appliquer / Comprendre'
    selected_levels = niveau_mapping.get(test_niveau, [])
    print(f"Test niveau: {test_niveau}")
    print(f"Selected levels: {selected_levels}")
    
    bloom_taxonomy = COMPETENCES_QUESTIONS.get('bloom_taxonomy', {})
    result = {}
    for level in selected_levels:
        if level in bloom_taxonomy:
            result[level] = bloom_taxonomy[level]
    
    print(f"Result keys: {list(result.keys())}")
    print(f"Result structure: {type(result)}")
    
    # Test a specific level
    if 'appliquer' in result:
        print(f"Appliquer level: {result['appliquer']}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
