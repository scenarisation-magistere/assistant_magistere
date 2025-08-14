# Génération du récapitulatif de Macrodesign

[INSTRUCTION_ASSISTANT] :
- But : Générer une fiche complète de macrodesign à partir :
  - des données générales validées (prompts 001B → 001D),
  - des compétences (001E) et de leur ordre (001F / A_008 → `ordre_competences`),
  - des référentiels d’autoévaluation par section (001G),
  - du YAML `contenus_sections` produit par A_010B.
- Sorties attendues :
  1) Bloc YAML `macrodesign_generalites`
  2) Bloc YAML `contenus_par_section`
  Les deux blocs doivent être autocohérents et exploitables pour l’export.
- Règles :
  - Ne pas modifier le contenu validé ; seulement assembler et normaliser.
  - Si un champ manque : laisser des crochets `[ ]` (ne pas inventer).
  - Respecter le scénario CMO (8 sections) et la nomenclature A_010B.
- Vérifications :
  - Concordance compétences ↔ sections S2–S5.
  - Présence de l’intention “Acquisition” dans S2–S5.
  - Présence du badge standard en S2–S5.
- Variables internes : `yaml_generalites`, `yaml_contenus` (concaténation finale).
- Affichage après validation :
  - Afficher “📤 Consignes d’export — Deux formats au choix”.
  - Formulation simple : le participant peut
    1) garder un fichier **YAML** pour réutiliser plus tard ;
    2) ouvrir deux fichiers **CSV** pour visualiser/éditer au tableur.
  - Préciser : “Quand vous commencerez le microdesign, l’assistant vous proposera d’intégrer le fichier YAML si vous l’avez conservé.”
- Question préalable (avant export) : poser la variable interne `lancer_tutorat_apres_export` avec choix [Oui / Non].
- Après validation et export du macrodesign, poser la question au participant :  
  “Souhaitez-vous enchaîner avec un module **optionnel** pour définir votre **plan d’accompagnement tutoral** selon la **méthode Jacques Rodet** ?”  
  - **Oui** → l’assistant guidera immédiatement le participant pour définir son plan d’accompagnement tutoral et produira un export séparé (YAML et/ou CSV) dédié au tutorat.  
  - **Non** → passer directement à la suite (microdesign).  
- Enregistrer la réponse dans la variable interne `lancer_tutorat_apres_export`.  
- Si `lancer_tutorat_apres_export = "Oui"` → enchaîner avec le prompt opératoire `A_012_Tutorat_Anticipation.md` en mode export séparé (pas de fusion YAML).  
- Si `lancer_tutorat_apres_export = "Non"` → clore le macrodesign et proposer d’ouvrir le microdesign.  
- Ne jamais afficher le nom du fichier interne au participant ; utiliser uniquement la formulation pédagogique ci-dessus.
- Export (logique interne, affichage conditionnel) :
  - Poser la question : “Quel format d’export souhaitez-vous ? — [Markdown / CSV]”.
  - Si la réponse contient “markdown” (insensible casse/accents) :
    - Afficher UNIQUEMENT l’export Markdown tableur strict (Feuille 1 + Feuille 2).
    - Ne PAS afficher la version CSV.
  - Si la réponse contient “csv” :
    - Afficher UNIQUEMENT les deux blocs CSV (`generalites.csv` et `sections.csv`).
    - Après l’export CSV, proposer le lien suivant :  
      **“Pour un rendu formaté prêt à imprimer, vous pouvez télécharger notre modèle XLSX ici : [https://nuage02.apps.education.fr/index.php/s/wfDs68aYpokiKrP](https://nuage02.apps.education.fr/index.php/s/wfDs68aYpokiKrP) et y importer vos deux CSV.”**
    - Ne PAS afficher la version Markdown.
  - Sinon : redemander le choix avec l’indication “[exemples : Markdown / CSV]”.
  - Rappel : quand le microdesign démarrera, proposer au participant d’intégrer le fichier YAML s’il l’a conservé.
...

- TEMPLATES D’EXPORT (invisibles pour le participant — à utiliser selon le choix) :

  [TEMPLATE_MARKDOWN_FEUILLE_1]
  | titre_formation | public_type | public_profil | public_niveau | besoins_spec1 | besoins_spec2 | type_parcours | hybridation | temps_total | autonomie | animation | calendrier | horaires | nb_participants |
  | [titre] | [public_type] | [public_profil] | [public_niveau] | [b1] | [b2] | [type_parcours] | asynchrone (majeure) + synchrone (mineure) | moins de 3h | formation tutorée | [animation] | [calendrier] | [horaires] | [nb] |

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

  [TEMPLATE_CSV_GENERALITES]
  titre_formation;public_type;public_profil;public_niveau;besoins_spec1;besoins_spec2;type_parcours;hybridation;temps_total;autonomie;animation;calendrier;horaires;nb_participants
  [titre];[public_type];[public_profil];[public_niveau];[b1];[b2];[type_parcours];asynchrone (majeure) + synchrone (mineure);moins de 3h;formation tutorée;[animation];[calendrier];[horaires];[nb]

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

---

## 🎯 Objectif du prompt (visible formateur)

Assembler automatiquement tout le macrodesign validé en **deux blocs YAML prêts à l’export** :
- `macrodesign_generalites`
- `contenus_par_section`

Ces blocs serviront à produire un **tableur d’export** fidèle au scénario **CMO**.

---

## 🧾 Étape 1 — Génération des deux blocs YAML

### 📦 Bloc 1 — Généralités

```yaml
macrodesign_generalites:
  titre_formation: "[titre validé]"
  public_cible:
    type: "[enseignants / formateurs / autres]"
    profil: "[homogène / hétérogène]"
    niveau_expertise: "[débutant / intermédiaire / avancé]"
    besoins_specifiques:
      - "[besoin 1]"
      - "[besoin 2]"
  contraintes_formation:
    type_parcours: "[création / migration]"
    hybridation: "asynchrone (majeure) + synchrone (mineure)"
    temps_total: "moins de 3h"
    autonomie: "formation tutorée"
    animation: "[individuelle / coanimée]"
    calendrier: "[à préciser]"
    horaires: "[à préciser]"
    nombre_participants: "[valeur]"
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
  competences_visées:
    - "[formulation compétence 1]"
    - "[formulation compétence 2]"
    - "[formulation compétence 3]"
    - "[formulation compétence 4]"
  referentiels_autoévaluation:
    - section: 2
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
    - section: 3
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
    - section: 4
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
    - section: 5
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
~~~

### 📦 Bloc 2 — Contenus par section

```yaml
contenus_par_section:
  - section: 1
    titre: "Bienvenue dans la formation"
    intentions: ["Acquisition"]
    ressource: "Page d’accueil"
    activite_1: null
    activite_2: null
    discussion: "Présentation du parcours, modalités, contacts"
    badge: null
    modalite: "Asynchrone"

  - section: 2
    titre: "[titre section 2]"
    intentions: ["Acquisition", "[intention secondaire 2]"]
    ressource: "[ressource section 2]"
    activite_1: "[activité 1 section 2]"
    activite_2: "[activité 2 section 2]"
    discussion: "[discussion section 2]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 3
    titre: "[titre section 3]"
    intentions: ["Acquisition", "[intention secondaire 3]"]
    ressource: "[ressource section 3]"
    activite_1: "[activité 1 section 3]"
    activite_2: "[activité 2 section 3]"
    discussion: "[discussion section 3]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 4
    titre: "[titre section 4]"
    intentions: ["Acquisition", "[intention secondaire 4]"]
    ressource: "[ressource section 4]"
    activite_1: "[activité 1 section 4]"
    activite_2: "[activité 2 section 4]"
    discussion: "[discussion section 4]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 5
    titre: "[titre section 5]"
    intentions: ["Acquisition", "[intention secondaire 5]"]
    ressource: "[ressource section 5]"
    activite_1: "[activité 1 section 5]"
    activite_2: "[activité 2 section 5]"
    discussion: "[discussion section 5]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 6
    titre: "Classe virtuelle – mise en pratique"
    intentions: ["Collaboration"]
    ressource: "Lien vers classe virtuelle (BBB)"
    activite_1: null
    activite_2: null
    discussion: null
    badge: null
    modalite: "Synchrone"

  - section: 7
    titre: "Forum général – échanges libres"
    intentions: ["Discussion", "Collaboration"]
    ressource: null
    activite_1: "Forum"
    activite_2: null
    discussion: "Fils issus des discussions des sections S2 à S5"
    badge: null
    modalite: "Asynchrone"

  - section: 8
    titre: "Évaluation finale et perspectives"
    intentions: ["Enquête"]
    ressource: "Sondage Magistère"
    activite_1: null
    activite_2: null
    discussion: "Questionnaire de satisfaction à 3 temporalités"
    badge: null
    modalite: "Asynchrone"
```

---

## 📝 Étape 2 — Validation

Souhaitez-vous **valider** ce macrodesign (les deux blocs YAML ci-dessus) ?  
**Réponse : [à compléter]**

---

## 📤 Consignes d’export — Deux formats au choix

Vous pouvez récupérer votre macrodesign sous deux formes. Choisissez ce qui vous convient (vous pouvez aussi garder les deux) :

### A. Conserver un fichier YAML (pour réutiliser plus tard)
- À quoi ça sert ?  
  Pour reprendre votre travail plus tard, notamment lors du microdesign.
- Comment faire ?  
  1. Copiez les **deux blocs YAML** affichés ci-dessus (entre ```yaml et ```).  
  2. Collez-les dans un fichier texte et enregistrez sous **`macrodesign.yml`**.  
  3. Quand vous **commencerez le microdesign**, l’assistant vous **proposera d’intégrer ce fichier YAML** si vous l’avez conservé.

### B. Voir/éditer au tableur (CSV)
- À quoi ça sert ?  
  Pour une vue “tableur” (Excel, LibreOffice Calc, Google Sheets) et de petites corrections.
- Comment faire ?  
  1. Récupérez les deux blocs CSV fournis par l’assistant (**`generalites.csv`** et **`sections.csv`**).  
  2. Enregistrez-les tels quels, puis ouvrez-les dans votre tableur (séparateur **`;`**, encodage **UTF-8**).
- À noter :  
  Si vous modifiez le CSV et souhaitez ensuite reprendre avec le YAML, l’assistant pourra **reconvertir vos CSV en YAML**.

---

## Préférence — Préparer l’accompagnement tutoral après l’export ?

Après l’export du macrodesign, souhaitez-vous enchaîner avec un module **optionnel** pour définir votre **plan d’accompagnement tutoral** selon la **méthode Jacques Rodet** ?  
Ce module produira un **export séparé** (YAML et/ou CSV) dédié au tutorat, sans modifier votre macrodesign.

**Réponse : [à compléter]**  (Oui / Non)

- **Oui** → l’assistant vous guidera immédiatement pour définir votre plan d’accompagnement tutoral (méthode Jacques Rodet) et produira un export dédié au tutorat.  
- **Non** → vous passerez directement à la suite (microdesign) sans étape tutorat.

> L’export du macrodesign se fait d’abord.  
> Si vous répondez Oui, l’assistant lancera ensuite la phase tutorat.

---

[INSTRUCTION_ASSISTANT] :  
- Après validation et export du macrodesign, **poser la question ci-dessus** et enregistrer la réponse dans la variable interne `lancer_tutorat_apres_export`.  
- Si `lancer_tutorat_apres_export = "Oui"` → **enchaîner** avec le prompt opératoire `A_012_Tutorat_Anticipation.md` en **mode export séparé** (pas de fusion YAML).  
- Si `lancer_tutorat_apres_export = "Non"` → **clore** le macrodesign et proposer d’ouvrir le microdesign.  
- Ne jamais afficher le nom du fichier interne `A_012_Tutorat_Anticipation.md` au participant ; utiliser uniquement la formulation pédagogique indiquée ci-dessus.

---

## 📤 Étape 3 — Export (tableur)

Quel format d’export souhaitez-vous ?
- **Markdown (tableur “copier-coller”)**
- **CSV (Excel / LibreOffice / Google Sheets)**

**Réponse : [Markdown / CSV]**

> Après votre réponse, l’assistant affichera directement l’export correspondant.
