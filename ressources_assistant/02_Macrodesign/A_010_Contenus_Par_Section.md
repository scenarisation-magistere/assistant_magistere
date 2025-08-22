<!-- A_010_Contenus_Par_Section.md — version mise à jour (v2.1, alignée gabarit v5 et règles de filtrage CMO hybride) -->

[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE FORMATEUR, MOT POUR MOT, SANS MODIFICATION NI OMISSION.**  
> **AUCUNE RÉÉCRITURE, AUCUNE SYNTHÈSE. MARKDOWN UNIQUEMENT.**  
> **TOUTES LES SORTIES DOIVENT ÊTRE FOURNIES INTÉGRALEMENT EN MARKDOWN BRUT, DANS UN SEUL BLOC TRIPLE BACKTICKS, SANS TEXTE EN DEHORS.**

- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.
- Importer automatiquement :
  - `ordre_competences` validé dans **A_008_Organisation_Competences.md**.
  - `referentiels_par_section` validé dans **A_009_Referentiels_Par_Section.md** (pour `evaluation_mode` des S2–S5).
  - Le tableau RAG **R_03_Tableau_Choix_Ressources_Activites_Ressources_ABCLD.md** *(types et intentions alignés ; priorité de sélection par `reco` : 3 puis 2)*.
  - Le **gabarit d’export v5 (onglet 03_Macrodesign)** pour les **noms de champs exacts** et la **structure finale**.
- **Respect absolu** des contraintes CMO : ≤ **3 h**, ≤ **512 Mo**, **hybride** (asynchrone majoritaire), **autoformation accompagnée**.

---

# 🧭 A_010 — Contenus par section (S1 → S8)

## 🎯 Objectif
Générer, pour **S1 à S8**, les **ressources** et **activités** alignées sur :
- l’**ordre des compétences** (S2 → S5),
- le **référentiel d’auto‑évaluation** (S2 → S5, mode d’évaluation),
- les **intentions ABC Learning Design** (priorités ci‑dessous),
- la **table de choix R_03** (filtrage par type, intention et **`reco`**).

---

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
  - Ex. si compétence de **Collaboration** → choisir une **activité collaborative** avec intention **Collaboration** (Forum, Atelier, Wiki, Padlet/outil de co‑construction H5P…).
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
  - `evaluation_mode = auto_evaluation_4_degres` (cohérence A_009).
- **S6 — Classe virtuelle (BBB)** : `activite_1_type = BigBlueButtonBN`, `intention_activite_1 = Discussion`.  
- **S7 — Forum général** : `activite_1_type = Forum`, `intention_activite_1 = Discussion / Collaboration`.  
- **S8 — Évaluation de satisfaction** : `activite_1_type = Sondage Magistère`, `intention_activite_1 = Enquête`.

### 6) Contraintes d’export — Gabarit v5 (onglet 03)
- **Champs obligatoires** (noms **exactement**) :  
  `section_id, type_section, competence_id, competence_formulation, ressource_type, ressource_url, intention_ressource, activite_1_type, activite_1_url, intention_activite_1, activite_2_type, activite_2_url, intention_activite_2, justification_pedagogique, modalite, duree_estimee_min, evaluation_mode`.  
- **URLs** : si inconnues → `URL_A_COMPLETER`.  
- **Modalité / Durée / Éval. (valeurs par défaut recommandées)** :  
  - S1 : `modalite=asynchrone`, `duree_estimee_min=10`, `evaluation_mode=""`  
  - S2–S5 : `modalite=asynchrone`, `duree_estimee_min ∈ {30..45}`, `evaluation_mode=auto_evaluation_4_degres`  
  - S6 : `modalite=synchrone`, `duree_estimee_min=45`, `evaluation_mode=""`  
  - S7 : `modalite=asynchrone`, `duree_estimee_min=10`, `evaluation_mode=""`  
  - S8 : `modalite=asynchrone`, `duree_estimee_min=10`, `evaluation_mode=evaluation_satisfaction`

---

## 📤 Format de sortie (obligatoire)

- L’assistant produit **UNIQUEMENT** :
  1) **Un tableau Markdown** (colonnes fixes ci‑dessous) récapitulant **S1 → S8**.  
  2) **Un bloc YAML** **miroir** au **schéma v5** (`macrodesign: [...]`) prêt à l’export (onglet 03).

### Colonnes du tableau (ordre fixe)
| Section | Type de section | Compétence (id + formulation) | Ressource (type) | URL ressource | Intention ressource | Activité 1 (type) | URL activité 1 | Intention activité 1 | Activité 2 (type) | URL activité 2 | Intention activité 2 | Justification pédagogique | Modalité | Durée (min) | Évaluation |

> **Important :**  
> - **Pas de `null`** dans le tableau : utiliser `""` pour les champs vides.  
> - **Activité 2** absente si non pertinente (laisser `""` dans les colonnes associées).  
> - La **justification** est **obligatoire** pour S2–S5, concise (2–3 phrases), **centrée sur la pertinence** par rapport à la **compétence** et aux **priorités ABC LD**.

---

## 🧪 Exemple minimal (structure)

```markdown
| Section | Type de section        | Compétence (id + formulation)   | Ressource (type) | URL ressource     | Intention ressource | Activité 1 (type) | URL activité 1    | Intention activité 1 | Activité 2 (type) | URL activité 2 | Intention activité 2 | Justification pédagogique                                            | Modalité   | Durée (min) | Évaluation                    |
|---------|------------------------|----------------------------------|------------------|-------------------|---------------------|-------------------|-------------------|----------------------|-------------------|----------------|----------------------|------------------------------------------------------------------------|------------|-------------|-------------------------------|
| S1      | Accueil                | ""                               | Page             | URL_A_COMPLETER   | Acquisition         | ""                | ""                | ""                   | ""                | ""             | ""                   | Cadrage et attentes                                                   | asynchrone | 10          | ""                            |
| S2      | Apprentissage          | C1 — [formulation C1]            | Ressource H5P    | URL_A_COMPLETER   | Acquisition         | Forum             | URL_A_COMPLETER   | Collaboration        | ""                | ""             | ""                   | Ressource pour acquérir ; activité collaborative pour valider en pair | asynchrone | 35          | auto_evaluation_4_degres      |
| S3      | Apprentissage          | C2 — [formulation C2]            | Page             | URL_A_COMPLETER   | Acquisition         | Test              | URL_A_COMPLETER   | Pratique             | H5P Essay         | URL_A_COMPLETER| Production            | Ressource pour comprendre ; test pour appliquer ; essai pour produire | asynchrone | 35          | auto_evaluation_4_degres      |
| S6      | Classe virtuelle (BBB) | ""                               | ""               | ""                | ""                  | BigBlueButtonBN   | URL_A_COMPLETER   | Discussion           | ""                | ""             | ""                   | ""                                                                     | synchrone  | 45          | ""                            |
| S7      | Forum général          | ""                               | ""               | ""                | ""                  | Forum             | URL_A_COMPLETER   | Discussion / Collaboration | ""           | ""             | ""                   | ""                                                                     | asynchrone | 10          | ""                            |
| S8      | Évaluation de satisfaction | ""                            | ""               | ""                | ""                  | Sondage Magistère | URL_A_COMPLETER   | Enquête              | ""                | ""             | ""                   | ""                                                                     | asynchrone | 10          | evaluation_satisfaction       |
