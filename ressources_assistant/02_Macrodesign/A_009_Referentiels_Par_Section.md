[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**

- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.
- Importer automatiquement :
  - `ordre_competences` validé dans **A_008_Organisation_Competences.md**.
  - `formulations_competences` validées dans **A_007_Competences_Visees.md**.
- Présenter les compétences **séparément** (Compétence 1 à Compétence 4) dans l’ordre de `ordre_competences`.
- Pour chaque compétence :
  - Créer 4 degrés : `Je débute`, `Je progresse`, `Je suis autonome`, `Je maîtrise avec aisance`.
  - Indicateur **qualitatif** : texte lié directement à la compétence (proposé par l’assistant).
  - Indicateur **quantitatif** (fixe) :
    - Je débute → **25 %** de réussite dans l’activité proposée.
    - Je progresse → **50 %** de réussite dans l’activité proposée.
    - Je suis autonome → **75 %** de réussite dans l’activité proposée.
    - Je maîtrise avec aisance → **> 75 %** de réussite dans l’activité proposée.
  - **Badge** = "oui" si **degré 3** atteint ; sinon "non".
- Ne pas inclure d’adaptations CUA par défaut (les ajouter uniquement si le formateur les demande explicitement).
- Afficher **tous les tableaux** (2 à 4 compétences), puis demander une **validation globale** unique.
- Si **Non** : demander uniquement les **modifications ciblées**, mettre à jour et **réafficher** tous les tableaux.
- Si **Oui** : générer le **bloc YAML final complet** `referentiels_par_section` (sections 2 → 5), puis afficher **Synthèse + YAML + consigne Valider/Corriger**.
- Si **Corriger** : ne redemander que les champs visés, mettre à jour le YAML et **réafficher**.
- Si **Valider** : **enregistrer** et **passer automatiquement** au prompt suivant : **A_010_Contenus_Par_Section.md**.

---

# 🧭 A_009 — Référentiels d’auto-évaluation (validation globale)

## 🎯 Objectif
Produire des référentiels clairs, séparés par compétence, avec indicateurs qualitatifs liés à la compétence et indicateurs quantitatifs fixes, puis valider l’ensemble en une seule fois.

---

## 📋 Tableaux par compétence

### Compétence 1 — [Formulation compétence 1]
| Degré | Libellé                 | Indicateur qualitatif (lié à la compétence) | Indicateur quantitatif                              | Badge |
|------:|-------------------------|----------------------------------------------|-----------------------------------------------------|:-----:|
| 1     | Je débute               | [à proposer]                                 | 25 % de réussite dans l’activité proposée           |  non  |
| 2     | Je progresse            | [à proposer]                                 | 50 % de réussite dans l’activité proposée           |  non  |
| 3     | Je suis autonome        | [à proposer]                                 | 75 % de réussite dans l’activité proposée           |  oui  |
| 4     | Je maîtrise avec aisance| [à proposer]                                 | > 75 % de réussite dans l’activité proposée         |  non  |

---

### Compétence 2 — [Formulation compétence 2]
| Degré | Libellé                 | Indicateur qualitatif (lié à la compétence) | Indicateur quantitatif                              | Badge |
|------:|-------------------------|----------------------------------------------|-----------------------------------------------------|:-----:|
| 1     | Je débute               | [à proposer]                                 | 25 % de réussite dans l’activité proposée           |  non  |
| 2     | Je progresse            | [à proposer]                                 | 50 % de réussite dans l’activité proposée           |  non  |
| 3     | Je suis autonome        | [à proposer]                                 | 75 % de réussite dans l’activité proposée           |  oui  |
| 4     | Je maîtrise avec aisance| [à proposer]                                 | > 75 % de réussite dans l’activité proposée         |  non  |

---

### Compétence 3 — [Formulation compétence 3]
| Degré | Libellé                 | Indicateur qualitatif (lié à la compétence) | Indicateur quantitatif                              | Badge |
|------:|-------------------------|----------------------------------------------|-----------------------------------------------------|:-----:|
| 1     | Je débute               | [à proposer]                                 | 25 % de réussite dans l’activité proposée           |  non  |
| 2     | Je progresse            | [à proposer]                                 | 50 % de réussite dans l’activité proposée           |  non  |
| 3     | Je suis autonome        | [à proposer]                                 | 75 % de réussite dans l’activité proposée           |  oui  |
| 4     | Je maîtrise avec aisance| [à proposer]                                 | > 75 % de réussite dans l’activité proposée         |  non  |

---

### Compétence 4 — [Formulation compétence 4]
| Degré | Libellé                 | Indicateur qualitatif (lié à la compétence) | Indicateur quantitatif                              | Badge |
|------:|-------------------------|----------------------------------------------|-----------------------------------------------------|:-----:|
| 1     | Je débute               | [à proposer]                                 | 25 % de réussite dans l’activité proposée           |  non  |
| 2     | Je progresse            | [à proposer]                                 | 50 % de réussite dans l’activité proposée           |  non  |
| 3     | Je suis autonome        | [à proposer]                                 | 75 % de réussite dans l’activité proposée           |  oui  |
| 4     | Je maîtrise avec aisance| [à proposer]                                 | > 75 % de réussite dans l’activité proposée         |  non  |

*(Si seulement 2 ou 3 compétences : n’afficher que les tableaux correspondants, dans l’ordre de `ordre_competences`.)*

---

## 🔍 Validation globale
Souhaitez-vous conserver l’ensemble de ces propositions ? (**Oui/Non**)  
**Réponse : [à compléter]**

---

## ✏️ Modifications globales (si besoin)
Si **Non**, indiquez uniquement les compétences et degrés à modifier.  
**Réponse : [à compléter]**

---

## 📦 Bloc YAML final (complet — 4 compétences)
> **Inclure uniquement les compétences réellement présentes (2 à 4).**  
> **Respecter l’ordre de `ordre_competences` (sections S2 → S5).**

```yaml
referentiels_par_section:
  - section: 2
    competence: "[Compétence 1]"
    badge: "oui (si degré 3 atteint)"
    niveaux:
      - degre: 1
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "25 % de réussite dans l’activité proposée"
      - degre: 2
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "50 % de réussite dans l’activité proposée"
      - degre: 3
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "75 % de réussite dans l’activité proposée"
      - degre: 4
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "> 75 % de réussite dans l’activité proposée"
  - section: 3
    competence: "[Compétence 2]"
    badge: "oui (si degré 3 atteint)"
    niveaux:
      - degre: 1
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "25 % de réussite dans l’activité proposée"
      - degre: 2
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "50 % de réussite dans l’activité proposée"
      - degre: 3
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "75 % de réussite dans l’activité proposée"
      - degre: 4
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "> 75 % de réussite dans l’activité proposée"
  - section: 4
    competence: "[Compétence 3]"
    badge: "oui (si degré 3 atteint)"
    niveaux:
      - degre: 1
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "25 % de réussite dans l’activité proposée"
      - degre: 2
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "50 % de réussite dans l’activité proposée"
      - degre: 3
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "75 % de réussite dans l’activité proposée"
      - degre: 4
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "> 75 % de réussite dans l’activité proposée"
  - section: 5
    competence: "[Compétence 4]"
    badge: "oui (si degré 3 atteint)"
    niveaux:
      - degre: 1
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "25 % de réussite dans l’activité proposée"
      - degre: 2
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "50 % de réussite dans l’activité proposée"
      - degre: 3
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "75 % de réussite dans l’activité proposée"
      - degre: 4
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "> 75 % de réussite dans l’activité proposée"
