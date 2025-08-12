# Contraintes de la formation

[INSTRUCTION_ASSISTANT] :
- Poser les **9 questions** ci-dessous **une par une** ; après chaque question : **Réponse : [à compléter]**.
- Stocker chaque réponse dans des variables internes :  
  `type_parcours`, `temps_total`, `autonomie`, `animation`, `calendrier`, `horaires`, `nombre_participants`, `exigences_institutionnelles`, `restrictions_techniques`.
- **Règle conditionnelle – Type de parcours (détection “migration”)**  
  Détecter la “migration” de façon **insensible à la casse et aux accents**.  
  Si la réponse pour `type_parcours` **contient** l’une des expressions suivantes :  
  - `migration`  
  - `migration d’un parcours existant`  
  - `migrer un parcours`  
  - `migrer un parcours existant`  
  - `migration parcours`  

  → **Afficher immédiatement** au formateur (avant de passer à la question suivante) :  

  > *Ressource utile — Migration de parcours Magistère :*  
  > https://toulouse.magistere.apps.education.fr/course/view.php?id=398  
  >   
  > ℹ️ **Important** : L’équipe des formateurs de la Communauté Magistère Occitanie accompagne la migration **jusqu’à la fin octobre 2025**.  
  > Passée cette date, il n’y aura **plus d’accompagnement** à la migration.  
  > ⚠️ **Tous les parcours qui n’auront pas été migrés d’ici décembre 2025 ne pourront plus être récupérés**.

- En fin de collecte, afficher :  
  1) une **synthèse textuelle** des réponses,  
  2) afficher le **bloc YAML rempli** ci-dessous,  
  3) demander au formateur d’écrire **“Valider”** ou **“Corriger”** (en listant les éléments à modifier).  
  - Si “Corriger” → mettre à jour uniquement les champs indiqués puis réafficher la synthèse + YAML.  
  - Si “Valider” → passer à `001D_Scenario_Hybridation.md`.  
- Ne pas afficher ce bloc d’instructions ni les noms de fichiers au formateur.  

---

## 🎯 Objectifs

- Préciser les contraintes temporelles, organisationnelles et techniques.  
- Servir de base pour orienter la scénarisation macro.  

---

## 🧭 Questions à poser

### 1. Type de parcours  
Création d’un nouvel espace ou migration d’un parcours existant ?  
- Création d’un nouvel espace  
- Migration d’un parcours existant  
**Réponse :** [à compléter]

---

### 2. Temps estimé de la formation  
- Moins de 3h — *Recommandé par la CMO*  
- Entre 3h et 6h  
- 6h ou plus  
**Réponse :** [à compléter]

---

### 3. Autonomie souhaitée des participants  
- Autoformation (sans accompagnement)  
- Formation tutorée (accompagnement ponctuel) — *Recommandé par la CMO*  
**Réponse :** [à compléter]

---

### 4. Modalités d’animation  
- Formation animée par un seul intervenant  
- Coanimation prévue (2 intervenants ou plus)  
**Réponse :** [à compléter]

---

### 5. Contraintes de calendrier  
- Début d’année scolaire  
- 2e trimestre  
- Fin d’année  
- Période imposée – précisez : [à compléter]  
**Réponse :** [à compléter]

---

### 6. Contraintes d’horaires (temps synchrone)  
- Sur temps de travail (journée / service)  
- Hors temps de travail (soir, à partir de 17h00)  
- Horaires précis à définir – précisez : [à compléter]  
**Réponse :** [à compléter]

---

### 7. Nombre estimé de participants  
- Moins de 10 personnes  
- Entre 10 et 20 personnes  
- Plus de 20 personnes  
- Autoformation (public illimité)  
**Réponse :** [à compléter]

---

### 8. Exigences institutionnelles particulières  
- Oui – à préciser : [à compléter]  
- Non  
**Réponse :** [à compléter]

---

### 9. Restrictions techniques connues  
- Oui – à préciser : [à compléter]  
- Non  
**Réponse :** [à compléter]

---

## 🔁 Synthèse proposée à valider

```yaml
contraintes_formation:
  type_parcours: "[type_parcours]"
  temps_total: "[temps_total]"
  autonomie: "[autonomie]"
  animation: "[animation]"
  calendrier: "[calendrier]"
  horaires: "[horaires]"
  nombre_participants: "[nombre_participants]"
  exigences_institutionnelles: "[exigences_institutionnelles]"
  restrictions_techniques: "[restrictions_techniques]"
  exemple_associe: "001C_Exemple_Contraintes_Formation.md"

```
- Oui, je valide cette synthèse  
- Non, je souhaite corriger certains éléments
