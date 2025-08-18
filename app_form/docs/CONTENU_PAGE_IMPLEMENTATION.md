# Page Contenu - Implémentation

## Vue d'ensemble

La page **Contenus par Section** est la 5ème étape du processus de création de formation. Elle utilise l'IA pour générer automatiquement les contenus pédagogiques pour chaque compétence selon les règles ABC Learning Design définies dans le prompt `A_010_Contenus_Par_Section.md`.

## Fonctionnalités

### 🎯 Génération IA des Contenus
- Analyse automatique des compétences définies dans l'étape précédente
- Génération de contenus selon les règles ABC Learning Design
- Utilisation des ressources RAG pour la sélection d'activités et ressources
- Filtrage par recommandation et pertinence pédagogique

### 📋 Slider Compétence par Compétence
- Interface de navigation entre les compétences
- Affichage des contenus suggérés pour chaque compétence
- Sélection interactive des contenus les plus appropriés
- Visualisation des résultats en temps réel

### 📊 Tableau des Sections
- Génération automatique du tableau complet des sections (S1 à S8)
- Respect du format défini dans le prompt A_010
- Affichage des ressources, activités et intentions
- Justifications pédagogiques pour chaque sélection

## Architecture Technique

### Frontend (`templates/contenu.html`)
- Interface utilisateur moderne et responsive
- Slider de navigation entre compétences
- Grille de sélection des contenus
- Tableaux de résultats dynamiques
- Gestion des états de chargement et d'erreur

### Backend (`routes/contenu.py`)
- Routes pour la génération IA des contenus
- Intégration avec le système d'IA existant
- Parsing des réponses IA selon le format YAML
- Sauvegarde des données dans le fichier YAML de session

### IA (`ai_helpers.py`)
- Fonction `generate_ai_response()` pour l'appel à l'API OpenAI
- Prompt spécialisé selon les règles du document A_010
- Gestion des erreurs et fallback vers des données mock

## Règles de Génération

### Priorités Pédagogiques
1. **Acquisition** - mémoriser, identifier, définir, comprendre
2. **Collaboration** - coopérer, co-construire, travailler en groupe
3. **Discussion** - discuter, argumenter, échanger, analyser
4. **Pratique** - appliquer, s'entraîner, mettre en œuvre
5. **Production** - réaliser, produire, concevoir (secondaire)
6. **Enquête** - explorer, enquêter, rechercher (secondaire)

### Filtrage par Recommandation
- **Priorité 1** : Recommandation = 3 (très recommandé)
- **Priorité 2** : Recommandation = 2 (recommandé)
- **Priorité 3** : Recommandation = 1 (optionnel)

### Types de Contenus
- **Ressource principale** : Page ou Ressource H5P (intention Acquisition)
- **Activité 1** : Activité ou Activité H5P (intention selon compétence)
- **Activité 2** : Optionnelle, intention complémentaire

## Structure des Sections

### S1 - Accueil
- Type : Accueil
- Pas de compétence associée
- Pas de contenu pédagogique

### S2-S5 - Apprentissage
- Type : Apprentissage
- Une compétence par section
- Ressource + Activité(s) selon sélection utilisateur

### S6 - Classe Virtuelle
- Type : Classe virtuelle (BBB)
- Activité : BigBlueButtonBN
- Intention : Discussion

### S7 - Forum Général
- Type : Forum général
- Activité : Forum
- Intention : Discussion / Collaboration

### S8 - Évaluation
- Type : Évaluation
- Activité : Sondage Magistère
- Intention : Enquête

## Format de Données

### Entrée (Compétences)
```yaml
ordre_competences:
  - code: "C1"
    formulation: "C1 - Identifier les concepts clés"
  - code: "C2"
    formulation: "C2 - Appliquer les méthodes"
```

### Sortie (Contenus)
```yaml
contenus_par_section:
  - section: 1
    type_section: "Accueil"
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: null
    intention_activite_1: null
    activite_2: null
    intention_activite_2: null
    justification: null
  - section: 2
    type_section: "Apprentissage"
    competence_visee: "C1 - Identifier les concepts clés"
    ressource: "Page de contenu"
    intention_ressource: "Acquisition"
    activite_1: "Quiz interactif"
    intention_activite_1: "Pratique"
    activite_2: null
    intention_activite_2: null
    justification: "Sélection basée sur la pertinence pédagogique"
```

## Workflow Utilisateur

1. **Accès à la page** : Après avoir complété l'étape Référentiels
2. **Génération IA** : Clic sur "Générer les Contenus"
3. **Navigation** : Utilisation des boutons Précédent/Suivant
4. **Sélection** : Clic sur les contenus souhaités pour chaque compétence
5. **Validation** : Clic sur "Valider et Continuer"

## Tests

Le fichier `test_contenu_page.py` contient des tests pour :
- Extraction des codes de compétence
- Génération de contenus mock
- Parsing des réponses IA
- Workflow complet de génération

### Exécution des tests
```bash
cd app_form
python test_contenu_page.py
```

## Intégration

### Navigation
- Ajout dans `config/pages_config.py` (étape 5)
- Mise à jour du nombre total d'étapes (5 au lieu de 4)
- Configuration des routes précédente/suivante

### Routes
- `/contenu` : Page principale
- `/get_competences_data` : API pour récupérer les compétences
- `/generate_contenus` : API pour générer les contenus
- `/save_contenus` : API pour sauvegarder les résultats

### Dépendances
- `ai_helpers.py` : Fonctions d'IA
- `routes/contenu.py` : Routes spécifiques
- `templates/contenu.html` : Interface utilisateur
- Ressources RAG : `ressources_RAG/03_Outils_de_scénarisation/R_03_Tableau_Activites_Ressources.md`

## Améliorations Futures

1. **Interface plus riche** : Ajout de filtres et de tri
2. **Personnalisation** : Possibilité de modifier les contenus générés
3. **Prévisualisation** : Aperçu des contenus avant validation
4. **Export** : Génération de documents PDF ou Word
5. **Historique** : Sauvegarde des versions précédentes

## Dépannage

### Erreurs courantes
- **Aucune compétence trouvée** : Vérifier que l'étape Compétences est complétée
- **Erreur IA** : Vérifier la configuration OpenAI dans `.env`
- **Fichier RAG manquant** : Vérifier la présence du fichier `R_03_Tableau_Activites_Ressources.md`

### Logs
Les erreurs sont loggées dans la console et affichées à l'utilisateur via des messages d'erreur.
