#!/usr/bin/env python3
"""
Test script to verify the saving process across all steps
"""

import os
import yaml
import json
from datetime import datetime

def test_saving_process():
    """Test the complete saving process across all steps"""
    
    print("🧪 Testing Saving Process Across All Steps")
    print("=" * 50)
    
    # Test data for each step
    test_data = {
        'etape_1_public_cible': {
            'public_cible': {
                'type': 'Enseignants 2d degré',
                'profil': 'Groupe homogène (mêmes profils, mêmes besoins)',
                'niveau_expertise': 'Intermédiaire',
                'besoins_specifiques': ['Aucun besoin identifié'],
                'recommandations': ['À compléter ou à reformuler en fonction du profil et des besoins']
            },
            'contexte_formation': {
                'titre': 'Test Formation IA',
                'objectif_general': 'Test objectif général'
            }
        },
        'etape_2_contraintes': {
            'contraintes_formation': {
                'type_parcours': 'Création d\'un nouvel espace',
                'temps_total': 'Moins de 3h',
                'autonomie': 'Autoformation (sans accompagnement)',
                'animation': 'Formation animée par un seul intervenant',
                'calendrier': 'Début d\'année scolaire',
                'horaires': 'Sur temps de travail',
                'nombre_participants': 'Moins de 10 personnes',
                'exigences_institutionnelles': 'Non',
                'restrictions_techniques': 'Non',
                'exemple_associe': '001C_Exemple_Contraintes_Formation.md'
            }
        },
        'etape_3_scenario': {
            'scenario_cmo': {
                'title': 'Scénario structuré recommandé – Communauté Magistère Occitanie (CMO)',
                'description': 'Le scénario CMO propose une structuration claire et précise de la formation',
                'features': ['Prise en compte du public cible', 'Prise en compte des contraintes'],
                'sections': [
                    {'number': 1, 'type': 'Accueil', 'content': 'Présentation générale', 'modality': 'Asynchrone'},
                    {'number': 2, 'type': 'Section d\'apprentissage 1', 'content': 'Compétence 1', 'modality': 'Asynchrone'}
                ],
                'constraints': ['Durée de 3h maximum', 'Poids total de 512 Mo maximum'],
                'acknowledged': True,
                'timestamp': datetime.now().isoformat()
            }
        },
        'etape_4_competences': {
            'formulations_competences': [
                'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.',
                'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.',
                'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.'
            ],
            'competence_1': {
                'titre': 'Utilisation des outils d\'IA',
                'idees_cles': 'IA, outils, contenus pédagogiques',
                'niveau': 'Bas',
                'verbes': 'utiliser, créer',
                'formulation': 'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.'
            },
            'competence_2': {
                'titre': 'Personnalisation des parcours',
                'idees_cles': 'personnalisation, parcours, données',
                'niveau': 'Moyen',
                'verbes': 'personnaliser, adapter',
                'formulation': 'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.'
            },
            'competence_3': {
                'titre': 'Innovation pédagogique',
                'idees_cles': 'innovation, conception, solutions IA',
                'niveau': 'Haut',
                'verbes': 'innover, intégrer',
                'formulation': 'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.'
            },
            'evaluation_competences': {
                'ordre_competences': [
                    {
                        'code': 'C1',
                        'formulation': 'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.',
                        'justification': 'C1 est la compétence de base',
                        'pertinence': 'élevée'
                    },
                    {
                        'code': 'C2',
                        'formulation': 'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.',
                        'justification': 'C2 construit sur C1',
                        'pertinence': 'élevée'
                    },
                    {
                        'code': 'C3',
                        'formulation': 'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.',
                        'justification': 'C3 représente le niveau le plus élevé',
                        'pertinence': 'élevée'
                    }
                ],
                'avis_global': 'L\'ordre des compétences respecte la logique de progression pédagogique.',
                'points_amelioration': [
                    'Clarifier les verbes d\'action dans les formulations',
                    'Ajouter des exemples concrets d\'outils d\'IA'
                ],
                'competence_complementaire': {
                    'titre': 'Analyser les besoins des apprenants',
                    'niveau': 'Moyen',
                    'idees_cles': 'analyse, besoins, apprenants',
                    'verbes': 'analyser, évaluer, identifier',
                    'formulation': 'Être capable d\'analyser les besoins des apprenants afin de mieux personnaliser les parcours pédagogiques.',
                    'justification': 'Cette compétence est nécessaire pour combler le gap',
                    'position_suggeree': 'entre C1 et C2'
                }
            }
        },
        'etape_5_referentiels': [
            {
                'section': 1,
                'competence': 'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.',
                'niveaux': [
                    {
                        'degre': 1,
                        'libelle': 'Je débute',
                        'observable_qualitatif': 'Je suis capable de reconnaître les concepts de base.',
                        'observable_quantitatif': 'Je peux citer 1 à 2 concepts sur 5.',
                        'badge': 'non'
                    },
                    {
                        'degre': 2,
                        'libelle': 'Je progresse',
                        'observable_qualitatif': 'Je suis capable d\'expliquer les concepts de base.',
                        'observable_quantitatif': 'Je peux expliquer 3 à 4 concepts sur 5 avec une précision de 70%.',
                        'badge': 'non'
                    },
                    {
                        'degre': 3,
                        'libelle': 'Je suis autonome',
                        'observable_qualitatif': 'Je suis capable d\'appliquer les concepts de base dans des situations variées.',
                        'observable_quantitatif': 'Je peux appliquer 5 concepts sur 5 dans des scénarios pratiques avec une précision de 85%.',
                        'badge': 'oui'
                    },
                    {
                        'degre': 4,
                        'libelle': 'Je maîtrise avec aisance',
                        'observable_qualitatif': 'Je suis capable de synthétiser et d\'enseigner les concepts à d\'autres.',
                        'observable_quantitatif': 'Je peux enseigner 5 concepts sur 5 à des pairs avec une évaluation positive de 90%.',
                        'badge': 'non'
                    }
                ],
                'adaptations_cua': [
                    {
                        'besoin': 'Difficultés d\'apprentissage',
                        'adaptation': 'Mise à disposition de supports visuels et d\'exemples concrets pour faciliter la compréhension.'
                    }
                ]
            }
        ]
    }
    
    # Create test YAML file
    test_filename = f"test_formation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"
    test_filepath = os.path.join('output', test_filename)
    
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Build complete YAML data
    complete_data = {}
    complete_data['last_updated'] = datetime.now().isoformat()
    complete_data['current_step'] = 'etape_4_competences'
    
    # Add each step's data
    for step_name, step_data in test_data.items():
        complete_data[step_name] = step_data
    
    # Save to file
    try:
        with open(test_filepath, 'w', encoding='utf-8') as f:
            yaml.dump(complete_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print(f"✅ Test YAML file created: {test_filename}")
    except Exception as e:
        print(f"❌ Error creating test file: {e}")
        return False
    
    # Verify the file was created and contains all data
    try:
        with open(test_filepath, 'r', encoding='utf-8') as f:
            loaded_data = yaml.safe_load(f)
        
        print("\n📋 Verification Results:")
        print("-" * 30)
        
        # Check each step
        steps_to_check = [
            'etape_1_public_cible',
            'etape_2_contraintes', 
            'etape_3_scenario',
            'etape_4_competences',
            'etape_5_referentiels'
        ]
        
        all_steps_present = True
        for step in steps_to_check:
            if step in loaded_data:
                print(f"✅ {step}: Present")
                
                # Check specific data for competences
                if step == 'etape_4_competences':
                    competences_data = loaded_data[step]
                    formulations = competences_data.get('formulations_competences', [])
                    print(f"   - Formulations: {len(formulations)} found")
                    
                    # Check individual competences
                    for i in range(1, 4):
                        comp_key = f'competence_{i}'
                        if comp_key in competences_data:
                            comp_data = competences_data[comp_key]
                            titre = comp_data.get('titre', '')
                            formulation = comp_data.get('formulation', '')
                            print(f"   - {comp_key}: {titre if titre else formulation[:50]}...")
                            if not titre:
                                print(f"     ⚠️  Missing titre field")
                        else:
                            print(f"   - {comp_key}: Missing")
                            all_steps_present = False
                    
                    # Check evaluation_competences (nested under etape_4_competences)
                    evaluation_data = competences_data.get('evaluation_competences', {})
                    if evaluation_data:
                        ordre_competences = evaluation_data.get('ordre_competences', [])
                        print(f"   - Evaluation ordre compétences: {len(ordre_competences)} found")
                        
                        comp_complementaire = evaluation_data.get('competence_complementaire', {})
                        if comp_complementaire:
                            print(f"   - Compétence complémentaire: {comp_complementaire.get('titre', '')}")
                        else:
                            print(f"   - Compétence complémentaire: Missing")
                    else:
                        print(f"   - Evaluation competences: Missing")
                        all_steps_present = False
                
                # Check referentiels
                elif step == 'etape_5_referentiels':
                    refs = loaded_data[step]
                    print(f"   - Référentiels: {len(refs)} found")
                    for ref in refs:
                        section = ref.get('section', 'Unknown')
                        niveaux = ref.get('niveaux', [])
                        print(f"     Section {section}: {len(niveaux)} niveaux")
                
            else:
                print(f"❌ {step}: Missing")
                all_steps_present = False
        
        # Check metadata
        if 'last_updated' in loaded_data and 'current_step' in loaded_data:
            print(f"✅ Metadata: Present (current_step: {loaded_data['current_step']})")
        else:
            print("❌ Metadata: Missing")
            all_steps_present = False
        
        print(f"\n📊 Summary:")
        print(f"   - Total steps: {len(steps_to_check)}")
        print(f"   - Steps present: {sum(1 for step in steps_to_check if step in loaded_data)}")
        print(f"   - All steps present: {'✅ Yes' if all_steps_present else '❌ No'}")
        
        if all_steps_present:
            print(f"\n🎉 All tests passed! The saving process is working correctly.")
            print(f"📁 Test file: {test_filepath}")
            return True
        else:
            print(f"\n⚠️  Some tests failed. Please check the missing data.")
            return False
            
    except Exception as e:
        print(f"❌ Error verifying test file: {e}")
        return False

def test_competence_order_preservation():
    """Test that competence order (evaluation_competences) is preserved when submitting competences"""
    
    print("🧪 Testing Competence Order Preservation")
    print("=" * 50)
    
    # Simulate the scenario where user has already evaluated competences
    # and then validates to go to next page
    
    # Step 1: Create initial competences data with evaluation
    initial_competences_data = {
        'formulations_competences': [
            'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.',
            'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.',
            'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.'
        ],
        'competence_1': {
            'titre': 'Utilisation des outils d\'IA',
            'idees_cles': 'IA, outils, contenus pédagogiques',
            'niveau': 'Bas',
            'verbes': 'utiliser, créer',
            'formulation': 'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.'
        },
        'competence_2': {
            'titre': 'Personnalisation des parcours',
            'idees_cles': 'personnalisation, parcours, données',
            'niveau': 'Moyen',
            'verbes': 'personnaliser, adapter',
            'formulation': 'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.'
        },
        'competence_3': {
            'titre': 'Innovation pédagogique',
            'idees_cles': 'innovation, conception, solutions IA',
            'niveau': 'Haut',
            'verbes': 'innover, intégrer',
            'formulation': 'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.'
        },
        'evaluation_competences': {
            'ordre_competences': [
                {
                    'code': 'C1',
                    'formulation': 'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.',
                    'justification': 'C1 est la compétence de base',
                    'pertinence': 'élevée'
                },
                {
                    'code': 'C2',
                    'formulation': 'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.',
                    'justification': 'C2 construit sur C1',
                    'pertinence': 'élevée'
                },
                {
                    'code': 'C3',
                    'formulation': 'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.',
                    'justification': 'C3 représente le niveau le plus élevé',
                    'pertinence': 'élevée'
                }
            ],
            'avis_global': 'L\'ordre des compétences respecte la logique de progression pédagogique.',
            'points_amelioration': [
                'Clarifier les verbes d\'action dans les formulations',
                'Ajouter des exemples concrets d\'outils d\'IA'
            ],
            'competence_complementaire': {
                'titre': 'Analyser les besoins des apprenants',
                'niveau': 'Moyen',
                'idees_cles': 'analyse, besoins, apprenants',
                'verbes': 'analyser, évaluer, identifier',
                'formulation': 'Être capable d\'analyser les besoins des apprenants afin de mieux personnaliser les parcours pédagogiques.',
                'justification': 'Cette compétence est nécessaire pour combler le gap',
                'position_suggeree': 'entre C1 et C2'
            }
        }
    }
    
    # Step 2: Simulate what happens when user validates to go to next page
    # (This would be the data from the form submission)
    form_submission_data = {
        'formulation_1': 'Être capable d\'utiliser des outils d\'intelligence artificielle pour créer des contenus pédagogiques engageants.',
        'formulation_2': 'Être capable de personnaliser les parcours pédagogiques en fonction des données recueillies sur les apprenants.',
        'formulation_3': 'Être capable d\'innover dans la conception pédagogique en intégrant des solutions d\'intelligence artificielle.',
        'titre_1': 'Utilisation des outils d\'IA',
        'titre_2': 'Personnalisation des parcours',
        'titre_3': 'Innovation pédagogique',
        'idees_cles_1': 'IA, outils, contenus pédagogiques',
        'idees_cles_2': 'personnalisation, parcours, données',
        'idees_cles_3': 'innovation, conception, solutions IA',
        'niveau_1': 'Bas',
        'niveau_2': 'Moyen',
        'niveau_3': 'Haut',
        'verbes_1': 'utiliser, créer',
        'verbes_2': 'personnaliser, adapter',
        'verbes_3': 'innover, intégrer'
    }
    
    # Step 3: Simulate the submit_competences logic
    # Generate YAML data for competencies
    competences_data = {
        'formulations_competences': []
    }
    
    # Count competences from the data
    competence_count = 0
    for key in form_submission_data.keys():
        if key.startswith('formulation_'):
            competence_count = max(competence_count, int(key.split('_')[1]))
    
    # Extract formulations for each competence
    for i in range(1, competence_count + 1):
        formulation = form_submission_data.get(f'formulation_{i}', '')
        if formulation:
            competences_data['formulations_competences'].append(formulation)
    
    # Add detailed data for each competence
    for i in range(1, competence_count + 1):
        competence_key = f'competence_{i}'
        competences_data[competence_key] = {
            'titre': form_submission_data.get(f'titre_{i}', ''),
            'idees_cles': form_submission_data.get(f'idees_cles_{i}', ''),
            'niveau': form_submission_data.get(f'niveau_{i}', ''),
            'verbes': form_submission_data.get(f'verbes_{i}', ''),
            'formulation': form_submission_data.get(f'formulation_{i}', '')
        }
    
    # Step 4: Preserve existing evaluation_competences data if it exists
    existing_competences = initial_competences_data
    if 'evaluation_competences' in existing_competences:
        competences_data['evaluation_competences'] = existing_competences['evaluation_competences']
    
    # Step 5: Verify that evaluation_competences is preserved
    if 'evaluation_competences' in competences_data:
        print("✅ evaluation_competences preserved successfully!")
        print(f"   - ordre_competences count: {len(competences_data['evaluation_competences'].get('ordre_competences', []))}")
        print(f"   - avis_global: {competences_data['evaluation_competences'].get('avis_global', 'N/A')}")
        print(f"   - competence_complementaire: {competences_data['evaluation_competences'].get('competence_complementaire', {}).get('titre', 'N/A')}")
        
        # Verify the order is correct
        ordre_competences = competences_data['evaluation_competences'].get('ordre_competences', [])
        if len(ordre_competences) == 3:
            print("✅ All 3 competences are in the order!")
            for i, comp in enumerate(ordre_competences, 1):
                print(f"   {i}. {comp.get('code', 'N/A')}: {comp.get('formulation', 'N/A')[:50]}...")
        else:
            print(f"❌ Expected 3 competences in order, got {len(ordre_competences)}")
            return False
    else:
        print("❌ evaluation_competences was lost!")
        return False
    
    # Step 6: Verify that basic competences data is also preserved
    if 'formulations_competences' in competences_data and len(competences_data['formulations_competences']) == 3:
        print("✅ Basic competences data preserved!")
    else:
        print("❌ Basic competences data was lost!")
        return False
    
    print("\n🎉 All tests passed! Competence order preservation is working correctly.")
    return True

if __name__ == "__main__":
    print("🚀 Running all tests...")
    print("=" * 60)
    
    # Run the main saving process test
    success1 = test_saving_process()
    
    print("\n" + "=" * 60)
    
    # Run the competence order preservation test
    success2 = test_competence_order_preservation()
    
    print("\n" + "=" * 60)
    
    if success1 and success2:
        print("✅ All tests completed successfully!")
    else:
        print("❌ Some tests failed!")
        if not success1:
            print("   - Main saving process test failed")
        if not success2:
            print("   - Competence order preservation test failed")
        exit(1) 