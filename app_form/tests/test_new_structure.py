#!/usr/bin/env python3
"""
Script de test pour vérifier la nouvelle structure YAML avec 4 étapes
"""

import yaml
import os
from routes.main import check_previous_steps_completed

def test_new_yaml_structure():
    """Test de la nouvelle structure YAML"""
    print("🔍 Test de la nouvelle structure YAML...")
    
    # Charger le fichier YAML
    yaml_file = "output/formation_20250813_110258.yaml"
    
    if not os.path.exists(yaml_file):
        print("❌ Fichier YAML non trouvé")
        return False
    
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
    
    # Vérifier la structure
    print("\n📋 Structure YAML:")
    
    # Vérifier les étapes principales (maintenant 4 étapes)
    required_steps = ['etape_1_public_cible', 'etape_2_contraintes', 'etape_3_competences', 'etape_4_referentiels']
    for step in required_steps:
        if step in yaml_data:
            print(f"✅ {step}: Présent")
        else:
            print(f"❌ {step}: Manquant")
    
    # Vérifier la structure de etape_3_competences
    if 'etape_3_competences' in yaml_data:
        competences = yaml_data['etape_3_competences']
        print(f"\n📚 etape_3_competences:")
        
        # Vérifier formulations_competences
        if 'formulations_competences' in competences:
            print(f"✅ formulations_competences: {len(competences['formulations_competences'])} compétences")
        else:
            print("❌ formulations_competences: Manquant")
        
        # Vérifier evaluation_competences (maintenant à l'intérieur)
        if 'evaluation_competences' in competences:
            print("✅ evaluation_competences: Présent (déplacé à l'intérieur)")
            eval_data = competences['evaluation_competences']
            if 'ordre_competences' in eval_data:
                print(f"  ✅ ordre_competences: {len(eval_data['ordre_competences'])} compétences ordonnées")
        else:
            print("❌ evaluation_competences: Manquant")
        
        # Vérifier les compétences individuelles
        for i in range(1, 4):
            competence_key = f'competence_{i}'
            if competence_key in competences:
                titre = competences[competence_key].get('titre', 'Sans titre')
                print(f"✅ {competence_key}: {titre}")
            else:
                print(f"❌ {competence_key}: Manquant")
    
    # Vérifier etape_4_referentiels
    if 'etape_4_referentiels' in yaml_data:
        referentiels = yaml_data['etape_4_referentiels']
        print(f"\n📊 etape_4_referentiels:")
        
        if 'referentiels_par_section' in referentiels:
            print(f"✅ referentiels_par_section: {len(referentiels['referentiels_par_section'])} référentiels")
        else:
            print("❌ referentiels_par_section: Manquant")
    
    # Vérifier current_step
    current_step = yaml_data.get('current_step', 'Non défini')
    print(f"\n📍 current_step: {current_step}")
    
    return True

def test_verifications():
    """Test des vérifications d'étapes avec la nouvelle structure"""
    print("\n🔍 Test des vérifications d'étapes...")
    
    # Test avec la nouvelle structure (4 étapes)
    required_steps = ['etape_1_public_cible', 'etape_2_contraintes', 'etape_3_competences']
    completed, message = check_previous_steps_completed(required_steps)
    
    if completed:
        print("✅ Vérification des étapes: OK")
    else:
        print(f"❌ Vérification des étapes: {message}")
    
    return completed

def test_referentiels_loading():
    """Test du chargement des référentiels avec la nouvelle structure"""
    print("\n🔍 Test du chargement des référentiels...")
    
    yaml_file = "output/formation_20250813_110258.yaml"
    
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
    
    # Simuler le chargement comme dans referentiels.py
    competences_data = yaml_data.get('etape_3_competences', {})
    evaluation_data = competences_data.get('evaluation_competences', {})
    formulations = competences_data.get('formulations_competences', [])
    existing_referentiels = yaml_data.get('etape_4_referentiels', {}).get('referentiels_par_section', [])
    
    print(f"✅ Formulations trouvées: {len(formulations)}")
    print(f"✅ Référentiels existants: {len(existing_referentiels)}")
    
    # Vérifier la correspondance
    if len(formulations) == len(existing_referentiels):
        print("✅ Correspondance formulations/référentiels: OK")
    else:
        print(f"⚠️ Correspondance formulations/référentiels: {len(formulations)} vs {len(existing_referentiels)}")
    
    return True

if __name__ == "__main__":
    print("🚀 Début des tests de la nouvelle structure YAML")
    print("=" * 60)
    
    # Tests
    test_new_yaml_structure()
    test_verifications()
    test_referentiels_loading()
    
    print("\n" + "=" * 60)
    print("✅ Tests terminés")
