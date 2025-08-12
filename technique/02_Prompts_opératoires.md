# 📄 Instruction – Gestion des prompts opératoires de l’Assistant IA

## 1. Définition
Les **prompts opératoires** pilotent le fonctionnement interne de l’assistant IA.  
Ils orchestrent les étapes, posent des questions au formateur et appliquent des règles conditionnelles.

## 2. Caractéristiques
- Contiennent un bloc `[INSTRUCTION_ASSISTANT]` décrivant :
  - L’ordre des questions ou actions.
  - Les variables internes à renseigner.
  - Les règles conditionnelles à appliquer.
  - Les étapes suivantes à déclencher.
- Peuvent inclure des séparateurs `---` pour structurer la lisibilité interne.
- Ne contiennent **aucun contenu documentaire** à destination du formateur en dehors de la séquence prévue.

## 3. Format
- **Pas** de front-matter YAML RAG.
- **Pas** de balise `## [chunk_id]`.
- **Pas** d’intégration dans la base RAG.
- Maintenir un format clair et cohérent entre tous les prompts.

## 4. Stockage
- Dossier conseillé : 📂 `/prompts_operatoires`
- Nommer les fichiers selon l’ordre de la séquence et leur rôle, par ex. :
  - `001C_Contraintes_Formation.md`
  - `A_002_Role_Assistant_Etapes.md`

## 5. Bonnes pratiques
- Toujours tester la logique de question/réponse avant intégration dans l’assistant IA.
- S’assurer que les références à d’autres fichiers (ex. passage à l’étape suivante) sont correctes et correspondent à l’arborescence réelle.
- Tenir à jour les instructions internes si le flux de conception évolue.


