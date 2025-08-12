[INSTRUCTION_ASSISTANT] :
- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.
- Poser les questions **une par une** ; après chaque question afficher **exactement** : `**Réponse : [à compléter]**`.
- Importer la variable `formulations_competences` validée dans **A_007_Competences_Visees.md**.
- Générer un `ordre_propose` en s’appuyant sur l’**alignement pédagogique de Biggs** (cohérence objectifs–activités–évaluations) et la **progressivité** implicite issue de l’étape précédente.
- Présenter `ordre_propose` avec une **justification courte** (≤ 4 puces).
- Q1 : “Souhaitez-vous conserver cet ordre ? (Oui/Non)” → `**Réponse : [à compléter]**`.
- Si **Non** : Q2 pour recueillir les **modifications souhaitées** (nouvel ordre complet, échanges ciblés, repositionnements) → recalculer → afficher `ordre_retenu`.
- Générer `ordre_retenu` (chaque entrée : `code`, `formulation`, `justification`).
- Q3 : “Confirmez-vous l’ordre retenu ? (Oui/Non)” ; si **Non**, revenir à Q2.
- À **validation**, produire le bloc YAML `ordre_competences` dont **l’ordre des lignes = ordre des sections** ; stocker en variable interne `ordre_competences`.
- Fin de prompt : afficher **Synthèse** + **bloc YAML final** + consigne **Valider / Corriger** ; si **Corriger**, ne demander que les champs modifiés puis **réafficher** Synthèse + YAML.
- Passer ensuite à **A_009_Referentiels_Par_Section.md**.

---

# 🧭 A_008 — Organisation des compétences par section

## 💡 Objectif
Organiser les compétences dans un **ordre pédagogique cohérent** selon l’**alignement pédagogique (Biggs)** : cohérence entre objectifs, activités et évaluations.  
👉 Synthèse modèles pédagogiques (RAG) : [R_02_001_RC_Modeles_Pedagogiques_Inspirants.md](R_02_001_RC_Modeles_Pedagogiques_Inspirants.md)  
Cet ordre déterminera **directement** l’enchaînement des **sections d’apprentissage**.

---

## 🧾 Compétences issues de l’étape précédente
~~~yaml
formulations_competences:
  - "[compétence 1]"
  - "[compétence 2]"
  - "[compétence 3]"
  - "[compétence 4]"
~~~

---

## 1) Proposition initiale de l’assistant
Principes utilisés : cohérence (Biggs) + progressivité (de l’étape précédente).

~~~yaml
ordre_propose:
  - code: C1
    formulation: "[compétence 1]"
  - code: C3
    formulation: "[compétence 3]"
  - code: C2
    formulation: "[compétence 2]"
  - code: C4
    formulation: "[compétence 4]"
~~~

**Justification (synthèse)**
- C1 : base commune pour engager sans obstacle.  
- C3 : tâche concrète qui consolide l’autonomie.  
- C2 : transfert vers une autre situation.  
- C4 : synthèse / regard réflexif en fin de parcours.

**Souhaitez-vous conserver cet ordre ? (Oui/Non)**  
**Réponse : [à compléter]**

---

## 2) Si nécessaire — Indiquez vos modifications
Formes acceptées (exemples) :
- Nouvel ordre complet : `C2 > C1 > C3 > C4`
- Échanges ciblés : `échanger C2 et C3`
- Positionnement : `placer C4 en 2e`

**Réponse : [à compléter]**

---

## 3) Ordre retenu (avec justification)
~~~yaml
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
~~~

**Confirmez-vous l’ordre retenu ? (Oui/Non)**  
**Réponse : [à compléter]**

---

## 📦 Bloc YAML final (à transmettre)
> **Important** : l’**ordre des lignes** ci-dessous déterminera l’**ordre des sections** d’apprentissage.  
> Ligne 1 = Section 1, Ligne 2 = Section 2, etc.  
> Le code (`C1`, `C2`…) sert de traçabilité ; **seule la position** compte pour l’enchaînement.

~~~yaml
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
~~~

---

## ✅ Synthèse & contrôle de fin d’étape
- Ordre final retenu : **[C1 > C3 > C2 > C4]** (à adapter selon validation).  
- Passage prévu vers : **A_009_Referentiels_Par_Section.md**.

Écrivez **“Valider”** pour confirmer et passer à l’étape suivante, ou **“Corriger”** pour revenir à l’étape 2.  
**Réponse : [à compléter]**
