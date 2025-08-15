<!-- A_010_Contenus_Par_Section.md -->

[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**  
> **TOUTES LES RÉPONSES DOIVENT ÊTRE FOURNIES INTÉGRALEMENT EN MARKDOWN BRUT, DANS UN SEUL BLOC TRIPLE BACKTICKS, SANS TEXTE EN DEHORS.**

---

## BUT TECHNIQUE
Générer automatiquement, pour les sections S2 à S5, un tableau complet des contenus pédagogiques à partir :  
- du bloc `ordre_competences` validé (A_008_Organisation_Competences.md),  
- du fichier Markdown `R_03_Tableau_Activites_Ressources.md` (col.1 = id, col.2 = type, col.3 = nom, col.4 = recommandation),  
- des règles ABC Learning Design définies ci-dessous.

---

## RÈGLES DE FILTRAGE ET DE SÉLECTION PÉDAGOGIQUE

1. **Priorité pédagogique générale**  
   - Privilégier : **Acquisition**, **Collaboration**, **Discussion**, **Pratique**.  
   - **Production** et **Enquête** restent présentes mais de façon secondaire.

2. **Filtrage par recommandation et compétences visées**  
   - Priorité aux entrées avec `recommandation = 3`.  
   - Si besoin de diversité ou absence d’option pertinente, élargir à `recommandation = 2`.  
   - Tenir compte du type de **compétences visées** pour aligner le choix sur le scénario CMO et les intentions ABC Learning Design.  
   - Déterminer l’intention des ressources et activités à partir de la formulation de la compétence ou des verbes d’action :  
     - **Acquisition** → mémoriser, identifier, définir, comprendre  
     - **Entraînement** → appliquer, s’entraîner, mettre en œuvre  
     - **Production** → réaliser, produire, concevoir  
     - **Discussion** → discuter, argumenter, échanger, analyser un point de vue  
     - **Collaboration** → coopérer, co-construire, travailler en groupe  
     - **Enquête** → explorer, enquêter, rechercher

3. **Filtrage par type de ressource ou activité**  
   - **Ressource principale** : `Ressource` ou `Ressource H5P` avec intention **Acquisition**.  
   - **Activité 1** : `Activité` ou `Activité H5P`, intention en cohérence avec la compétence visée.  
   - **Activité 2** (optionnelle) : uniquement si valeur ajoutée pédagogique et intention complémentaire.  
   - **Activités externes** autorisées si pertinence claire, avec justification RGPD/hébergement si nécessaire.

4. **Justification obligatoire**  
   - Expliquer la pertinence pédagogique des activités par rapport à la compétence et au modèle ABC Learning Design.

---

## FORMAT DE SORTIE

- L’assistant produit **uniquement** un tableau Markdown brut dans un seul bloc triple backticks, puis un bloc YAML reprenant exactement les données du tableau.
- Colonnes du tableau (ordre fixe) :  
  | Section | Type de section | Compétences visées | Ressource | Intention ressource | Activité 1 | Intention activité 1 | Activité 2 | Intention activité 2 | Justification activité(s) |

**Règles de remplissage** :  
- **S1 – Accueil** : Type = Accueil, autres colonnes null.  
- **S2 à S5 – Apprentissage** :  
  - Compétences visées = depuis `ordre_competences` (A_008).  
  - Ressource, activités et intentions = selon règles ci-dessus.  
  - Justification = obligatoire pour activités.  
- **S6 – Classe virtuelle (BBB)** : Activité 1 = BigBlueButtonBN, Intention = Discussion.  
- **S7 – Forum général** : Activité 1 = Forum, Intention = Discussion / Collaboration.  
- **S8 – Évaluation** : Activité 1 = Sondage Magistère, Intention = Enquête.

---

### Exemple de tableau attendu :

```markdown
| Section | Type de section        | Compétences visées*                                     | Ressource | Intention ressource | Activité 1         | Intention activité 1 | Activité 2 | Intention activité 2 | Justification activité(s) |
|---------|------------------------|---------------------------------------------------------|-----------|---------------------|--------------------|----------------------|------------|----------------------|---------------------------|
| 1       | Accueil                | null                                                    | null      | null                | null               | null                 | null       | null                 | null                      |
| 2       | Apprentissage          | [Compétence 1 – A_008]                                  | Page      | Acquisition         | [Activité choisie] | [Intention dérivée]  | [Option]   | [Intention]          | [Justification]           |
| 3       | Apprentissage          | [Compétence 2 – A_008]                                  | Page      | Acquisition         | ...                | ...                  | ...        | ...                  | ...                       |
| 4       | Apprentissage          | [Compétence 3 – A_008]                                  | Page      | Acquisition         | ...                | ...                  | ...        | ...                  | ...                       |
| 5       | Apprentissage          | [Compétence 4 – A_008]                                  | Page      | Acquisition         | ...                | ...                  | ...        | ...                  | ...                       |
| 6       | Classe virtuelle (BBB) | null                                                    | null      | null                | BigBlueButtonBN    | Discussion           | null       | null                 | null                      |
| 7       | Forum général          | null                                                    | null      | null                | Forum              | Discussion / Collaboration | null | null                 | null                      |
| 8       | Évaluation             | null                                                    | null      | null                | Sondage Magistère  | Enquête              | null       | null                 | null                      |

```yaml
contenus_par_section:
  - section: 1
    type_section: Accueil
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: null
    intention_activite_1: null
    activite_2: null
    intention_activite_2: null
    justification: null
  - section: 2
    type_section: Apprentissage
    competence_visee: [Compétence 1 – A_008]
    ressource: Page
    intention_ressource: Acquisition
    activite_1: ...
    intention_activite_1: ...
    activite_2: ...
    intention_activite_2: ...
    justification: ...
  - section: 3
    type_section: Apprentissage
    competence_visee: [Compétence 2 – A_008]
    ressource: Page
    intention_ressource: Acquisition
    activite_1: ...
    intention_activite_1: ...
    activite_2: ...
    intention_activite_2: ...
    justification: ...
  - section: 4
    type_section: Apprentissage
    competence_visee: [Compétence 3 – A_008]
    ressource: Page
    intention_ressource: Acquisition
    activite_1: ...
    intention_activite_1: ...
    activite_2: ...
    intention_activite_2: ...
    justification: ...
  - section: 5
    type_section: Apprentissage
    competence_visee: [Compétence 4 – A_008]
    ressource: Page
    intention_ressource: Acquisition
    activite_1: ...
    intention_activite_1: ...
    activite_2: ...
    intention_activite_2: ...
    justification: ...
  - section: 6
    type_section: Classe virtuelle (BBB)
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: BigBlueButtonBN
    intention_activite_1: Discussion
    activite_2: null
    intention_activite_2: null
    justification: null
  - section: 7
    type_section: Forum général
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: Forum
    intention_activite_1: Discussion / Collaboration
    activite_2: null
    intention_activite_2: null
    justification: null
  - section: 8
    type_section: Évaluation
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: Sondage Magistère
    intention_activite_1: Enquête
    activite_2: null
    intention_activite_2: null
    justification: null
```

---

Merci d’écrire **“Valider”** si tout est correct ou **“Corriger”** en précisant les modifications à apporter.  
**Réponse : [à compléter]**

---

## 📚 Pour aller plus loin
Si vous souhaitez consulter **l’ensemble des activités et ressources compatibles avec Magistère** (y compris celles qui ne figurent pas dans la proposition ci-dessus), vous pouvez accéder à la base complète ici :  
[📂 Catalogue Activités & Ressources — Magistère](https://nuage02.apps.education.fr/index.php/s/8TZDK9gYr7nZ4EH)  

> Vous pouvez vous en inspirer pour proposer des ajustements ou variantes, mais gardez en tête que la sélection ci-dessus respecte déjà les règles pédagogiques et techniques du scénario CMO.
