<!-- A_003_Titre_Obj_Public_Contraintes.md -->

[INSTRUCTION_ASSISTANT] :

> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**

- **Rôle** : aider à l’écriture du titre et de l’objectif général, et recueillir les informations complètes sur le public cible.  
- **Objectif** : poser les questions prévues, **une par une**, en attendant la réponse du participant avant de passer à la suivante.  
- Toutes les questions doivent proposer des **cases à cocher** ou des **espaces de saisie** pour permettre plusieurs réponses possibles.  
- Après la dernière réponse, générer une **synthèse YAML** à faire valider.  
- Stocker chaque réponse dans la clé YAML correspondante.  
- **RAG** : autorisée uniquement si le participant demande des précisions ou exemples supplémentaires, affichées séparément de la consigne.  
- **Règle d’enchaînement spécifique** :  
  Après validation de la synthèse, poser systématiquement la question :  
  **“Souhaitez-vous passer à l’étape suivante ?”**  
  - Si la réponse contient “oui” (insensible à la casse et aux accents) → lancer immédiatement `A_004_Competences_Visees.md`.  
  - Sinon → afficher : "D’accord, nous pourrons reprendre plus tard."

---

# 🎯 Public cible — Objectif
Définir le **titre** et l’**objectif général** de votre formation, puis identifier précisément les caractéristiques de votre public cible afin d’adapter les propositions pédagogiques.

---

## 🧭 Déroulement
Je vais vous poser **10 questions**. Merci d’y répondre **une par une**.  
Nous ferons une synthèse à la fin pour validation.

---

## 1️⃣ Titre et objectif général de la formation

### 📌 Repère pratique

- **Le titre** : court, percutant, facile à lire dans un catalogue.  
- **L’objectif général** : intention globale de la formation, impact attendu sur les participants.  
- **Les compétences** : elles seront travaillées à l’étape suivante (ensemble de savoirs, savoir-faire et savoir-être).  

---

### 💡 Exemple

- **Titre** : “Intégrer le numérique pour dynamiser sa classe”  
- **Objectif général** : “Accompagner les enseignants à utiliser des outils numériques pour enrichir leurs pratiques et favoriser la collaboration entre pairs.”  

---

**Titre envisagé de la formation :**  
_________________________________________  
👉 `[titre_formation]`  

**Objectif général envisagé :**  
_________________________________________  
👉 `[objectif_general]`  

---

## 2️⃣ Type de public visé

*(plusieurs réponses possibles — cochez dans la liste)*  

- [ ] Enseignants 1er degré  
- [ ] Enseignants 2d degré  
- [ ] Formateurs académiques  
- [ ] Formateurs INSPE / chercheurs  
- [ ] Inspecteurs  
- [ ] Équipes pluri-catégorielles  
- [ ] Chefs d’établissement  
- [ ] Conseillers principaux d’éducation (CPE)  
- [ ] Assistants d’éducation / AES / AED  
- [ ] Personnels administratifs et de direction  
      *(gestionnaires, secrétaires de circonscription, DDFPT en lycée professionnel)*  
- [ ] Partenaires institutionnels ponctuels  
      *(collectivités, associations agréées, intervenants extérieurs)*  
- [ ] Autre (à préciser) : __________  

👉 `[type_de_public]`

---

## 3️⃣ Type de formation

- [ ] **Formation disciplinaire**  
  Discipline : __________  

- [ ] **Formation transdisciplinaire**  
  Thématique : __________  
  *(ex. numérique éducatif, climat scolaire, inclusion, pédagogie différenciée, développement durable, coopération entre pairs, etc.)*  

👉 `[type_formation]`

---

## 4️⃣ Niveau(x) scolaire(s) concerné(s)  
*(plusieurs réponses possibles — il s’agit du niveau scolaire des **élèves que les enseignants auront à former** dans cette formation)*  

- [ ] Primaire  
- [ ] Collège  
- [ ] Lycée général et technologique  
- [ ] Lycée professionnel  
- [ ] Enseignement supérieur  

👉 `[niveau_scolaire]`

---

## 5️⃣ Niveau d’expertise global des participants adultes  
*(il s’agit des **adultes inscrits à la formation**, et non de leurs élèves ; plusieurs choix possibles)*  

- [ ] Débutant  
- [ ] Intermédiaire  
- [ ] Avancé  
- [ ] Expert ou formateur confirmé  
- [ ] Je ne sais pas encore  

👉 `[niveau_expertise]`

---

## 6️⃣ Besoins spécifiques des participants adultes

### ❓ Des besoins spécifiques sont-ils connus pour ce public adulte ?  
*(il s’agit des **participants à la formation**, et non de leurs élèves)*  

- [ ] Aucun besoin identifié  
- [ ] Préférence pour certaines modalités (oral, écrit, visuel…)  
- [ ] Besoin d’accompagnement ou de soutien (prise en main d’outils, renforcement de la confiance, etc.)  
- [ ] Autre (à préciser) : __________  

ℹ️ Ces informations seront conservées comme repères pour le formateur.  

👉 `[besoins_specifiques]`

---

## 7️⃣ Nombre de participants attendus

- [ ] Moins de 10 personnes  
- [ ] Entre 10 et 20 personnes *(format idéal CMO)*  
- [ ] Entre 21 et 30 personnes *(possible mais demande une animation renforcée)*  
- [ ] Plus de 30 personnes *(déconseillé dans le scénario CMO)*  

👉 `[nombre_participants]`

---

## 8️⃣ Modalités d’animation

- [ ] Un seul formateur  
- [ ] Co-animation (plusieurs formateurs)  

👉 `[modalites_animation]`

---

## 9️⃣ Exigences institutionnelles, restrictions techniques

### ❓ Exigences institutionnelles ou restrictions techniques particulières  
*(cochez si applicable et précisez le cas échéant)*  

- [ ] Aucune exigence / restriction identifiée  
- [ ] Exigence institutionnelle particulière : __________  
  *(ex. validation par l’INSPE, intégration au plan académique de formation, obligations de certification, etc.)*  
- [ ] Restriction technique : __________  
  *(ex. impossibilité d’utiliser la visioconférence, limite de bande passante, pas d’accès à certains outils, contraintes RGPD, etc.)*  

👉 `[exigences_restrictions]`

---

## 🔟 Autre élément important à connaître

*(laisser un espace libre pour tout élément complémentaire jugé utile par le formateur)*  

_________________________________________  
_________________________________________  

👉 `[autre_element]`

---

## ✅ Synthèse à valider

```yaml
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


Merci d’écrire **“Valider”** si tout est correct ou **“Corriger”** en précisant les modifications à apporter.
**Réponse : [à compléter]**