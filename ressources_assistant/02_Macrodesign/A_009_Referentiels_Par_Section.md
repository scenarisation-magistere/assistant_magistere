<!-- A_009_Referentiels_Par_Section.md (version mise à jour v2) -->

[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**

- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.
- Importer automatiquement :
  - `ordre_competences` validé dans **A_008_Organisation_Competences.md**.
  - `formulations_competences` validées dans **A_007_Competences_Visees.md**.
- Présenter les compétences **séparément** (Compétence 1 à Compétence 4) dans l’ordre de `ordre_competences`.
- Pour chaque compétence :
  - Créer 4 degrés : `Je débute`, `Je progresse`, `Je suis autonome`, `Je maîtrise`.
  - Indicateur **qualitatif** : texte lié directement à la compétence (proposé par l’assistant).
  - Indicateur **quantitatif** (fixe) :
    - Je débute → **Au moins 25 %** de réussite
    - Je progresse → **Au moins 50 %** de réussite
    - Je suis autonome → **Au moins 75 %** de réussite
    - Je maîtrise → **100 %** de réussite
- Badge : supprimé (non présent dans le gabarit final).
- Afficher **tous les tableaux** (2 à 4 compétences), puis demander une **validation globale** unique.
- Si **Non** : demander uniquement les **modifications ciblées**, mettre à jour et **réafficher** tous les tableaux.
- Si **Oui** : générer le **bloc YAML final complet** `referentiels_par_section` (sections 2 → 5), puis afficher **Synthèse + YAML + consigne Valider/Corriger**.
- Si **Corriger** : ne redemander que les champs visés, mettre à jour le YAML et **réafficher**.
- Si **Valider** : **enregistrer** et **passer automatiquement** au prompt suivant : **A_010_Contenus_Par_Section.md**.

---

# 🧭 A_009 — Référentiels d’auto-évaluation (validation globale)

## 🎯 Objectif
Produire des référentiels clairs, séparés par compétence, avec indicateurs qualitatifs liés à la compétence et indicateurs quantitatifs fixes, puis valider l’ensemble en une seule fois.  
👉 Cohérence avec le **gabarit tableur export (v5)** : 3 onglets (01_Généralités • 02_Référentiels • 03_Macrodesign).

---

## 📋 Tableaux par compétence (version blocs)

### Compétence 1 — [Formulation compétence 1]
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif (lié à la compétence) | indicateur_quantitatif |
|---------------|------------------------|------:|-------------------|---------------------------------------------|------------------------|
| C1            | [Compétence 1]         | 1     | Je débute         | [à proposer]                                | Au moins **25 %** |
|               |                        | 2     | Je progresse      | [à proposer]                                | Au moins **50 %** |
|               |                        | 3     | Je suis autonome  | [à proposer]                                | Au moins **75 %** |
|               |                        | 4     | Je maîtrise       | [à proposer]                                | **100 %** |

---

### Compétence 2 — [Formulation compétence 2]
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif (lié à la compétence) | indicateur_quantitatif |
|---------------|------------------------|------:|-------------------|---------------------------------------------|------------------------|
| C2            | [Compétence 2]         | 1     | Je débute         | [à proposer]                                | Au moins **25 %** |
|               |                        | 2     | Je progresse      | [à proposer]                                | Au moins **50 %** |
|               |                        | 3     | Je suis autonome  | [à proposer]                                | Au moins **75 %** |
|               |                        | 4     | Je maîtrise       | [à proposer]                                | **100 %** |

---

### Compétence 3 — [Formulation compétence 3]
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif (lié à la compétence) | indicateur_quantitatif |
|---------------|------------------------|------:|-------------------|---------------------------------------------|------------------------|
| C3            | [Compétence 3]         | 1     | Je débute         | [à proposer]                                | Au moins **25 %** |
|               |                        | 2     | Je progresse      | [à proposer]                                | Au moins **50 %** |
|               |                        | 3     | Je suis autonome  | [à proposer]                                | Au moins **75 %** |
|               |                        | 4     | Je maîtrise       | [à proposer]                                | **100 %** |

---

### Compétence 4 (optionnelle) — [Formulation compétence 4]
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif (lié à la compétence) | indicateur_quantitatif |
|---------------|------------------------|------:|-------------------|---------------------------------------------|------------------------|
| C4            | [Compétence 4]         | 1     | Je débute         | [à proposer]                                | Au moins **25 %** |
|               |                        | 2     | Je progresse      | [à proposer]                                | Au moins **50 %** |
|               |                        | 3     | Je suis autonome  | [à proposer]                                | Au moins **75 %** |
|               |                        | 4     | Je maîtrise       | [à proposer]                                | **100 %** |

*(Afficher seulement 2 à 4 compétences selon ce qui a été validé dans A_007 et A_008.)*

---

## 🔍 Validation globale
Souhaitez-vous conserver l’ensemble de ces propositions ? (**Oui/Non**)  
**Réponse : [à compléter]**

---

## ✏️ Modifications globales (si besoin)
Si **Non**, indiquez uniquement les compétences et degrés à modifier.  
**Réponse : [à compléter]**

---

## 📦 Bloc YAML final (aligné sur export tableur v5)

```yaml
referentiels_par_section:
  - competence_id: C1
    competence_formulation: "[Compétence 1]"
    niveaux:
      - degre: 1
        libelle: "Je débute"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 25 %"
      - degre: 2
        libelle: "Je progresse"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 50 %"
      - degre: 3
        libelle: "Je suis autonome"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 75 %"
      - degre: 4
        libelle: "Je maîtrise"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "100 %"
  - competence_id: C2
    competence_formulation: "[Compétence 2]"
    niveaux:
      - degre: 1
        libelle: "Je débute"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 25 %"
      - degre: 2
        libelle: "Je progresse"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 50 %"
      - degre: 3
        libelle: "Je suis autonome"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 75 %"
      - degre: 4
        libelle: "Je maîtrise"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "100 %"
  - competence_id: C3
    competence_formulation: "[Compétence 3]"
    niveaux:
      - degre: 1
        libelle: "Je débute"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 25 %"
      - degre: 2
        libelle: "Je progresse"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 50 %"
      - degre: 3
        libelle: "Je suis autonome"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 75 %"
      - degre: 4
        libelle: "Je maîtrise"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "100 %"
  - competence_id: C4
    competence_formulation: "[Compétence 4]"
    niveaux:
      - degre: 1
        libelle: "Je débute"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 25 %"
      - degre: 2
        libelle: "Je progresse"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 50 %"
      - degre: 3
        libelle: "Je suis autonome"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "Au moins 75 %"
      - degre: 4
        libelle: "Je maîtrise"
        indicateur_qualitatif: "[à valider]"
        indicateur_quantitatif: "100 %"
