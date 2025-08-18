#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.contenu import parse_ai_contenus_response

def test_parsing():
    """Test the AI response parsing function"""
    try:
        # Read the test response
        with open('debug/contenus_response.txt', 'r', encoding='utf-8') as f:
            test_response = f.read()
        
        # Parse the response
        result = parse_ai_contenus_response(test_response)
        
        print(f"Parsed sections: {len(result)}")
        if result:
            print(f"First section: {result[0]}")
            print(f"Last section: {result[-1]}")
            
            # Check if all sections are properly formatted
            for i, section in enumerate(result):
                required_fields = ['section', 'type_de_section', 'competences_visees', 
                                 'ressource', 'intention_ressource', 'activite_1', 
                                 'intention_activite_1', 'activite_2', 'intention_activite_2', 
                                 'justification_activite_s']
                
                missing_fields = [field for field in required_fields if field not in section]
                if missing_fields:
                    print(f"Section {i+1} missing fields: {missing_fields}")
                else:
                    print(f"Section {i+1} ({section['section']}) - {section['type_de_section']} ✓")
        else:
            print("No result returned")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_parsing()
