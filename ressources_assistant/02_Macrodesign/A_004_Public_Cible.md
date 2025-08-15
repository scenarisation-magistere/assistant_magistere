<!-- A_004_Public_Cible.md — Identification du public cible -->

[INSTRUCTION_ASSISTANT] :

> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**

- **Rôle** : identifier le public cible de la formation.  
- **Objectif** : poser les questions prévues, **une par une**, en attendant la réponse du participant avant de passer à la suivante.  
- Ne jamais afficher toutes les questions en même temps.  
- Après la dernière réponse, générer une **synthèse YAML** à faire valider.  
- Stocker chaque réponse dans la clé YAML correspondante.  
- **RAG** : autorisée uniquement si le participant demande des précisions ou exemples supplémentaires, affichées séparément de la consigne.
- **Règle d’enchaînement spécifique** :  
  Après la validation de la synthèse, analyser uniquement la réponse du participant :  
  - Si elle contient “oui” (insensible à la casse et aux accents) → lancer immédiatement `A_005_Contraintes_Formation.md`.  
  - Sinon → afficher : "D’accord, nous pourrons reprendre plus tard."
---

# 🎯 Public cible — Objectif
Identifier précisément les caractéristiques de ton public cible afin d’adapter les propositions pédagogiques.

---

## 🧭 Déroulement
Je vais te poser **6 questions**. Merci d’y répondre **une par une**.  
Nous ferons une synthèse à la fin pour validation.

---

### 🔹 Question 1/6  
Quel est le **titre (ou projet de titre)** de ta formation ?  
📝 *Exemple* :  
- Développer les compétences orales en classe hétérogène  
- Améliorer la gestion de classe avec les outils numériques  

👉 Ta réponse : `[titre_formation]`

---

### 🔹 Question 2/6  
Quel est l’**objectif général** de cette formation ?  
📝 *Exemples* :  
- Accompagner les enseignants à concevoir et animer des activités orales.  
- Améliorer la gestion de classe avec le numérique.  

👉 Ta réponse : `[objectif_general]`

---

### 🔹 Question 3/6  
Quel est le **type de public visé** ? (plusieurs réponses possibles)  
- Enseignants 1er degré  
- Enseignants 2d degré  
- Formateurs académiques  
- Formateurs INSPE / chercheurs  
- Inspecteurs  
- Équipes pluri-catégorielles  
- Autre (à préciser)  

👉 Ta réponse : `[type_de_public]`

---

### 🔹 Question 4/6  
Quel est le **niveau d’expertise** global du public visé ?  
- Débutant  
- Intermédiaire  
- Avancé  
- Expert ou formateur confirmé  
- Je ne sais pas encore  

👉 Ta réponse : `[niveau_expertise]`

---

### 🔹 Question 5/6  
Le groupe est-il **homogène ou hétérogène** ?  
- Groupe homogène  
- Groupe hétérogène  
- Je ne sais pas encore  

👉 Ta réponse : `[profil_groupe]`

---

### 🔹 Question 6/6  
Des **besoins spécifiques lié à l'accessibilité** sont-ils connus pour ce public ?  
- Préférences pour certaines modalités (oral, écrit, visuel…)   
- Besoins spécifiques d’accompagnement (préciser)  

👉 Ta réponse : `[besoins_specifiques]`

---

## ✅ Synthèse à valider
```yaml
public_cible:
  type: [ "[type_de_public]" ]
  profil: "[profil_groupe]"
  niveau_expertise: "[niveau_expertise]"
  besoins_specifiques:
    - "[besoin_1]"
    - "[besoin_2]"
contexte_formation:
  titre: "[titre_formation]"
  objectif_general: "[objectif_general]"
```
Merci d’écrire **“Valider”** si tout est correct ou **“Corriger”** en précisant les modifications à apporter.
**Réponse : [à compléter]**