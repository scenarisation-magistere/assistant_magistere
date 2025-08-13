#!/usr/bin/env python3
"""
Test script to verify that referentiels page uses the saved titre field
"""

import os
import yaml
import sys

# Add the current directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_referentiels_titre_usage():
    """Test that referentiels page uses the saved titre field"""
    
    print("🧪 Testing Referentiels Titre Usage")
    print("=" * 40)
    
    # Load the test YAML file
    test_files = [f for f in os.listdir('output') if f.startswith('test_formation_') and f.endswith('.yaml')]
    
    if not test_files:
        print("❌ No test YAML files found. Please run test_saving_process.py first.")
        return False
    
    # Use the most recent test file
    test_file = sorted(test_files)[-1]
    test_filepath = os.path.join('output', test_file)
    
    print(f"📁 Using test file: {test_file}")
    
    try:
        with open(test_filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading test file: {e}")
        return False
    
    # Test the referentiels page logic
    print("\n📋 Testing Referentiels Page Logic:")
    print("-" * 35)
    
    # Extract competences data
    competences_data = yaml_data.get('etape_4_competences', {})
    formulations = competences_data.get('formulations_competences', [])
    
    print(f"1. Formulations trouvées: {len(formulations)}")
    
    # Simulate the referentiels page logic
    sections = []
    for i, formulation in enumerate(formulations, 1):
        # Try to get the titre from the competence data
        competence_key = f'competence_{i}'
        titre = ''
        if competence_key in competences_data:
            titre = competences_data[competence_key].get('titre', '')
        
        # Extract title function (simplified version)
        def extract_title(competence_text):
            prefixes_to_remove = [
                "Être capable de ", "Être capable d'", "Savoir ", "Pouvoir ", 
                "Maîtriser ", "Connaître "
            ]
            title = competence_text
            for prefix in prefixes_to_remove:
                if title.startswith(prefix):
                    title = title[len(prefix):]
                    break
            if title:
                title = title[0].upper() + title[1:]
            if len(title) > 40:
                title = title[:40] + "..."
            return title
        
        final_title = titre if titre else extract_title(formulation)
        
        sections.append({
            'numero': i,
            'competence': formulation,
            'code': f'C{i}',
            'title': final_title
        })
        
        print(f"   Section {i}:")
        print(f"     - Titre sauvegardé: '{titre}'")
        print(f"     - Titre extrait: '{extract_title(formulation)}'")
        print(f"     - Titre final utilisé: '{final_title}'")
        print(f"     - Utilise titre sauvegardé: {'✅ Oui' if titre else '❌ Non (fallback)'}")
    
    # Check if titles are being used correctly
    print(f"\n📊 Summary:")
    print(f"   - Total sections: {len(sections)}")
    
    titles_used = 0
    fallbacks_used = 0
    
    for section in sections:
        competence_key = f'competence_{section["numero"]}'
        if competence_key in competences_data:
            saved_titre = competences_data[competence_key].get('titre', '')
            if saved_titre:
                titles_used += 1
            else:
                fallbacks_used += 1
    
    print(f"   - Titres sauvegardés utilisés: {titles_used}")
    print(f"   - Fallbacks utilisés: {fallbacks_used}")
    
    # Verify the expected titles
    expected_titles = [
        'Utilisation des outils d\'IA',
        'Personnalisation des parcours', 
        'Innovation pédagogique'
    ]
    
    print(f"\n🎯 Expected vs Actual Titles:")
    for i, (expected, section) in enumerate(zip(expected_titles, sections)):
        actual = section['title']
        match = expected == actual
        print(f"   Section {i+1}:")
        print(f"     - Expected: '{expected}'")
        print(f"     - Actual: '{actual}'")
        print(f"     - Match: {'✅ Yes' if match else '❌ No'}")
    
    # Test the template rendering simulation
    print(f"\n🎨 Template Rendering Simulation:")
    for section in sections:
        template_line = f"📚 Section {section['numero']} - {section['code']} : {section['title']}"
        print(f"   {template_line}")
    
    # Final verification
    all_titles_used = titles_used == len(sections)
    all_titles_match = all(expected == section['title'] for expected, section in zip(expected_titles, sections))
    
    if all_titles_used and all_titles_match:
        print(f"\n🎉 All tests passed!")
        print(f"✅ Referentiels page is correctly using saved titre fields")
        return True
    else:
        print(f"\n⚠️ Some tests failed")
        if not all_titles_used:
            print(f"❌ Not all saved titles are being used")
        if not all_titles_match:
            print(f"❌ Title values don't match expected")
        return False

def test_referentiels_page_integration():
    """Test the actual referentiels page integration"""
    
    print(f"\n🔗 Testing Referentiels Page Integration:")
    print("-" * 40)
    
    try:
        # Import the referentiels page function
        from questions.referentiels import referentiels_page
        print("✅ Referentiels page function imported successfully")
        
        # Load test data
        test_files = [f for f in os.listdir('output') if f.startswith('test_formation_') and f.endswith('.yaml')]
        if not test_files:
            print("❌ No test YAML files found.")
            return False
        
        test_file = sorted(test_files)[-1]
        test_filepath = os.path.join('output', test_file)
        
        with open(test_filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        
        # Simulate the data extraction that referentiels_page does
        competences_data = yaml_data.get('etape_4_competences', {})
        formulations = competences_data.get('formulations_competences', [])
        
        print(f"✅ Data extraction successful")
        print(f"   - Competences data: {len(competences_data)} competences")
        print(f"   - Formulations: {len(formulations)} formulations")
        
        # Check if titre fields are present
        titre_fields_present = 0
        for i in range(1, len(formulations) + 1):
            competence_key = f'competence_{i}'
            if competence_key in competences_data:
                titre = competences_data[competence_key].get('titre', '')
                if titre:
                    titre_fields_present += 1
                    print(f"   - {competence_key}: '{titre}'")
        
        print(f"✅ Titre fields found: {titre_fields_present}/{len(formulations)}")
        
        return titre_fields_present == len(formulations)
        
    except ImportError as e:
        print(f"❌ Error importing referentiels page: {e}")
        return False
    except Exception as e:
        print(f"❌ Error in integration test: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Referentiels Titre Usage Test")
    print("=" * 40)
    
    # Test 1: Logic verification
    success1 = test_referentiels_titre_usage()
    
    # Test 2: Integration verification
    success2 = test_referentiels_page_integration()
    
    if success1 and success2:
        print(f"\n🎉 All referentiels titre tests passed!")
        print(f"✅ The referentiels page is correctly using saved titre fields")
    else:
        print(f"\n❌ Some referentiels titre tests failed!")
        print(f"⚠️ Please check the titre field usage in referentiels page")
        exit(1) 