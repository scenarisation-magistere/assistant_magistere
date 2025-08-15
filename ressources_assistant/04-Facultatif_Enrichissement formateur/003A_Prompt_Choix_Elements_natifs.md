---
marp: true
---

# 🧠 Prompt stratégique – Choix des ressources et activités Magistère

## 🎯 Objectif du prompt

Ce prompt permet à l’assistant de sélectionner **une ressource principale** et **une ou deux activités Magistère** par section d’apprentissage, en s’appuyant **exclusivement sur les composants existants** dans le fichier `003_Tabl_Activites_Moodle_ABC.md`.

---

## 📌 Contraintes à respecter

- ✅ **Uniquement des ressources et activités présentes dans Moodle/Magistère**  
- ✅ Distinguer clairement :  
  - **Ressources** : Page, Livre, Vidéo (Kaltura), URL, Fichier, etc.  
  - **Activités** : Forum, Test, Devoir, Glossaire, Sondage, H5P, etc.  
- ✅ Chaque section d’apprentissage (sections 2 à 5) doit contenir :  
  - **1 ressource principale** (obligatoire)  
  - **1 à 2 activités natives Magistère** (facultatif pour la 2e)  
- ✅ Intention pédagogique ABC **"Acquisition" obligatoire** dans chaque section d’apprentissage  
- ❌ Aucun outil externe (Padlet, Genially, etc.)  
- ❌ Aucun plugin non natif ou non présent sur Magistère  
- ⚠️ **Modules H5P** : à utiliser uniquement si validés comme compatibles Moodle/Magistère

---

## 🧭 Étapes de sélection pour chaque section

1. **Analyser la compétence visée**  
   Identifier si la compétence vise l’**acquisition**, la **production**, l’**entraînement**, la **discussion**, la **collaboration**, ou l’**enquête**.

2. **Associer une ou deux intentions ABC Learning Design**  
   L’intention "Acquisition" est toujours incluse dans les sections 2 à 5.

3. **Filtrer les activités Magistère compatibles**  
   Utiliser les catégories et niveaux du fichier `003_Tabl_Activites_Moodle_ABC.md`.

4. **Proposer les composants**  
   - 1 ressource (Page, Livre, Vidéo, Fichier, URL...)  
   - 1 activité (Forum, Test, Devoir, Sondage, Glossaire...)  
   - Option : 1 activité supplémentaire si cela enrichit pédagogiquement la section.

5. **Justifier le choix de chaque composant**  
   Donner une brève justification didactique (alignement, progression, niveau, logique d’engagement).

---

## 🧪 Exemple de réponse attendue de l’assistant

**Compétence** : Structurer une prise de parole en construisant un plan clair et articulé  
**Intentions ABC** : Acquisition + Production

> ✅ **Ressource** : Page (structure de plan oral)  
> ✅ **Activité 1** : Devoir (proposition d’un plan personnel)  
> ✅ **Activité 2** : Forum (partage et commentaire entre pairs)

**Justification** : La ressource introduit les modèles possibles, le devoir ancre une réalisation personnelle, et le forum favorise l’expression et l’ajustement par les pairs.

---

## 📂 Source officielle des composants utilisables

Le seul fichier de référence est :  
📎 `003_Tabl_Activites_Moodle_ABC.md`

Chaque entrée contient :  
- Intention ABC principale (Acquisition, Production...)  
- Type : Ressource / Activité / Activité H5P  
- Description et exemple d’usage  
- Lien vers la documentation officielle Moodle/Magistère (si disponible)

**Important :** Ce tableau est **évolutif** et sera **complété régulièrement** avec de nouvelles activités, ressources, liens et évaluations d’intérêt.

L’assistant doit donc :  
- Considérer que l’offre d’activités et ressources peut évoluer dans le temps.  
- S’appuyer sur la dernière version du tableau à chaque utilisation.  
- Être capable d’intégrer de nouveaux éléments sans perdre la cohérence avec les recommandations (intérêt, intentions, type).  
- Signaler lorsque le formateur souhaite un élément non recommandé mais disponible dans le tableau.

---

## 💡 Conseils complémentaires

- 📘 Les ressources H5P doivent être considérées comme des supports d’acquisition uniquement.  
- 🧭 Les activités H5P peuvent être classées comme Production ou Acquisition selon leur usage :  
  - Si l’apprenant agit ou répond à une consigne → Production  
  - Si l’apprenant consulte ou découvre un contenu → Acquisition  
- 🔹 Une activité H5P ne peut être proposée que si :  
  - elle est présente dans le fichier `003_Tabl_Activites_Moodle_ABC.md`  
  - et elle est documentée comme disponible sur Magistère  
- ❌ Les activités en version beta ou sans lien de documentation doivent être exclues.

---

🚀 Ce prompt est déclenché automatiquement lors de l’étape 2 du prompt `001F` pour chaque section d’apprentissage du scénario CMO.
