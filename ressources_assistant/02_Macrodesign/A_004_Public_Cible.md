<!-- Instructions pour l'assistant -->

[INSTRUCTION_ASSISTANT] :
- Ce fichier sert à **identifier le public cible** de la formation. L'assistant doit poser **une question à la fois**, attendre la réponse du formateur, puis passer à la suivante.
- **Après chaque question**, l’assistant doit s’arrêter et attendre que le formateur fournisse sa réponse avant de passer à la question suivante.
- L’assistant **ne doit pas afficher toutes les questions en même temps**. Il doit poser chaque question **une par une**.
- L’assistant doit **générer la synthèse YAML** après que le formateur ait répondu à toutes les questions et validé la synthèse.

---

## Objectif

Déterminer les caractéristiques du public cible de la formation.  
Ces éléments permettront à l’assistant d’adapter finement ses propositions pédagogiques.

---

## 🧭 Déroulement

Je vais te poser une série de **6 questions** pour identifier précisément le public cible de ta formation.  
Merci de répondre à chacune d’elles, **une à une**. Une synthèse te sera proposée à la fin pour validation.

---

### 🔹 Question 1/6 : Quel est le **titre (ou projet de titre)** de ta formation ?  
📝 *Exemple*  
  Développer les compétences orales en classe hétérogène  
  Améliorer la gestion de classe avec les outils numériques  
  Développer des compétences orales en classe hétérogène  

👉 Ta réponse : `[titre_formation]`

---

➡️ Lorsque tu m’auras donné ta réponse, je te poserai la question suivante.

---

### 🔹 Question 2/6 : Quel est l’**objectif général** de cette formation ?  
**Exemples** :  
  Accompagner les enseignants à concevoir et animer des activités permettant aux élèves de s’exprimer oralement avec confiance et clarté.  
  Accompagner les enseignants dans l'utilisation des outils numériques pour améliorer la gestion de la classe et favoriser l'engagement des élèves.  
  Former les enseignants à l'animation de discussions et de débats en classe en utilisant des ressources multimédia adaptées.

👉 Ta réponse : `[objectif_general]`

---

### 🔹 Question 3/6 : Quel est le **type de public visé** ? (plusieurs réponses possibles)  
👉 Coche ou indique toutes les catégories qui s’appliquent :

- Enseignants 1er degré  
- Enseignants 2d degré  
- Formateurs académiques  
- Formateurs INSPE / chercheurs  
- Inspecteurs  
- Équipes pluri-catégorielles  
- Autre (à préciser)

👉 Ta réponse : `[type_de_public]`

---

### 🔹 Question 4/6 : Quel est le **niveau d’expertise** global du public visé ?  
👉 Choisis 1 ou 2 options :

- Débutant  
- Intermédiaire  
- Avancé  
- Expert ou formateur confirmé  
- Je ne sais pas encore

👉 Ta réponse : `[niveau_expertise]`

---

### 🔹 Question 5/6 : Le groupe est-il **homogène ou hétérogène** ?  
👉 Coche ou indique ce qui te semble le plus proche :

- Groupe homogène (mêmes profils, mêmes besoins)  
- Groupe hétérogène  
- Je ne sais pas encore

👉 Ta réponse : `[profil_groupe]`

---

### 🔹 Question 6/6 : Des **besoins spécifiques** sont-ils connus pour ce public ?  
👉 Décris les besoins identifiés chez tes participants ou formateurs :

- Aucun besoin identifié  
- Préférence pour certaines modalités (oral, écrit, visuel…)  
- Besoins liés à l'accessibilité (supports adaptés, ajustements pour mieux comprendre et participer)  
- Besoins spécifiques d’accompagnement dans certaines compétences ou outils (par exemple, pour renforcer la confiance dans l’utilisation du numérique, etc.)

👉 Ta réponse : `[besoins_specifiques]`

---

## ✅ Synthèse à valider

Voici une synthèse générée à partir de tes réponses. Merci de vérifier :

```yaml
public_cible:
  type: [ "[type_de_public]" ]
  profil: "[profil_groupe]"
  niveau_expertise: "[niveau_expertise]"
  besoins_specifiques:
    - "[besoin_1]"
    - "[besoin_2]"
  recommandations:
    - "[à compléter ou à reformuler en fonction du profil et des besoins]"
contexte_formation:
  titre: "[titre_formation]"
  objectif_general: "[objectif_general]"
