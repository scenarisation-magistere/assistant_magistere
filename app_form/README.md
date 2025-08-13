# Questionnaire Formation - Flask App

Cette application Flask convertit les questionnaires de détermination du public cible et des contraintes de formation en une interface web moderne et interactive en trois étapes, avec génération automatique de scénario CMO.

## 🚀 Installation

1. **Cloner ou télécharger** le projet dans le dossier `app_form/`
2. **Installer les dépendances** :
   ```bash
   cd app_form
   pip install -r requirements.txt
   ```
3. **Configurer l'API OpenAI** :
   - Renommez `env_template.txt` en `.env`
   - Ajoutez votre clé API OpenAI : `OPENAI_API_KEY=votre_cle_api_ici`
   - Obtenez votre clé sur [OpenAI Platform](https://platform.openai.com/api-keys)
4. **Tester la configuration** (optionnel) :
   ```bash
   python test_openai.py
   ```
5. **Lancer l'application** :
   ```bash
   python app.py
   ```
6. **Accéder à l'application** : http://localhost:5000

## 📋 Fonctionnalités

### **Étape 1 : Public Cible** (6 questions)
- **Interface moderne** : Design responsive avec animations et transitions
- **Questions** :
  1. Titre de la formation (champ texte)
  2. Objectif général (zone de texte)
  3. Type de public visé (cases à cocher multiples)
  4. Niveau d'expertise (boutons radio)
  5. Profil du groupe (boutons radio)
  6. Besoins spécifiques (cases à cocher multiples)

### **Étape 2 : Contraintes Formation** (9 questions)
- **Questions** :
  1. Type de parcours (création/migration)
  2. Temps estimé de la formation
  3. Autonomie souhaitée des participants
  4. Modalités d'animation
  5. Contraintes de calendrier
  6. Contraintes d'horaires
  7. Nombre estimé de participants
  8. Exigences institutionnelles
  9. Restrictions techniques

### **Étape 3 : Scénario CMO** (Page d'information)
- **Présentation du scénario CMO** : Structure et contraintes
- **Page d'information** : Présentation claire de la structure recommandée
- **Téléchargement des données** : Accès aux fichiers YAML générés
- **Options de navigation** : Possibilité de recommencer le questionnaire

### **Étape 4 : Compétences Visées** (Formulation avec IA)
- **Formulation des compétences** : 4 compétences structurées en étapes
- **Suggestions IA** : Boutons pour obtenir des suggestions de verbes d'action
- **Génération IA complète** : Suggestions de compétences basées sur les données précédentes
- **Taxonomie de Bloom** : Niveaux cognitifs (Haut, Moyen, Bas)
- **Génération automatique** : Formulations générées à partir des choix
- **Rappel des données** : Affichage des informations des étapes précédentes
- **Intégration OpenAI** : Appels réels à GPT-4o-mini pour les suggestions

### **Fonctionnalités communes**
- **Barre de progression** : Indique l'avancement du remplissage
- **Exemples intégrés** : Chaque question affiche des exemples de réponses
- **Génération YAML** : Export automatique des données au format YAML
- **Sauvegarde** : Les résultats sont sauvegardés dans un fichier avec timestamp
- **Avertissement migration** : Affichage automatique d'un avertissement si migration détectée
- **Champs conditionnels** : Affichage de champs texte supplémentaires selon les réponses
- **Session persistante** : Conservation des données entre les étapes

## 📁 Structure des fichiers

```
app_form/
├── app.py                    # Application Flask principale
├── ai_helpers.py             # Fonctions d'aide pour l'IA
├── env_template.txt          # Template pour la configuration OpenAI
├── .env                      # Configuration OpenAI (à créer)
├── questions/                # Dossier des questions
│   ├── __init__.py           # Fichier d'initialisation du package
│   ├── public_cible.py       # Questions pour l'étape 1
│   ├── contraintes.py        # Questions pour l'étape 2
│   ├── scenario.py           # Structure du scénario CMO
│   └── competences.py        # Questions pour l'étape 4
├── templates/
│   ├── public_cible.html     # Template pour l'étape 1
│   ├── contraintes.html      # Template pour l'étape 2
│   ├── scenario.html         # Template pour l'étape 3
│   └── competences.html      # Template pour l'étape 4
├── output/                   # Dossier de sortie YAML
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation
```

## 🎯 Utilisation

1. **Étape 1** : Remplissez le formulaire "Public Cible"
2. Cliquez sur "Valider et Continuer vers les Contraintes"
3. **Étape 2** : Remplissez le formulaire "Contraintes Formation"
4. Cliquez sur "Valider et Continuer vers le Scénario CMO"
5. **Étape 3** : Consultez la structure du scénario CMO (page d'information)
6. Cliquez sur "Continuer vers les Compétences Visées"
7. **Étape 4** : Formulez les compétences visées avec suggestions IA
8. **Un seul fichier YAML** est créé dans le dossier `output/` et mis à jour à chaque étape
9. **Options disponibles** : Télécharger les données ou recommencer le questionnaire

## 📊 Format de sortie

**Un seul fichier YAML par session** est créé dans le dossier `output/` avec la structure suivante :

```yaml
etape_1_public_cible:
  public_cible: [données du public cible]
  contexte_formation: [contexte de formation]

etape_2_contraintes:
  public_cible: [données du public cible]
  contexte_formation: [contexte de formation]
  contraintes_formation: [données des contraintes]

etape_3_scenario_complet:
  public_cible: [données du public cible]
  contexte_formation: [contexte de formation]
  contraintes_formation: [données des contraintes]
  scenario_cmo: [scénario généré avec compétences, sections, ressources, activités]

last_updated: "2024-01-15T14:30:00"
current_step: "etape_3_scenario_complet"
```

**Avantages de cette approche :**
- **Un seul fichier** par session de formation
- **Progression visible** : chaque étape ajoute ses données
- **Historique complet** : toutes les étapes sont conservées
- **Organisation claire** : dossier `output/` dédié
- **Traçabilité** : horodatage et étape courante

## ⚠️ Fonctionnalité Migration

Si l'utilisateur sélectionne "Migration d'un parcours existant", l'application affiche automatiquement :
- Un lien vers la ressource de migration Magistère
- Un avertissement sur la date limite d'accompagnement (octobre 2025)
- Un avertissement sur la perte des données après décembre 2025

## 🤖 Intégration IA (OpenAI)

L'application intègre des fonctionnalités IA avancées pour la génération de suggestions de compétences :

### **Configuration OpenAI**
- **Modèle** : GPT-4o-mini (configurable dans `.env`)
- **Tokens max** : 1000 (configurable)
- **Température** : 0.7 (configurable)

### **Fonctionnalités IA**
- **Génération de suggestions** : 4 compétences complètes basées sur les données de formation
- **Analyse contextuelle** : Utilise le titre, objectif, public cible et besoins spécifiques
- **Taxonomie de Bloom** : Respect des niveaux cognitifs dans les suggestions
- **Format JSON structuré** : Réponses formatées pour une intégration facile

### **Gestion d'erreurs**
- **Authentification** : Vérification de la clé API
- **Limites de taux** : Gestion des erreurs de quota
- **Parsing JSON** : Gestion des réponses malformées
- **Fallback** : Suggestions locales en cas d'échec API
- **Mode dégradé** : Fonctionnement sans OpenAI avec suggestions prédéfinies

### **Mode Fallback**
L'application fonctionne même sans OpenAI grâce à un système de fallback :
- **Suggestions prédéfinies** : Basées sur la taxonomie de Bloom
- **Adaptation au niveau** : Haut, Moyen, Bas selon les données
- **Personnalisation** : Utilise le titre de formation
- **Indication visuelle** : Bannière "Mode Fallback" dans l'interface

## 🔧 Dépannage OpenAI

### **Erreurs courantes :**

#### **"Clé API OpenAI non trouvée"**
- Vérifiez que le fichier `.env` existe (renommez `env_template.txt`)
- Vérifiez que la ligne `OPENAI_API_KEY=votre_cle_api_ici` est présente
- Assurez-vous qu'il n'y a pas d'espaces autour du `=`

#### **"Erreur d'authentification OpenAI"**
- Vérifiez que votre clé API est valide sur [OpenAI Platform](https://platform.openai.com/api-keys)
- Assurez-vous que votre compte a des crédits disponibles
- Vérifiez que la clé n'a pas expiré

#### **"Limite de taux dépassée"**
- Attendez quelques minutes avant de réessayer
- Vérifiez votre quota d'utilisation sur OpenAI Platform

#### **"Module 'openai' has no attribute 'error'"**
- Assurez-vous d'avoir installé la dernière version : `pip install --upgrade openai`
- La nouvelle version utilise `from openai import OpenAI` au lieu de `import openai`

### **Test de configuration :**
```bash
python test_openai.py
```

## 🔧 Personnalisation

### **Modification des questions**

Les questions sont maintenant organisées dans le dossier `questions/` :

- **`questions/public_cible.py`** : Questions pour l'étape 1 (Public Cible)
- **`questions/contraintes.py`** : Questions pour l'étape 2 (Contraintes Formation)  
- **`questions/scenario.py`** : Structure du scénario CMO

Chaque question peut être de type :
- `text` : Champ texte simple
- `textarea` : Zone de texte multiligne
- `radio` : Boutons radio (choix unique)
- `checkbox` : Cases à cocher (choix multiples)

Les questions radio peuvent inclure `text_input_options` pour afficher un champ texte supplémentaire selon la réponse.

### **Intégration GPT-5**

Pour intégrer une vraie API GPT-5, modifiez la fonction `generate_cmo_scenario_with_gpt()` dans `app.py`.

### **Avantages de cette organisation**

- **Modularité** : Chaque étape a ses propres questions dans un fichier séparé
- **Maintenabilité** : Plus facile de modifier les questions sans toucher au code principal
- **Réutilisabilité** : Les questions peuvent être importées dans d'autres modules
- **Clarté** : Structure claire et organisée du code 