## 🎯 Objectif

Ce prompt permet à l’assistant de sélectionner automatiquement, pour chaque section d’apprentissage (S2 à S5) :
- une **intention secondaire ABC Learning Design** (obligatoire),
- une **ressource principale** native Magistère (obligatoire),
- une **activité principale** (obligatoire),
- une **activité secondaire** (optionnelle mais conseillée si utile),
- une **discussion contextualisée** pour le forum,
- et un **badge** avec la formule fixe :  
  `"Réussite si atteinte du degré 3 (autoévaluation)"`

Ces choix doivent permettre au participant de **s’engager activement** et de s’entraîner jusqu’à **valider le niveau 3 de la compétence visée**.

---

## 📌 Contraintes à respecter

- ✅ Utiliser **uniquement** des composants natifs Moodle/Magistère.
- ✅ Intention **"Acquisition" toujours incluse** dans chaque section.
- ✅ Ressource principale : 1 seule.
- ✅ Activité 1 obligatoire, Activité 2 optionnelle (si elle apporte une valeur ajoutée pédagogique).
- ⚠️ Ressources externes type Padlet, Genially, etc. **non conseillées** dans ce scénario. Préférer les ressources internes natives de Magistère pour garantir la portabilité et la stabilité.
- ❌ Ne pas proposer deux ressources dans une même section.

---

## 🧭 Étapes détaillées à suivre pour chaque section (S2 à S5)

### 🔹 Remarque sur le modèle pédagogique global

Le scénario choisi repose sur le **modèle hybride de la Communauté Magistère Occitanie**, qui valorise une alternance équilibrée entre les intentions pédagogiques suivantes :
- Acquisition (obligatoire dans chaque section),
- Entraînement,
- Discussion,
- Collaboration.

👉 Le choix des intentions secondaires pour chaque section doit :
- être **cohérent avec la compétence visée** (priorité),
- mais aussi **contribuer à l’équilibre global du parcours**.

📌 Cet équilibre général peut être intégré dans les **justifications pédagogiques** produites par l’assistant.

---

### 1. Analyser la compétence

Identifier le **type d'engagement cognitif ou affectif** attendu.  
Cela permet de déduire l’**intention secondaire ABC Learning Design** à associer :

| Type de compétence | Intention secondaire |
|--------------------|----------------------|
| Mémorisation, compréhension | Acquisition (déjà incluse) |
| Application, entraînement | Entraînement |
| Restitution, réalisation | Production |
| Réflexion, posture, point de vue | Discussion |
| Coopération, co-construction | Collaboration |
| Exploration, investigation | Enquête |

🎯 L’intention secondaire est **obligatoire**.  
Une **3e intention (optionnelle)** peut être ajoutée **si une activité 2 est sélectionnée** pour la développer.

---

### 2. Filtrer dans le tableau ABC les éléments compatibles

Utiliser le fichier :  
📎 `030_Tabl_Activites_Moodle_ABC.md`

Ce tableau est structuré comme suit :

| Colonne     | Contenu |
|-------------|---------|
| Intention   | Intention pédagogique ABC associée |
| Type        | Ressource / Activité / Activité H5P / Ressource H5P |
| Nom         | Nom à afficher dans le YAML/tableau de sortie |
| Description | Courte description |
| Exemple     | Exemple pédagogique |
| Lien        | Lien vers le tutoriel Magistère |
| Intérêt     | Niveau d’intérêt pédagogique (1 = faible, 3 = fort) |

📌 **Remarques importantes sur la colonne `Type`** :
- `Activité H5P` doit être **considérée comme une activité** dans la logique du prompt.
- `Ressource H5P` doit être **considéré comme une ressource**, au même titre qu’une page ou un livre.

⚠️ Ne sélectionner que les lignes :
- dont l’intention ABC **contient l’intention cible**,
- dont le **type correspond** (ressource ou activité),
- dont le **niveau d’intérêt** est de préférence 2 ou 3.

📘 La ressource **Page** est généralement la plus adaptée pour introduire un contenu dans Magistère.


---

### 3. Proposer les composants pédagogiques

- **Ressource principale** (ex. : Page, Livre, Fichier, Vidéo)
- **Activité 1** : alignée sur l’intention secondaire, favorise la **pratique directe**
- **Activité 2** : optionnelle, si elle :
  - complète sans redondance l’activité 1,
  - enrichit pédagogiquement la séquence,
  - diversifie les modalités d’engagement
- **Discussion** : contextualisée, en lien direct avec la compétence
- **Badge** : avec formulation fixe `"Réussite si atteinte du degré 3 (autoévaluation)"`

---

### 4. Justifier chaque choix

L’assistant doit justifier chaque choix selon les critères suivants :

| Élément         | Justification attendue |
|----------------|-------------------------|
| Intention secondaire | Alignée avec la compétence et adaptée à la montée en complexité |
| Ressource principale | Apport structuré, accessible, adapté au public |
| Activité 1 | Mobilise activement la compétence (niveau 2 ou 3 attendu) |
| Activité 2 | (si présente) Introduit un renforcement, une variation utile |
| Discussion | Sert à verbaliser, co-construire ou réfléchir sur la tâche |
| Badge | Permet de baliser l’engagement et valoriser l’effort accompli |

---

## 🎛️ Résumé des règles de sélection

| Élément       | Obligatoire | Nombre autorisé | Sélection prioritaire |
|---------------|-------------|------------------|------------------------|
| Intention ABC | Oui         | min. 2, max. 3   | Intention secondaire déduite + Acquisition |
| Ressource     | Oui         | 1 seule          | De type “Ressource”, intérêt ≥ 2 |
| Activité      | Oui (1), Optionnelle (2) | 1 ou 2 | De type “Activité”, intérêt ≥ 2 |
| Discussion    | Oui         | 1                | En lien avec la compétence visée |
| Badge         | Oui         | 1 (fixe)         | Formule standardisée |

---

## 📚 Ressources associées
- `030_Tabl_Activites_Moodle_ABC.md` – tableau markdown lisible des ressources et activités natives Magistère, avec niveaux d’intérêt et intentions ABC associées.
- `001H_Contenus_Par_Section.md` – prompt déclencheur du présent script, qui active ce traitement pour chaque section d’apprentissage.

---

🚀 Ce prompt est utilisé **automatiquement** dans la boucle du prompt `001H_Contenus_Par_Section.md`, mais peut également être déclenché indépendamment.




