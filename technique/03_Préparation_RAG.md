# A_000A – Préparation des fichiers de connaissances pour la RAG

[INSTRUCTION_PREPARATION_RAG] :
- **But** : produire des fichiers Markdown prêts pour **découpage automatique** (LangChain/LlamaIndex) et indexation vectorielle.
- **Périmètre** : fichiers de **connaissances** uniquement (pas de consignes d’agent, pas de prompts).

## 1) Format et encodage
- Fichier **`.md`** unique, encodage **UTF-8**, fins de ligne **LF** (Unix).
- **Tableaux** en Markdown natif ; **pas d’images/HTML riches**.
- Extensions proscrites pour l’ingestion : `.pdf`, `.docx`, `.html` (à conserver pour archive uniquement).

## 2) En-tête YAML (obligatoire)
- Placer le YAML **tout en haut**, délimité par `---` au début et à la fin.
- Clés minimales :  
  `id`, `titre`, `type`, `source_titre`, `source_editeur`, `source_date` (YYYY-MM-DD), `langue`, `mots_cles_normalises` (liste), `utilisation_rag`, `version`.
- Conventions : clés en **snake_case**, **dates ISO**, valeurs factuelles (pas de commentaires).

## 3) Corps du document (structure source)
- Titres hiérarchisés : `#`, `##`, `###`.
- **Séparateurs `---`** entre sections majeures.
- **Ancre par section** au niveau `##` : `## [chunk_id] Titre court`.
  - `chunk_id` : **minuscule**, **ASCII**, **snake_case**, **≤ 40 caractères**, **stable** (ex. `rc2015_d1`).
- Contenu **neutre et factuel**. Paragraphes et listes **atomisés**.
- Chaque section doit être **comprise seule** (autosuffisante).

## 4) Nettoyage
- Supprimer les marqueurs techniques et commentaires non utiles :  
  `:contentReference[...]`, commentaires HTML hors ancres de chunk, traces d’outils.
- Éviter le bruit : apartés, digressions, consignes de dialogue.

## 5) Granularité visée (source)
- Viser **150–250 mots** par section (indicatif).  
- Le **découpage final** est réalisé automatiquement par le pipeline.

## 6) Paramètres de split (référence pipeline)
- `chunk_size_tokens: 800`  
- `chunk_overlap_tokens: 120`  
- `split_by: "markdown_headings+separators"`  
- `normalize_whitespace: true`  
- `metadata_from_front_matter: true`

## 7) Contrôles qualité avant ingestion
- Le YAML s’ouvre sans erreur ; dates au format ISO ; encodage UTF-8.
- Chaque `## [chunk_id]` introduit une section autonome.
- Les métadonnées couvrent **source** et **usage RAG**.



