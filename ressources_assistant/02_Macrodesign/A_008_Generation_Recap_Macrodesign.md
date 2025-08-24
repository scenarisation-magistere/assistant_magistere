# A_008 — Export du Macrodesign (Version GPT personnalisé — Export Markdown / CSV avec aperçu visuel intégré)

---

## 1️⃣ Partie **interne** — Logique pour l’assistant (invisible au participant)

> **IMPORTANT — Ces consignes sont destinées uniquement à l’assistant. Elles ne doivent jamais être affichées au participant.**

Assembler les **trois blocs YAML** validés (A_003, A_005, A_006, A_007) et produire un **APERÇU VISUEL LISIBLE** sous forme de **trois tableaux Markdown** dont les **en-têtes sont exactement** ceux ci-dessous (avec accents/espaces/parenthèses). Les exports **CSV** doivent **reprendre ces mêmes en-têtes lisibles** (séparateur `;`).  
> **Interdiction** : ne **pas** convertir les en-têtes en `snake_case`. Conserver **à l’identique** la casse, les accents, les espaces et les parenthèses.

### 📌 Règles générales
- Le **YAML est la source de vérité** (ne rien modifier).  
- Si un champ est manquant : **laisser `[ ]`** (ne pas inventer).  
- Respecter le scénario **CMO** (S1 à S8).  
- **Vérifications automatiques** (appliquées sur les données, pas sur les en-têtes) :
  - Concordance **compétences ↔ sections S2–S5** : `C1→S2`, `C2→S3`, `C3→S4`, `C4→S5`.  
  - S2–S5 : l’**intention ressource** doit être **« Acquisition »**.  
  - Référentiels : quantitatif ∈ {`25 %`,`50 %`,`75 %`,`100 %`}.  
- **Sorties supportées** dans ce prompt : **Markdown** (aperçu lisible) et **CSV** (en-têtes lisibles).  
- **XLSX/PDF** : réservés à la **version Guillaume** (environnement externe).

### 🔁 Flux d’exécution (interne)
1. Lire les **3 blocs YAML** (ci-dessous).  
2. Construire les **3 rendus lisibles** :
   - Feuille 1 : **tableau 2 colonnes** (clé/valeur) **dans cet ordre strict** :
     1. `titre`  
     2. `objectif_general`  
     3. `type_public`  
     4. `type_formation`  
     5. `niveau_scolaire`  
     6. `niveau_expertise`  
     7. `besoins_specifiques`  
     8. `nombre_participants`  
     9. `modalites_animation`  
     10. `exigences_restrictions`  
     11. `autre_element`  
     12. `competences_formulees` (afficher sous forme : `C1; C2; C3; C4`)  
   - Feuille 2 : **référentiels** avec en-têtes **lisibles** (voir « En-têtes lisibles à produire »).  
   - Feuille 3 : **macrodesign** avec en-têtes **lisibles** (voir « En-têtes lisibles à produire »).  
3. Afficher l’**aperçu visuel** (les 3 tableaux Markdown lisibles).  
4. Demander **validation**.  
5. Proposer **export** : **Markdown** (rendu tel quel) ou **CSV** (mêmes en-têtes lisibles).  
6. Produire **uniquement** l’export choisi.

### 🧭 En-têtes lisibles à produire (pour l’aperçu Markdown **et** le CSV)
- **Feuille 1 — Généralités (clé/valeur)**  
  `| Champ YAML | Valeur à saisir |`
- **Feuille 2 — Référentiels par section**  
  `| competence_id | competence_formulation [illustratif] | degre | libelle_degre | indicateur_qualitatif [illustratif] | indicateur_quantitatif |`
- **Feuille 3 — Contenus par section**  
  `| Section | Type de section | Compétence (id) | Compétence (formulation) | Ressource (type) | URL ressource | Intention ressource | Activité 1 (type) | URL activité 1 | Intention activité 1 | Activité 2 (type) | URL activité 2 | Intention activité 2 | Justification pédagogique | Modalité | Durée (min) | Évaluation |`

> **Notes d’assemblage** :  
> - **Feuille 1** : chaque clé YAML devient une **ligne** dans « Champ YAML », sa valeur normalisée dans « Valeur à saisir ».  
> - **Feuille 2** :  
>   - `competence_id`/`competence_formulation` proviennent de `referentiels_par_section`.  
>   - `degre` = 1..4 ; `libelle_degre` = {Je débute, Je progresse, Je suis autonome, Je maîtrise}.  
>   - `indicateur_quantitatif` = {25 %, 50 %, 75 %, 100 %}.  
>   - `indicateur_qualitatif [illustratif]` : reprendre le texte s’il existe, sinon `[ ]`.  
> - **Feuille 3** :  
>   - `Section` = S1..S8 ; `Type de section` ∈ {Accueil, Apprentissage, Classe virtuelle, Forum général, Évaluation finale}.  
>   - Pour S2..S5 : `Compétence (id)` = {C1..C4} mappée à la section, `Intention ressource` = **Acquisition**.  
>   - `Durée (min)` : S1=5, S2–S5=30, S6=60, S7/S8 = `[ ]` si non précisé. 
---

### 📦 Sources internes (YAML)
```yaml
#### 🔹 Bloc 1 — Généralités
    macrodesign_generalites:
      contexte_formation:
        titre: "[titre_formation]"
        objectif_general: "[objectif_general]"
      public_cible:
        type: [ "[type_de_public]" ]
        type_formation: "[type_formation]"
        niveau_scolaire: [ "[niveau_scolaire]" ]
        niveau_expertise: "[niveau_expertise]"
        besoins_specifiques: [ "[besoins_specifiques]" ]
        nombre_participants: "[nombre_participants]"
        modalites_animation: "[modalites_animation]"
        exigences_restrictions: "[exigences_restrictions]"
        autre_element: "[autre_element]"
      competences_formulees:
        - "[compétence 1]"
        - "[compétence 2]"
        - "[compétence 3]"
        - "[compétence 4]"

#### 🔹 Bloc 2 — Référentiels par section
    referentiels_par_section:
      - competence_id: "C1"
        competence_formulation: "[formulation compétence 1]"
        niveaux:
          - degre: 1
            libelle: "Je débute"
            indicateur_qualitatif: "[ ]"
            indicateur_quantitatif: "25 %"
          - degre: 2
            libelle: "Je progresse"
            indicateur_qualitatif: "[ ]"
            indicateur_quantitatif: "50 %"
          - degre: 3
            libelle: "Je suis autonome"
            indicateur_qualitatif: "[ ]"
            indicateur_quantitatif: "75 %"
          - degre: 4
            libelle: "Je maîtrise"
            indicateur_qualitatif: "[ ]"
            indicateur_quantitatif: "100 %"
      - competence_id: "C2"
        competence_formulation: "[formulation compétence 2]"
        niveaux: [ ... ]
      - competence_id: "C3"
        competence_formulation: "[formulation compétence 3]"
        niveaux: [ ... ]
      - competence_id: "C4"
        competence_formulation: "[formulation compétence 4]"
        niveaux: [ ... ]

#### 🔹 Bloc 3 — Contenus par section
    contenus_par_section:
      - section: S1
        type_section: Accueil
        ressource_type: "Page"
        intention_ressource: "Acquisition"
        justification: "Présentation générale, cadrage et attentes"
        modalite: "asynchrone"
        duree_min: 5
      - section: S2
        type_section: Apprentissage
        competence_id: "C1"
        competence_formulation: "[formulation C1]"
        ressource_type: "[ ]"
        intention_ressource: "Acquisition"
        activite_1_type: "[ ]"
        intention_activite_1: "[ ]"
        activite_2_type: "[ ]"
        intention_activite_2: "[ ]"
        justification: "[ ]"
        modalite: "asynchrone"
        duree_min: 30
        evaluation: "auto_evaluation_4_degres"
      - section: S3
        type_section: Apprentissage
        competence_id: "C2"
        competence_formulation: "[formulation C2]"
        ressource_type: "[ ]"
        intention_ressource: "Acquisition"
        activite_1_type: "[ ]"
        intention_activite_1: "[ ]"
        activite_2_type: "[ ]"
        intention_activite_2: "[ ]"
        justification: "[ ]"
        modalite: "asynchrone"
        duree_min: 30
        evaluation: "auto_evaluation_4_degres"
      - section: S4
        type_section: Apprentissage
        competence_id: "C3"
        competence_formulation: "[formulation C3]"
        ressource_type: "[ ]"
        intention_ressource: "Acquisition"
        activite_1_type: "[ ]"
        intention_activite_1: "[ ]"
        activite_2_type: "[ ]"
        intention_activite_2: "[ ]"
        justification: "[ ]"
        modalite: "asynchrone"
        duree_min: 30
        evaluation: "auto_evaluation_4_degres"
      - section: S5
        type_section: Apprentissage
        competence_id: "C4"
        competence_formulation: "[formulation C4]"
        ressource_type: "[ ]"
        intention_ressource: "Acquisition"
        activite_1_type: "[ ]"
        intention_activite_1: "[ ]"
        activite_2_type: "[ ]"
        intention_activite_2: "[ ]"
        justification: "[ ]"
        modalite: "asynchrone"
        duree_min: 30
        evaluation: "auto_evaluation_4_degres"
      - section: S6
        type_section: Classe virtuelle
        activite_1_type: "BigBlueButtonBN"
        intention_activite_1: "Discussion"
        justification: "Mise en pratique synchrone"
        modalite: "synchrone"
        duree_min: 60
      - section: S7
        type_section: Forum général
        activite_1_type: "Forum"
        intention_activite_1: "Discussion / Collaboration"
        justification: "Échanges libres et prolongés"
        modalite: "asynchrone"
        duree_min: "[ ]"
      - section: S8
        type_section: Évaluation finale
        activite_1_type: "Sondage Magistère"
        intention_activite_1: "Enquête"
        justification: "Évaluer la satisfaction et recueillir les perspectives"
        modalite: "asynchrone"
        duree_min: "[ ]"
        evaluation: "evaluation_satisfaction"
```
---

## 2️⃣ Partie **visible** — Interaction avec le participant

### 🧾 Étape 1 — Aperçu visuel (3 tableaux Markdown)

#### 🔹 Feuille 1 — Généralités
| Titre | Objectif général | Type public | Type formation | Niveau scolaire | Niveau expertise | Besoins spécifiques | Nb participants | Animation | Restrictions | Autre | Compétences formulées |
|-------|------------------|-------------|----------------|-----------------|------------------|---------------------|-----------------|-----------|--------------|-------|-----------------------|
| [titre] | [objectif_general] | [type_public] | [type_formation] | [niveau_scolaire] | [niveau_expertise] | [besoins_specifiques] | [nombre_participants] | [modalites_animation] | [exigences_restrictions] | [autre_element] | [C1; C2; C3; C4] |

#### 🔹 Feuille 2 — Référentiels par section
| Section | Compétence (id) | Formulation | Degré | Libellé | Indicateur qualitatif | Indicateur quantitatif |
|---------|-----------------|-------------|------:|---------|-----------------------|------------------------|
| S2 | C1 | [formulation C1] | 1 | Je débute | [ ] | 25 % |
| S2 | C1 | [formulation C1] | 2 | Je progresse | [ ] | 50 % |
| S2 | C1 | [formulation C1] | 3 | Je suis autonome | [ ] | 75 % |
| S2 | C1 | [formulation C1] | 4 | Je maîtrise | [ ] | 100 % |
| S3 | C2 | [formulation C2] | 1 | Je débute | [ ] | 25 % |
| … | … | … | … | … | … | … |

#### 🔹 Feuille 3 — Contenus par section
| Section | Type | Compétence (id + formulation) | Ressource | URL ressource | Int. ressource | Activité 1 | URL act. 1 | Int. act. 1 | Activité 2 | URL act. 2 | Int. act. 2 | Justification | Modalité | Durée (min) | Éval |
|---------|------|-------------------------------|-----------|---------------|----------------|------------|------------|-------------|------------|------------|-------------|--------------|----------|-------------|------|
| S1 | Accueil | — | Page | [ ] | Acquisition | — | — | — | — | — | — | Présentation générale, cadrage et attentes | asynchrone | 5 | — |
| S2 | Apprentissage | C1 — [formulation C1] | [ ] | [ ] | Acquisition | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | asynchrone | 30 | auto_eval |
| S3 | Apprentissage | C2 — [formulation C2] | [ ] | [ ] | Acquisition | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | asynchrone | 30 | auto_eval |
| S4 | Apprentissage | C3 — [formulation C3] | [ ] | [ ] | Acquisition | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | asynchrone | 30 | auto_eval |
| S5 | Apprentissage | C4 — [formulation C4] | [ ] | [ ] | Acquisition | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | asynchrone | 30 | auto_eval |
| S6 | Classe virtuelle | — | — | — | — | BigBlueButtonBN | [ ] | Discussion | — | — | — | Mise en pratique synchrone | synchrone | 60 | — |
| S7 | Forum général | — | — | — | — | Forum | [ ] | Discussion / Collaboration | — | — | — | Échanges libres et prolongés | asynchrone | [ ] | — |
| S8 | Évaluation finale | — | — | — | — | Sondage Magistère | [ ] | Enquête | — | — | — | Satisfaction et perspectives | asynchrone | [ ] | evaluation_satisfaction |

---

### 📝 Étape 2 — Validation
Souhaitez-vous **valider** ce macrodesign (aperçu visuel ci-dessus) ?  
**Réponse : [à compléter]**

---

### 📤 Étape 3 — Choix du format d’export
Quel format d’export souhaitez-vous ?  
- **Markdown** (lisible directement)  
- **CSV** (ouvert dans Excel / LibreOffice)  
- **XLSX** (fichier Excel multi-feuilles) — Version Guillaume uniquement
- **PDF** (A4, tableaux paginés) — Version Guillaume uniquement
**Réponse : [à compléter]**

---

## 📧 Référents académiques
- **DRANE — Laurent Castillo** — laurent.castillo@ac-toulouse.fr  
- **DRANE — Caroline Menanteau** — caroline.menanteau@ac-toulouse.fr  
- **EAFC — Laurence Graglia** — eafc-inge10@ac-toulouse.fr
