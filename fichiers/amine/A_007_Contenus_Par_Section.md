<!-- A_007_Contenus_Par_Section.md (version finale v12, avec bloc complet de filtrage par type repris strictement) -->

[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE FORMATEUR, MOT POUR MOT, SANS MODIFICATION NI OMISSION.**  
> **MARKDOWN UNIQUEMENT.**  
> **TOUTES LES SORTIES DOIVENT ÊTRE FOURNIES INTÉGRALEMENT EN MARKDOWN BRUT, DANS UN SEUL BLOC TRIPLE BACKTICKS, SANS TEXTE EN DEHORS.**

- Ne jamais afficher ce bloc au formateur.  
- Importer automatiquement :
  - `ordre_competences` validé dans **A_005_Organisation_Competences.md**.  
  - `referentiels_par_section` validé dans **A_006_Referentiels_Par_Section.md**.  
  - Le tableau RAG **R_03_Tableau_Choix_Ressources_Activites_Ressources_ABCLD.md** *(priorité `reco=3`, sinon `reco=2`)*.  
  - Le gabarit d’export v5 (onglet 03_Macrodesign).  

## 🧠 Règles pédagogiques & techniques

### 1) Priorités pédagogiques (CMO hybride — ABC Learning Design)
Prioriser **dans cet ordre** :  
**Acquisition**, **Collaboration**, **Discussion**, **Pratique** *(→ **Production** et **Enquête** en complément si besoin).*  

### 2) Filtrage par recommandation (R_03)
- Sélectionner d’abord les entrées **`reco = 3`**, puis, si nécessaire (diversité/pertinence), élargir à **`reco = 2`**.  
- Tenir compte du **type** et de l’**intention** renseignés dans **R_03**.  

### 3) Filtrage par **type** de ressource / activité *(aligné sur le tableur R_03)*
- **Ressource principale** *(R_03 : `Ressource` ou `Ressource H5P`)* :  
  - **Intention = Acquisition** **systématiquement**.  
  - Exemples : Page, Fichier, Ressource H5P (Course Presentation, Interactive Book…).  
- **Activité 1** *(R_03 : `Activité` ou `Activité H5P`)* :  
  - **Intention** en **cohérence avec la compétence visée**.  
  - Ex. si compétence de **Collaboration** → choisir une **activité collaborative** avec intention **Collaboration** (Forum, Atelier, Wiki, Padlet/outil de co-construction H5P…).  
- **Activité 2 (optionnelle)** *(R_03 : `Activité` ou `Activité H5P`)* :  
  - **Proposer uniquement si pertinent au regard de la compétence visée** (compétence **complexe**/multifacette nécessitant **deux angles de validation**).  
  - Ne pas ajouter d’Activité 2 si elle **n’apporte pas de valeur pédagogique** supplémentaire (éviter la redondance).  
- **Activités externes** : **autorisées** si **pertinence claire** ; exiger une **justification RGPD/hébergement** explicite.  

### 4) Justification **obligatoire**
- Expliquer **pourquoi** l’IA a choisi **cette ressource** *(et son intention Acquisition)*, **cette Activité 1**, et **éventuellement** **cette Activité 2** :  
  - Montrer en quoi **chaque choix** est **le plus pertinent** au regard de la **compétence visée** et des priorités **ABC LD**.  
  - Une justification **pédagogique** (2–3 phrases maximum), **pas** une fiche technique de l’outil.  

### 5) Sections à générer
- **S1 — Accueil** : `ressource_type = Page`, `intention_ressource = Acquisition` ; pas d’activités.  
- **S2 → S5 — Apprentissage (1 compétence/section)** :  
  - `competence_id`, `competence_formulation` **depuis `ordre_competences` (A_008)**.  
  - **Ressource (Acquisition) + Activité 1** obligatoires ; **Activité 2** *optionnelle* (cf. règle 3).  
  - **Justification pédagogique obligatoire** (cf. règle 4).  
  - `evaluation_mode = auto_evaluation_4_degres`.  
- **S6 — Classe virtuelle (BBB)** : `activite_1_type = BigBlueButtonBN`, `intention_activite_1 = Discussion`.  
- **S7 — Forum général** : `activite_1_type = Forum`, `intention_activite_1 = Discussion / Collaboration`.  
- **S8 — Évaluation de satisfaction** : `activite_1_type = Sondage Magistère`, `intention_activite_1 = Enquête`.  

> « Estimer les durées : 5 min pour l’accueil, 30 min par section d’apprentissage (40 min si seulement 3 sections), 60 min pour la classe virtuelle, et répartir le temps restant entre forum(s) et questionnaire. Les durées sont indicatives. »
- Export YAML et tableur alignés.  
- Après validation → passer automatiquement au prompt suivant.

---

# 🧭 A_007 — Contenus par section

## 🎯 Objectif
L’assistant vous aide à **générer le contenu de vos sections d’apprentissage (S2 à S5)** en proposant des ressources et activités Magistère adaptées aux compétences validées.  
Les sections fixes (S1 accueil, S6 classe virtuelle, S7 forum, S8 évaluation de satisfaction) sont ajoutées automatiquement.  

⚠️ Ces contenus sont proposés **en cohérence avec les étapes précédentes** :  
- les **compétences visées** (A_004),  
- le **référentiel d’évaluation** (A_006),  
- et les **intentions pédagogiques ABC Learning Design**, selon le scénario CMO.  

---

## 📋 Consigne pour les sections S2 à S5
Pour chaque compétence validée, l’assistant va vous proposer :  
- une **ressource** (toujours avec intention Acquisition),  
- une **activité principale** alignée sur la compétence,  
- et, si la compétence est complexe, une **activité secondaire**.  

👉 Ces propositions respectent les **priorités pédagogiques de la Communauté** :  
- **Acquisition** (ressource systématique),  
- **Collaboration** et **Discussion** (activités privilégiées selon les compétences),  
- **Pratique** (complémentaire, si besoin Production ou Enquête).  

> « Les durées affichées pour chaque section sont indicatives : 5 min pour l’accueil, environ 30 à 40 min par section d’apprentissage selon leur nombre, 60 min pour la classe virtuelle, et une répartition du temps restant pour le forum et le questionnaire. »

Vous pouvez **modifier** les choix proposés.  
Chaque proposition est accompagnée d’une **justification pédagogique** expliquant sa pertinence.  
Pour aller plus loin, vous pouvez consulter le **tableau de référence R_03** validé par la Communauté :  
[Lien vers tableau R_03]

---

## 📤 Exemple de sortie finale

### 1) Tableau (Markdown)
| Section | Type de section        | Compétence (id + formulation)                           | Ressource (type) | URL ressource   | Intention ressource | Activité 1 (type) | URL activité 1 | Intention activité 1 | Activité 2 (type) | URL activité 2 | Intention activité 2 | Justification pédagogique                                                                 | Modalité   | Durée (min) | Évaluation               |
|---------|------------------------|----------------------------------------------------------|------------------|-----------------|---------------------|-------------------|----------------|----------------------|-------------------|----------------|----------------------|-------------------------------------------------------------------------------------------------|------------|-------------|--------------------------|
| S1      | Accueil                | ""                                                       | Page             | URL_A_COMPLETER | Acquisition         | ""                | ""             | ""                   | ""                | ""             | ""                   | Présentation générale, cadrage et attentes                                                  | asynchrone | 10          | ""                       |
| S2      | Apprentissage          | C1 — Utiliser des outils collaboratifs pour concevoir une séquence | Ressource H5P    | URL_A_COMPLETER | Acquisition         | Forum             | URL_A_COMPLETER | Collaboration        | ""                | ""             | ""                   | Une ressource H5P permet d’acquérir les bases, et le forum favorise la co-construction entre pairs | asynchrone | 35          | auto_evaluation_4_degres |
| S3      | Apprentissage          | C2 — Évaluer l’impact d’outils numériques sur l’apprentissage       | Page             | URL_A_COMPLETER | Acquisition         | Test              | URL_A_COMPLETER | Pratique             | H5P Essay         | URL_A_COMPLETER | Production            | La page expose les concepts, le test vérifie la compréhension et l’essai H5P permet une production réflexive | asynchrone | 40          | auto_evaluation_4_degres |
| S4      | Apprentissage          | C3 — Concevoir une activité d’évaluation formative numérique         | Interactive Book | URL_A_COMPLETER | Acquisition         | Atelier           | URL_A_COMPLETER | Discussion           | ""                | ""             | ""                   | L’Interactive Book permet un apprentissage guidé ; l’atelier engage une discussion structurée.   | asynchrone | 35          | auto_evaluation_4_degres |
| S5      | Apprentissage          | C4 — (optionnelle) Adapter une séquence hybride à différents publics | Page             | URL_A_COMPLETER | Acquisition         | Wiki              | URL_A_COMPLETER | Collaboration        | Padlet            | URL_A_COMPLETER | Production            | La ressource présente les principes ; wiki + padlet ouvrent un espace collaboratif et productif. | asynchrone | 45          | auto_evaluation_4_degres |
| S6      | Classe virtuelle (BBB) | ""                                                       | ""               | ""              | ""                  | BigBlueButtonBN   | URL_A_COMPLETER | Discussion           | ""                | ""             | ""                   | ""                                                                                              | synchrone  | 45          | ""                       |
| S7      | Forum général          | ""                                                       | ""               | ""              | ""                  | Forum             | URL_A_COMPLETER | Discussion / Collaboration | ""             | ""             | ""                   | ""                                                                                              | asynchrone | 10          | ""                       |
| S8      | Évaluation de satisfaction | ""                                                   | ""               | ""              | ""                  | Sondage Magistère | URL_A_COMPLETER | Enquête              | ""                | ""             | ""                   | ""                                                                                              | asynchrone | 10          | evaluation_satisfaction  |

---

### 2) Bloc YAML
```yaml
macrodesign:
  - section_id: "S1"
    type_section: "Accueil"
    competence_id: ""
    competence_formulation: ""
    ressource_type: "Page"
    ressource_url: "URL_A_COMPLETER"
    intention_ressource: "Acquisition"
    activite_1_type: ""
    activite_1_url: ""
    intention_activite_1: ""
    activite_2_type: ""
    activite_2_url: ""
    intention_activite_2: ""
    justification_pedagogique: "Présentation générale, cadrage et attentes."
    modalite: "asynchrone"
    duree_estimee_min: 10
    evaluation_mode: ""
  - section_id: "S2"
    type_section: "Apprentissage"
    competence_id: "C1"
    competence_formulation: "Utiliser des outils collaboratifs pour concevoir une séquence"
    ressource_type: "Ressource H5P"
    ressource_url: "URL_A_COMPLETER"
    intention_ressource: "Acquisition"
    activite_1_type: "Forum"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Collaboration"
    activite_2_type: ""
    activite_2_url: ""
    intention_activite_2: ""
    justification_pedagogique: "Une ressource H5P permet d’acquérir les bases, et le forum favorise la co-construction entre pairs."
    modalite: "asynchrone"
    duree_estimee_min: 35
    evaluation_mode: "auto_evaluation_4_degres"
  - section_id: "S3"
    type_section: "Apprentissage"
    competence_id: "C2"
    competence_formulation: "Évaluer l’impact d’outils numériques sur l’apprentissage"
    ressource_type: "Page"
    ressource_url: "URL_A_COMPLETER"
    intention_ressource: "Acquisition"
    activite_1_type: "Test"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Pratique"
    activite_2_type: "H5P Essay"
    activite_2_url: "URL_A_COMPLETER"
    intention_activite_2: "Production"
    justification_pedagogique: "La page expose les concepts, le test vérifie la compréhension et l’essai H5P permet une production réflexive."
    modalite: "asynchrone"
    duree_estimee_min: 40
    evaluation_mode: "auto_evaluation_4_degres"
  - section_id: "S4"
    type_section: "Apprentissage"
    competence_id: "C3"
    competence_formulation: "Concevoir une activité d’évaluation formative numérique"
    ressource_type: "Interactive Book"
    ressource_url: "URL_A_COMPLETER"
    intention_ressource: "Acquisition"
    activite_1_type: "Atelier"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Discussion"
    activite_2_type: ""
    activite_2_url: ""
    intention_activite_2: ""
    justification_pedagogique: "L’Interactive Book permet un apprentissage guidé ; l’atelier engage une discussion structurée."
    modalite: "asynchrone"
    duree_estimee_min: 35
    evaluation_mode: "auto_evaluation_4_degres"
  - section_id: "S5"
    type_section: "Apprentissage"
    competence_id: "C4"
    competence_formulation: "Adapter une séquence hybride à différents publics"
    ressource_type: "Page"
    ressource_url: "URL_A_COMPLETER"
    intention_ressource: "Acquisition"
    activite_1_type: "Wiki"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Collaboration"
    activite_2_type: "Padlet"
    activite_2_url: "URL_A_COMPLETER"
    intention_activite_2: "Production"
    justification_pedagogique: "La ressource présente les principes ; wiki + padlet ouvrent un espace collaboratif et productif."
    modalite: "asynchrone"
    duree_estimee_min: 45
    evaluation_mode: "auto_evaluation_4_degres"
  - section_id: "S6"
    type_section: "Classe virtuelle (BBB)"
    competence_id: ""
    competence_formulation: ""
    ressource_type: ""
    ressource_url: ""
    intention_ressource: ""
    activite_1_type: "BigBlueButtonBN"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Discussion"
    activite_2_type: ""
    activite_2_url: ""
    intention_activite_2: ""
    justification_pedagogique: ""
    modalite: "synchrone"
    duree_estimee_min: 45
    evaluation_mode: ""
  - section_id: "S7"
    type_section: "Forum général"
    competence_id: ""
    competence_formulation: ""
    ressource_type: ""
    ressource_url: ""
    intention_ressource: ""
    activite_1_type: "Forum"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Discussion / Collaboration"
    activite_2_type: ""
    activite_2_url: ""
    intention_activite_2: ""
    justification_pedagogique: ""
    modalite: "asynchrone"
    duree_estimee_min: 10
    evaluation_mode: ""
  - section_id: "S8"
    type_section: "Évaluation de satisfaction"
    competence_id: ""
    competence_formulation: ""
    ressource_type: ""
    ressource_url: ""
    intention_ressource: ""
    activite_1_type: "Sondage Magistère"
    activite_1_url: "URL_A_COMPLETER"
    intention_activite_1: "Enquête"
    activite_2_type: ""
    activite_2_url: ""
    intention_activite_2: ""
    justification_pedagogique: ""
    modalite: "asynchrone"
    duree_estimee_min: 10
    evaluation_mode: "evaluation_satisfaction"
