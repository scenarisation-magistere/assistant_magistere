# A_011 — Génération du récapitulatif de Macrodesign

---

## 1️⃣ [INSTRUCTION_ASSISTANT] — Logique interne (technique, invisible participant)

- **But** : Assembler et afficher le récapitulatif complet du **macrodesign** à partir :
  - des fichiers validés :  
    **A_004_Public_Cible.md**, **A_005_Contraintes_Formation.md**, **A_006_Scenario_CMO.md**,  
    **A_007_Competences_Visees.md**, **A_008_Organisation_Competences.md**,  
    **A_009_Referentiels_Par_Section.md**, **A_010_Contenus_Par_Section.md** ;
  - du bloc `ordre_competences` (issu de **A_008**) ;
  - du bloc `contenus_par_section` (issu de **A_010**).

- **Sorties attendues à afficher au participant (dans l’ordre)** :
  1) Bloc YAML **`macrodesign_generalites`** — version de référence à conserver ;
  2) Bloc YAML **`contenus_par_section`** — report conforme à A_010 ;
  3) Question : **« Quel format d’export souhaitez-vous ? — [Markdown / CSV] »** ;
  4) Afficher **uniquement** l’export choisi (Markdown **ou** CSV), rempli avec les données validées ;
  5) Rappel en fin d’export : **référents académiques** + message « microdesign : import du YAML ».

- **Règles générales** :
  - Ne **pas modifier** de contenu validé ; seulement **assembler** et **normaliser**.
  - Si un champ manque : laisser des crochets `[ ]` (ne pas inventer).
  - Respecter le scénario **CMO** (8 sections) et la nomenclature d’**A_010**.
  - Le **YAML** est la **source de vérité** pour la suite (microdesign + implémentation Magistère).
  - Les **templates d’export** ci-dessous sont **invisibles** au participant : ne les afficher **que** une fois **remplis** selon le format choisi.

- **Vérifications automatiques (avant export)** :
  - Concordance **compétences ↔ sections S2–S5** ;
  - Présence de l’intention **« Acquisition »** dans S2–S5 (au moins pour la ressource) ;
  - Présence d’un **badge** standard (critères) pour S2–S5 dans les référentiels.

- **Variables internes** :
  - `yaml_generalites`, `yaml_contenus` (concaténation/disponibilité pour exports)
  - `choix_export` ∈ {`markdown`, `csv`}

---

### 📦 Templates d’export (INVISIBLES — à utiliser pour générer la sortie choisie)

#### 🔹 Template Markdown — Feuille 1 (Généralités)
[TEMPLATE_MARKDOWN_FEUILLE_1]
| titre_formation | public_type | public_profil | public_niveau | besoins_spec1 | besoins_spec2 | type_parcours | hybridation | temps_total | autonomie | animation | calendrier | horaires | nb_participants |
| [titre] | [public_type] | [public_profil] | [public_niveau] | [b1] | [b2] | [type_parcours] | [hybridation] | [temps_total] | [autonomie] | [animation] | [calendrier] | [horaires] | [nb] |

#### 🔹 Template Markdown — Feuille 2 (Sections)
[TEMPLATE_MARKDOWN_FEUILLE_2]
| section | titre | competence | intentions | ressource | activite_1 | activite_2 | discussion | badge | modalite |
| 1 | Bienvenue dans la formation |  | Acquisition | Page d’accueil |  |  | Présentation du parcours, modalités, contacts |  | Asynchrone |
| 2 | [s2_titre] | [s2_comp] | Acquisition;[s2_int2] | [s2_ress] | [s2_act1] | [s2_act2] | [s2_disc] | Réussite si atteinte du degré 3 | Asynchrone |
| 3 | [s3_titre] | [s3_comp] | Acquisition;[s3_int2] | [s3_ress] | [s3_act1] | [s3_act2] | [s3_disc] | Réussite si atteinte du degré 3 | Asynchrone |
| 4 | [s4_titre] | [s4_comp] | Acquisition;[s4_int2] | [s4_ress] | [s4_act1] | [s4_act2] | [s4_disc] | Réussite si atteinte du degré 3 | Asynchrone |
| 5 | [s5_titre] | [s5_comp] | Acquisition;[s5_int2] | [s5_ress] | [s5_act1] | [s5_act2] | [s5_disc] | Réussite si atteinte du degré 3 | Asynchrone |
| 6 | Classe virtuelle – mise en pratique |  | Collaboration | Lien vers classe virtuelle (BBB) |  |  |  |  | Synchrone |
| 7 | Forum général – échanges libres |  | Discussion;Collaboration |  | Forum |  | Fils issus des discussions des sections S2 à S5 |  | Asynchrone |
| 8 | Évaluation finale et perspectives |  | Enquête | Sondage Magistère |  |  | Questionnaire de satisfaction à 3 temporalités |  | Asynchrone |

#### 🔹 Template CSV — Généralités
[TEMPLATE_CSV_GENERALITES]
titre_formation;public_type;public_profil;public_niveau;besoins_spec1;besoins_spec2;type_parcours;hybridation;temps_total;autonomie;animation;calendrier;horaires;nb_participants
[titre];[public_type];[public_profil];[public_niveau];[b1];[b2];[type_parcours];[hybridation];[temps_total];[autonomie];[animation];[calendrier];[horaires];[nb]

#### 🔹 Template CSV — Sections
[TEMPLATE_CSV_SECTIONS]
section;titre;competence;intentions;ressource;activite_1;activite_2;discussion;badge;modalite
1;Bienvenue dans la formation;;Acquisition;Page d’accueil;;;Présentation du parcours, modalités, contacts;;Asynchrone
2;[s2_titre];[s2_comp];Acquisition;[s2_int2];[s2_ress];[s2_act1];[s2_act2];[s2_disc];Réussite si atteinte du degré 3;Asynchrone
3;[s3_titre];[s3_comp];Acquisition;[s3_int2];[s3_ress];[s3_act1];[s3_act2];[s3_disc];Réussite si atteinte du degré 3;Asynchrone
4;[s4_titre];[s4_comp];Acquisition;[s4_int2];[s4_ress];[s4_act1];[s4_act2];[s4_disc];Réussite si atteinte du degré 3;Asynchrone
5;[s5_titre];[s5_comp];Acquisition;[s5_int2];[s5_ress];[s5_act1];[s5_act2];[s5_disc];Réussite si atteinte du degré 3;Asynchrone
6;Classe virtuelle – mise en pratique;;Collaboration;Lien vers classe virtuelle (BBB);;;;;Synchrone
7;Forum général – échanges libres;;Discussion;Collaboration;;Forum;;Fils issus des discussions des sections S2 à S5;;Asynchrone
8;Évaluation finale et perspectives;;Enquête;Sondage Magistère;;;;Questionnaire de satisfaction à 3 temporalités;;Asynchrone

> **IMPORTANT (rendu)** : ces templates **ne doivent jamais être affichés bruts**. Le participant ne voit **que** :  
> (a) les deux blocs YAML ci-dessous, puis (b) l’export **rempli** selon son choix.

---

## 2️⃣ Partie visible — Échanges pédagogiques avec le participant

### 🎯 Rappel d’usage
- Le **fichier YAML** est la **version de référence** : conservez-le pour le **microdesign** et l’**implémentation Magistère** (les prochains prompts vous y guideront).
- La **version CSV** sert surtout au **partage/échanges** avec d’autres formateurs.

---

### 🧾 Étape 1 — Votre macrodesign (deux blocs YAML prêts à l’export)

#### 📦 Bloc 1 — Généralités (référentiel complet inclus)
```yaml
macrodesign_generalites:
  titre_formation: "[ ]"
  public_cible:
    type: "[ ]"            # ex. enseignants / formateurs / autres
    profil: "[ ]"          # ex. homogène / hétérogène
    niveau_expertise: "[ ]" # ex. débutant / intermédiaire / avancé
    besoins_specifiques:
      - "[ ]"
      - "[ ]"
  contraintes_formation:
    type_parcours: "[ ]"   # ex. création / migration
    hybridation: "[ ]"     # ex. asynchrone (majeure) + synchrone (mineure)
    temps_total: "[ ]"     # ex. moins de 3h
    autonomie: "[ ]"       # ex. formation tutorée
    animation: "[ ]"       # ex. individuelle / coanimée
    calendrier: "[ ]"
    horaires: "[ ]"
    nombre_participants: "[ ]"
  scenario_hybride:
    reference: "CMO"
    structure:
      - Accueil
      - Apprentissage 1
      - Apprentissage 2
      - Apprentissage 3
      - Apprentissage 4
      - Classe virtuelle
      - Forum général
      - Évaluation finale
  competences_visees:
    - id: "[c1_id]"
      formulation: "[formulation compétence 1]"
    - id: "[c2_id]"
      formulation: "[formulation compétence 2]"
    - id: "[c3_id]"
      formulation: "[formulation compétence 3]"
    - id: "[c4_id]"
      formulation: "[formulation compétence 4]"
  referentiels_autoevaluation_complet:
    - section: 2
      competence_id: "[c1_id]"
      competence: "[formulation compétence 1]"
      niveaux:
        - niveau: 1
          label: "[ ]"
          indicateurs:
            - "[ ]"
            - "[ ]"
        - niveau: 2
          label: "[ ]"
          indicateurs:
            - "[ ]"
            - "[ ]"
        - niveau: 3
          label: "[ ]"
          indicateurs:
            - "[ ]"
            - "[ ]"
        - niveau: 4
          label: "[ ]"
          indicateurs:
            - "[ ]"
            - "[ ]"
      badge_criteres: "[ ]"
      modalites_preuve: "[ ]"
    - section: 3
      competence_id: "[c2_id]"
      competence: "[formulation compétence 2]"
      niveaux:
        - niveau: 1
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 2
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 3
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 4
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
      badge_criteres: "[ ]"
      modalites_preuve: "[ ]"
    - section: 4
      competence_id: "[c3_id]"
      competence: "[formulation compétence 3]"
      niveaux:
        - niveau: 1
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 2
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 3
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 4
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
      badge_criteres: "[ ]"
      modalites_preuve: "[ ]"
    - section: 5
      competence_id: "[c4_id]"
      competence: "[formulation compétence 4]"
      niveaux:
        - niveau: 1
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 2
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 3
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
        - niveau: 4
          label: "[ ]"
          indicateurs: ["[ ]","[ ]"]
      badge_criteres: "[ ]"
      modalites_preuve: "[ ]"


#### 📦 Bloc 2 — Contenus par section
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
    competence_visee: "[Compétence 1 – A_008]"
    ressource: "Page"
    intention_ressource: "Acquisition"
    activite_1: "[activité 1 section 2]"
    intention_activite_1: "[intention dérivée]"
    activite_2: "[activité 2 section 2]"
    intention_activite_2: "[intention dérivée]"
    justification: "[justification]"

  - section: 3
    type_section: Apprentissage
    competence_visee: "[Compétence 2 – A_008]"
    ressource: "Page"
    intention_ressource: "Acquisition"
    activite_1: "[activité 1 section 3]"
    intention_activite_1: "[intention dérivée]"
    activite_2: "[activité 2 section 3]"
    intention_activite_2: "[intention dérivée]"
    justification: "[justification]"

  - section: 4
    type_section: Apprentissage
    competence_visee: "[Compétence 3 – A_008]"
    ressource: "Page"
    intention_ressource: "Acquisition"
    activite_1: "[activité 1 section 4]"
    intention_activite_1: "[intention dérivée]"
    activite_2: "[activité 2 section 4]"
    intention_activite_2: "[intention dérivée]"
    justification: "[justification]"

  - section: 5
    type_section: Apprentissage
    competence_visee: "[Compétence 4 – A_008]"
    ressource: "Page"
    intention_ressource: "Acquisition"
    activite_1: "[activité 1 section 5]"
    intention_activite_1: "[intention dérivée]"
    activite_2: "[activité 2 section 5]"
    intention_activite_2: "[intention dérivée]"
    justification: "[justification]"

  - section: 6
    type_section: Classe virtuelle (BBB)
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: "BigBlueButtonBN"
    intention_activite_1: "Discussion"
    activite_2: null
    intention_activite_2: null
    justification: null

  - section: 7
    type_section: Forum général
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: "Forum"
    intention_activite_1: "Discussion / Collaboration"
    activite_2: null
    intention_activite_2: null
    justification: null

  - section: 8
    type_section: Évaluation
    competence_visee: null
    ressource: null
    intention_ressource: null
    activite_1: "Sondage Magistère"
    intention_activite_1: "Enquête"
    activite_2: null
    intention_activite_2: null
    justification: null

```
---

## 📄 Aperçu des formats d’export

### Format “Généralités”
| titre_formation | public_type | public_profil | public_niveau | besoins_spec1 | besoins_spec2 | type_parcours | hybridation | temps_total | autonomie | animation | calendrier | horaires | nb_participants |
|-----------------|-------------|---------------|---------------|---------------|---------------|---------------|-------------|-------------|-----------|-----------|------------|----------|-----------------|
| [titre]         | [type]      | [profil]      | [niveau]      | [b1]          | [b2]          | [parcours]    | [hybrid]    | [temps]     | [auto]    | [anim]    | [cal]      | [hor]    | [nb]            |

### Format “Contenus par section”
| Section | Type de section | Compétences visées | Ressource | Intention ressource | Activité 1 | Intention activité 1 | Activité 2 | Intention activité 2 | Justification activité(s) |
|---------|-----------------|--------------------|-----------|---------------------|------------|----------------------|------------|----------------------|---------------------------|
| 1       | Accueil         | null               | null      | null                | null       | null                 | null       | null                 | null                      |
| 2       | Apprentissage   | [Compétence 1]     | Page      | Acquisition         | ...        | ...                  | ...        | ...                  | ...                       |
| ...     | ...             | ...                | ...       | ...                 | ...        | ...                  | ...        | ...                  | ...                       |


## 📝 Étape 2 — Validation et conservation

Souhaitez-vous **valider** ce macrodesign (les deux blocs YAML ci-dessus) ?  
**Réponse : [à compléter]**

---

## 💾 Conservation recommandée

Nous vous conseillons **fortement** de **conserver les deux blocs YAML** ci-dessus dans un fichier nommé **`macrodesign.yml`**, soit en copiant-collant le contenu, soit via un lien de téléchargement si disponible.  
Ce fichier sera **directement réutilisable** lors du **microdesign**, qui vous guidera pour l’implémentation complète dans **Magistère**.

---

## 📤 Étape 3 — Partage et export

En plus de votre fichier YAML, vous pouvez générer un **format de partage** pour :
- **Échanger facilement** avec d’autres formateurs.
- **Ouvrir et modifier** dans un tableur (Excel, LibreOffice, Google Sheets).
- **Préparer un affichage clair** à imprimer.

**Quel format de partage souhaitez-vous en plus du YAML conservé ?**  
- **Markdown (tableur “copier-coller”)** — rapide à lire dans un traitement de texte ou éditeur markdown.  
- **CSV (Excel / LibreOffice / Google Sheets)** — pratique pour travailler en tableur.  

**Réponse : [Markdown / CSV]**

> **Astuce :**  
> - **YAML** → à conserver pour la suite du parcours et la reprise dans le microdesign.  
> - **CSV / Markdown** → pour partager et ajuster avec vos collègues formateurs.

---

## ☎️ Référents académiques
- **DRANE — Laurent Castillo** — laurent.castillo@ac-toulouse.fr — 05 36 25 72 82  
- **DRANE — Caroline Menanteau** — caroline.menanteau@ac-toulouse.fr — 05 36 25 87 60  
- **EAFC — Laurence Graglia** — eafc-inge10@ac-toulouse.fr — 05 36 25 70 24