## 🎯 Objectif du prompt

Ce prompt permet à l’assistant de générer **automatiquement les contenus pédagogiques des sections d’apprentissage S2 à S5**, en exploitant :

- le bloc `ordre_competences` issu du prompt `001F_Organisation_Competences.md`,
- les ressources et activités natives Magistère classées dans le fichier `030_Tableau_87_Activites_Moodle_ABC.xlsx`,
- les règles d’intentions pédagogiques du modèle ABC Learning Design.

---

## 🔁 Fonctionnement section par section

Pour chaque section d’apprentissage (S2 à S5), l’assistant :

1. Récupère la compétence correspondante dans l’ordre défini par `001F`.
2. Génère un **titre clair de section**, lié à la compétence.
3. Associe l’intention **“Acquisition”** + une **intention secondaire** (déduite du type de compétence).
4. Sélectionne :
   - une **ressource principale** native Magistère,
   - une **activité 1** obligatoire,
   - une **activité 2** optionnelle (si elle apporte une plus-value pédagogique),
   - une **discussion contextualisée** pour alimenter le forum (section 7),
   - un **badge** standard : "Réussite si atteinte du degré 3 (autoévaluation)".
5. Justifie tous ses choix pédagogiques à la suite du tableau.

---

## 📌 Contraintes à respecter

- Aucune ressource ou activité externe autorisée (Padlet, Genially…)
- Les composants doivent exister nativement dans Magistère/Moodle
- H5P uniquement si validés compatibles
- Acquisition obligatoire dans toutes les sections
- Le badge est toujours présent, avec la **formulation unique** :  
  **"Réussite si atteinte du degré 3 (autoévaluation)"**

---

## 📊 Tableau de sortie complet (sections 1 à 8)

| Section | Titre de la section                         | Compétence visée | Intentions ABC         | Ressource principale         | Activité 1           | Activité 2           | Discussion forum                                  | Badge |
|---------|---------------------------------------------|------------------|-------------------------|------------------------------|----------------------|----------------------|---------------------------------------------------|--------|
| 1       | Bienvenue dans la formation                 | —                | Acquisition             | Page d’accueil               | —                    | —                    | Présentation du parcours, modalités, contacts     | —      |
| 2       | [Titre proposé]                             | [Compétence 1]   | Acquisition + […]       | [Ressource]                  | [Activité 1]         | [Activité 2]         | [Discussion contextualisée]                       | Réussite si atteinte du degré 3 |
| 3       | [Titre proposé]                             | [Compétence 2]   | Acquisition + […]       | [Ressource]                  | [Activité 1]         | [Activité 2]         | [Discussion contextualisée]                       | Réussite si atteinte du degré 3 |
| 4       | [Titre proposé]                             | [Compétence 3]   | Acquisition + […]       | [Ressource]                  | [Activité 1]         | [Activité 2]         | [Discussion contextualisée]                       | Réussite si atteinte du degré 3 |
| 5       | [Titre proposé]                             | [Compétence 4]   | Acquisition + […]       | [Ressource]                  | [Activité 1]         | [Activité 2]         | [Discussion contextualisée]                       | Réussite si atteinte du degré 3 |
| 6       | Classe virtuelle – Mise en pratique collective | —             | Collaboration           | URL vers salle BBB           | —                    | —                    | —                                                 | —      |
| 7       | Forum général – Échanger et approfondir     | —                | Discussion / Collaboration | —                         | Forum                | —                    | Fils de discussion alimentés par S2 à S5          | —      |
| 8       | Évaluation finale et perspectives           | —                | Enquête                  | Sondage Magistère            | —                    | —                    | Questionnaires court / moyen / long terme         | —      |


---

## 📝 Justifications pédagogiques par section

L’assistant doit détailler pour chaque section :

### Section 2 – Justifications
- **Intention secondaire choisie** : [justification]
- **Ressource** : [explication de l’adéquation avec la compétence]
- **Activité 1** : [justification du choix]
- **Activité 2** : [ajoutée ou non, justification]
- **Discussion** : [objectif de la discussion]
- **Badge** : Réussite si atteinte du degré 3

### Section 3 – Justifications
- **Intention secondaire choisie** : [justification]
- **Ressource** : [explication de l’adéquation avec la compétence]
- **Activité 1** : [justification du choix]
- **Activité 2** : [ajoutée ou non, justification]
- **Discussion** : [objectif de la discussion]
- **Badge** : Réussite si atteinte du degré 3

### Section 4 – Justifications
- **Intention secondaire choisie** : [justification]
- **Ressource** : [explication de l’adéquation avec la compétence]
- **Activité 1** : [justification du choix]
- **Activité 2** : [ajoutée ou non, justification]
- **Discussion** : [objectif de la discussion]
- **Badge** : Réussite si atteinte du degré 3

### Section 5 – Justifications
- **Intention secondaire choisie** : [justification]
- **Ressource** : [explication de l’adéquation avec la compétence]
- **Activité 1** : [justification du choix]
- **Activité 2** : [ajoutée ou non, justification]
- **Discussion** : [objectif de la discussion]
- **Badge** : Réussite si atteinte du degré 3

---

## 🔁 Étape finale – Boucle d’itération section par section

Le tableau a été généré automatiquement à partir des compétences visées et des règles ABC Learning Design.  
Vous pouvez à présent **valider ou modifier** les éléments proposés pour chaque section d’apprentissage (S2 à S5).

### 📍 Pour chaque section, 6 éléments peuvent être revus :

1. Titre de la section  
2. Intention secondaire ABC  
3. Ressource principale  
4. Activité 1 obligatoire  
5. Activité 2 optionnelle  
6. Discussion forum

---

### ✅ Section 2 – Révisions

- **Titre proposé** : `[titre section 2]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Intention secondaire** : `[intention secondaire section 2]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Ressource principale** : `[ressource section 2]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 1 (obligatoire)** : `[activité 1 section 2]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 2 (optionnelle)** : `[activité 2 section 2]`  
  → Modifier / Supprimer ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Discussion forum proposée** : `[discussion section 2]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

---
### ✅ Section 3 – Révisions

- **Titre proposé** : `[titre section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Intention secondaire** : `[intention secondaire section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Ressource principale** : `[ressource section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 1 (obligatoire)** : `[activité 1 section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 2 (optionnelle)** : `[activité 2 section 3]`  
  → Modifier / Supprimer ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Discussion forum proposée** : `[discussion section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

---

### ✅ Section 4 – Révisions

- **Titre proposé** : `[titre section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Intention secondaire** : `[intention secondaire section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Ressource principale** : `[ressource section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 1 (obligatoire)** : `[activité 1 section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 2 (optionnelle)** : `[activité 2 section 3]`  
  → Modifier / Supprimer ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Discussion forum proposée** : `[discussion section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

---

### ✅ Section 5 – Révisions

- **Titre proposé** : `[titre section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Intention secondaire** : `[intention secondaire section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Ressource principale** : `[ressource section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 1 (obligatoire)** : `[activité 1 section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Activité 2 (optionnelle)** : `[activité 2 section 3]`  
  → Modifier / Supprimer ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

- **Discussion forum proposée** : `[discussion section 3]`  
  → Modifier ? [Oui / Non]  
  ✏️ Si oui : `_____________________________________`

---

### ✅ Validation finale

Souhaitez-vous valider cette version complète comme **macrodesign finalisé** ?  
- [ ] Oui → Passage au microdesign ou à l’export  
- [ ] Non → Une nouvelle itération est possible ci-dessous

---

## 📦 Bloc YAML de sortie attendu

```yaml
contenus_sections:
  - section: 1
    titre: "[Titre proposé pour la section d’accueil]"
    competence: null
    intentions: ["Acquisition"]
    ressource: "Page d’accueil"
    activite_1: null
    activite_2: null
    discussion: "Présentation du parcours, modalités, contacts"
    badge: null

  - section: 2
    titre: "[Titre proposé section 2]"
    competence: "[Compétence 1]"
    intentions: ["Acquisition", "[Intention secondaire]"]
    ressource: "[Ressource principale]"
    activite_1: "[Activité 1]"
    activite_2: "[Activité 2 (facultative)]"
    discussion: "[Discussion contextualisée]"
    badge: "Réussite si atteinte du degré 3 (autoévaluation)"

  - section: 3
    titre: "[Titre proposé section 3]"
    competence: "[Compétence 2]"
    intentions: ["Acquisition", "[Intention secondaire]"]
    ressource: "[Ressource principale]"
    activite_1: "[Activité 1]"
    activite_2: "[Activité 2 (facultative)]"
    discussion: "[Discussion contextualisée]"
    badge: "Réussite si atteinte du degré 3 (autoévaluation)"

  - section: 4
    titre: "[Titre proposé section 4]"
    competence: "[Compétence 3]"
    intentions: ["Acquisition", "[Intention secondaire]"]
    ressource: "[Ressource principale]"
    activite_1: "[Activité 1]"
    activite_2: "[Activité 2 (facultative)]"
    discussion: "[Discussion contextualisée]"
    badge: "Réussite si atteinte du degré 3 (autoévaluation)"

  - section: 5
    titre: "[Titre proposé section 5]"
    competence: "[Compétence 4]"
    intentions: ["Acquisition", "[Intention secondaire]"]
    ressource: "[Ressource principale]"
    activite_1: "[Activité 1]"
    activite_2: "[Activité 2 (facultative)]"
    discussion: "[Discussion contextualisée]"
    badge: "Réussite si atteinte du degré 3 (autoévaluation)"

  - section: 6
    titre: "[Titre proposé pour la classe virtuelle]"
    competence: null
    intentions: ["Collaboration"]
    ressource: "Lien vers classe virtuelle (BBB)"
    activite_1: null
    activite_2: null
    discussion: null
    badge: null

  - section: 7
    titre: "[Titre proposé pour le forum général]"
    competence: null
    intentions: ["Discussion", "Collaboration"]
    ressource: null
    activite_1: "Forum"
    activite_2: null
    discussion: "Fils issus des discussions des sections S2 à S5"
    badge: null

  - section: 8
    titre: "[Titre proposé pour l’évaluation finale]"
    competence: null
    intentions: ["Enquête"]
    ressource: "Sondage Magistère"
    activite_1: null
    activite_2: null
    discussion: "Questionnaire de satisfaction à 3 temporalités"
    badge: null
```
 


## 📚 Ressources associées
- [001E_Competences_Visées.md] – permet de formuler jusqu’à 4 compétences visées, utilisées dans les sections S2 à S5.
- [001F_Organisation_Competences.md] – détermine l’ordre pédagogique des compétences à affecter aux sections.
- [001H_Consi_pour_choix_ABCLD.md] – fournit les règles pour sélectionner ressources et activités selon les intentions ABC.
- [030_Tableau_87_Activites_Moodle_ABC.xlsx] – base de données de toutes les ressources et activités natives disponibles sur Magistère.