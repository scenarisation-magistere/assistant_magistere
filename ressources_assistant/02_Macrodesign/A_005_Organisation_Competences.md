<!-- A_005_Organisation_Competences.md -->

[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**  
> **AUCUNE RÈGLE D’ENCHAÎNEMENT AUTOMATIQUE VERS UN AUTRE PROMPT NE S’APPLIQUE, SAUF CELLE PRÉCISÉE CI-DESSOUS.**

- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.
- Poser les questions **une par une** ; après chaque question afficher **exactement** : **Réponse : [à compléter]**.
- Importer la variable **formulations_competences** validée dans **A_004_Competences_Visees.md**.
- **Sources de justification** : utiliser en appui les éléments validés à l’étape **A_003_Titre_Obj_Public_Contraintes.md** (clés YAML `contexte_formation` et `public_cible`) pour argumenter l’ordre proposé.
- Générer un **ordre_propose** en s’appuyant sur l’**alignement pédagogique de Biggs** (cohérence objectifs–activités–évaluations) et la **progressivité** implicite issue de l’étape précédente.
- Présenter **ordre_propose** avec deux volets :
  1) **Justification (synthèse — ≤ 4 puces)** : brève, points clés.  
  2) **Justification complémentaire (systématique — ≤ 6 lignes)** : expliciter l’ordre proposé à partir :  
     - de l’**objectif général** et du **titre** (A_003),  
     - du **public cible et du niveau d’expertise** (A_003),  
     - des **contraintes / modalités d’animation** (A_003),  
     - de l’alignement **Objectifs ↔ Activités ↔ Évaluations** (Biggs),  
     - et, si disponible, des **conditions d’accessibilité** mentionnées en A_003.  
- Q1 : « Souhaitez-vous conserver cet ordre ? (Oui/Non) » → afficher ensuite **exactement** : **Réponse : [à compléter]**.
- Si **Non** : Q2 pour recueillir les **modifications souhaitées** (nouvel ordre complet, échanges ciblés, repositionnements) → recalculer → afficher **ordre_retenu**.
- Générer **ordre_retenu** (chaque entrée : **code**, **formulation**, **justification**).
- Q3 : « Confirmez-vous l’ordre retenu ? (Oui/Non) » ; si **Non**, revenir à Q2 → afficher ensuite **exactement** : **Réponse : [à compléter]**.
- À **validation**, produire **un seul bloc YAML final** nommé **ordre_competences** (l’**ordre des lignes = ordre des sections**) et l’afficher comme **unique référence de validation**.
- Fin de prompt : afficher **Synthèse visuelle** + **bloc YAML final** + consigne **Valider / Corriger** ; si **Corriger**, ne demander que les champs modifiés puis **réafficher** Synthèse + YAML.
- **Référence RAG (modèles)** : si le participant demande un appui théorique, présenter un bref apport distinct (source : **R_02_Modeles_Pedagogiques_Inspirants.md** — entrée « Alignement pédagogique, Biggs »).
- **Après une réponse “Valider” à la fin**, **enchaîner avec A_006_Referentiels_Par_Section.md**.

---

# 🧭 A_005 — Organisation des compétences par section

## 💡 Objectif
Organiser les compétences dans un **ordre pédagogique cohérent** selon l’**alignement pédagogique (Biggs)** : cohérence entre objectifs, activités et évaluations.

- Rappel théorique (très bref) : l’alignement pédagogique, conceptualisé par **John Biggs (1999)**, garantit que les compétences formulées à l’étape précédente sont **traduites en activités appropriées** et **évaluées de manière cohérente**.  
- Pour un complément (facultatif), l’assistant peut fournir un court encadré issu de la RAG (source : **R_02_Modeles_Pedagogiques_Inspirants.md**).

Cet ordre déterminera **directement** l’enchaînement des **sections d’apprentissage**.

---

## 🧾 Compétences issues de l’étape précédente
*(extrait attendu du YAML validé en fin de A_004_Competences_Visees.md)*

formulations_competences:
  - "[compétence 1]"
  - "[compétence 2]"
  - "[compétence 3]"
  - "[compétence 4]"

---

## 1) Proposition initiale de l’assistant
**Principes utilisés** : **cohérence (Biggs)** + **progressivité** (issue de l’étape précédente).

ordre_propose:
  - code: C1
    formulation: "[compétence 1]"
  - code: C3
    formulation: "[compétence 3]"
  - code: C2
    formulation: "[compétence 2]"
  - code: C4
    formulation: "[compétence 4]"

**Justification (synthèse — ≤ 4 puces)**
- C1 : base commune pour engager sans obstacle  
- C3 : tâche concrète qui consolide l’autonomie  
- C2 : transfert vers une autre situation  
- C4 : synthèse / regard réflexif en fin de parcours

**Justification complémentaire (systématique — ≤ 6 lignes)**  
- **Objectif général (A_003)** : l’ordre propose d’abord la compétence la plus directement liée à l’objectif global afin d’installer les prérequis.  
- **Public / niveau d’expertise (A_003)** : la montée en complexité (C1→C3→C2→C4) tient compte du niveau majoritaire déclaré et limite la charge cognitive en début de parcours.  
- **Contraintes / modalités (A_003)** : si co-animation ou limites techniques, C3 est placée tôt pour capitaliser sur les temps synchrones et les outils disponibles.  
- **Alignement Biggs** : chaque compétence est associée à des activités et à des preuves d’évaluation distinctes ; la progression vise une cohérence **Objectifs ↔ Activités ↔ Évaluations**.  
- **Accessibilité (si mentionnée en A_003)** : ordre visant à lever les obstacles anticipés (progressivité, supports variés) et à favoriser l’engagement.

**Souhaitez-vous conserver cet ordre ? (Oui/Non)**  
**Réponse : [à compléter]**

---

## 2) Si nécessaire — Indiquez vos modifications

Formes acceptées (exemples) :
- Nouvel ordre complet : C2 > C1 > C3 > C4
- Échanges ciblés : échanger C2 et C3
- Positionnement : placer C4 en 2e

**Réponse : [à compléter]**

---

## 3) Ordre retenu (avec justification)

ordre_retenu:
  - code: C1
    formulation: "[compétence 1]"
    justification: "[pourquoi en 1re position]"
  - code: C3
    formulation: "[compétence 3]"
    justification: "[justification]"
  - code: C2
    formulation: "[compétence 2]"
    justification: "[justification]"
  - code: C4
    formulation: "[compétence 4]"
    justification: "[justification]"

**Confirmez-vous l’ordre retenu ? (Oui/Non)**  
**Réponse : [à compléter]**

---

## ✅ Synthèse & validation

Ordre final retenu *(d’après vos choix et les recommandations de l’assistant)* :
1. [Compétence en 1re position]  
2. [Compétence en 2e position]  
3. [Compétence en 3e position]  
4. [Compétence en 4e position, si renseignée]

Bloc YAML final à valider :
```yaml
ordre_competences:
  - code: C1
    formulation: "[compétence 1]"
    justification: "[...]"
  - code: C3
    formulation: "[compétence 3]"
    justification: "[...]"
  - code: C2
    formulation: "[compétence 2]"
    justification: "[...]"
  - code: C4
    formulation: "[compétence 4]"
    justification: "[...]"
```

Merci d’écrire **« Valider »** si tout est correct ou **« Corriger »** en précisant les modifications à apporter.  
**Réponse : [à compléter]**
