# Export CMO — Tableur modèle (v5) — **Markdown**

## 01_Généralités — format vertical

| Champ YAML | Valeur à saisir |
|---|---|
| Titre officiel de la formation |  |
| Type de public (enseignants, formateurs, autres) |  |
| Type de formation, niveau scolaire et expertise |  |
| Liste des besoins spécifiques éventuels |  |
| Nombre de participants et modalités d'animation |  |
| Exigences institutionnelles ou restrictions techniques |  |
| Compétences formulées (max 4) |  |

---

## 02_Référentiels — blocs par compétence (sans répétition)

### C1
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif                                                     | indicateur_quantitatif                         |
|---|---|---:|---|---|---|
| C1 | L’enseignant sera capable d’évaluer l’impact des outils numériques sur l’apprentissage et l’inclusion de ses élèves. | 1 | Je débute        | Je repère des éléments clés liés à la compétence.                         | Au moins **25 %** de réussite dans l’activité |
|  |  | 2 | Je progresse     | Je réalise la compétence avec appui (exemples, guide).                     | Au moins **50 %** de réussite dans l’activité |
|  |  | 3 | Je suis autonome | Je réalise la compétence de manière autonome et justifiée.                 | Au moins **75 %** de réussite dans l’activité |
|  |  | 4 | Je maîtrise      | J’adapte la compétence à des contextes variés et j’accompagne mes pairs.  | **100 %** de réussite dans l’activité |

### C2
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif                                                     | indicateur_quantitatif                         |
|---|---|---:|---|---|---|
| C2 | L’enseignant sera capable de collaborer avec ses pairs pour partager des pratiques et co-créer des solutions d’intégration des outils numériques pour l’accessibilité. | 1 | Je débute        | Je repère des éléments clés liés à la compétence.                         | Au moins **25 %** de réussite dans l’activité |
|  |  | 2 | Je progresse     | Je réalise la compétence avec appui (exemples, guide).                     | Au moins **50 %** de réussite dans l’activité |
|  |  | 3 | Je suis autonome | Je réalise la compétence de manière autonome et justifiée.                 | Au moins **75 %** de réussite dans l’activité |
|  |  | 4 | Je maîtrise      | J’adapte la compétence à des contextes variés et j’accompagne mes pairs.  | **100 %** de réussite dans l’activité |

### C3
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif                                                     | indicateur_quantitatif                         |
|---|---|---:|---|---|---|
| C3 | L’enseignant sera capable d’utiliser des outils numériques adaptés pour répondre aux besoins spécifiques de ses élèves. | 1 | Je débute        | Je repère des éléments clés liés à la compétence.                         | Au moins **25 %** de réussite dans l’activité |
|  |  | 2 | Je progresse     | Je réalise la compétence avec appui (exemples, guide).                     | Au moins **50 %** de réussite dans l’activité |
|  |  | 3 | Je suis autonome | Je réalise la compétence de manière autonome et justifiée.                 | Au moins **75 %** de réussite dans l’activité |
|  |  | 4 | Je maîtrise      | J’adapte la compétence à des contextes variés et j’accompagne mes pairs.  | **100 %** de réussite dans l’activité |

### C4 (optionnelle)
| competence_id | competence_formulation | degre | libelle_degre     | indicateur_qualitatif                                                     | indicateur_quantitatif                         |
|---|---|---:|---|---|---|
| C4 | [optionnel] | 1 | Je débute        | Je repère des éléments clés liés à la compétence.                         | Au moins **25 %** de réussite dans l’activité |
|  |  | 2 | Je progresse     | Je réalise la compétence avec appui (exemples, guide).                     | Au moins **50 %** de réussite dans l’activité |
|  |  | 3 | Je suis autonome | Je réalise la compétence de manière autonome et justifiée.                 | Au moins **75 %** de réussite dans l’activité |
|  |  | 4 | Je maîtrise      | J’adapte la compétence à des contextes variés et j’accompagne mes pairs.  | **100 %** de réussite dans l’activité |

---

## 03_Macrodesign — 8 sections CMO (colonnes finales)

> Colonnes conservées : `section_id, type_section, competence_id, competence_formulation, ressource_type, ressource_url, intention_ressource, activite_1_type, activite_1_url, intention_activite_1, activite_2_type, activite_2_url, intention_activite_2, justification_pedagogique, modalite, duree_estimee_min, evaluation_mode`.

| section_id | type_section | competence_id | competence_formulation | ressource_type | ressource_url | intention_ressource | activite_1_type | activite_1_url | intention_activite_1 | activite_2_type | activite_2_url | intention_activite_2 | justification_pedagogique | modalite | duree_estimee_min | evaluation_mode |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---|
| S1 | Accueil |  |  | Page |  | Acquisition |  |  |  |  |  |  | Cadrage et attentes | asynchrone | 10 |  |
| S2 | Apprentissage | C1 | L’enseignant sera capable d’évaluer l’impact des outils numériques sur l’apprentissage et l’inclusion de ses élèves. | Fichier | URL_A_COMPLETER | Acquisition | Quiz | URL_A_COMPLETER | Pratique | Forum | URL_A_COMPLETER | Discussion | La ressource structure l’observation ; les activités mobilisent analyse et justification. | asynchrone | 30 | auto_evaluation_4_degres |
| S3 | Apprentissage | C2 | L’enseignant sera capable de collaborer avec ses pairs pour partager des pratiques et co-créer des solutions d’intégration des outils numériques pour l’accessibilité. | Page | URL_A_COMPLETER | Acquisition | Collaboration | URL_A_COMPLETER | Collaboration | Forum | URL_A_COMPLETER | Discussion | Ressource = cadrage des rôles ; activités = co-construction et feedback pair-à-pair. | asynchrone | 30 | auto_evaluation_4_degres |
| S4 | Apprentissage | C3 | L’enseignant sera capable d’utiliser des outils numériques adaptés pour répondre aux besoins spécifiques de ses élèves. | Fichier | URL_A_COMPLETER | Acquisition | Pratique | URL_A_COMPLETER | Pratique | Étude de cas | URL_A_COMPLETER | Discussion | Ressource = repères et outils ; activités = application concrète et justification du choix. | asynchrone | 30 | auto_evaluation_4_degres |
| S5 | Apprentissage | C4 | [optionnel] | URL | URL_A_COMPLETER | Acquisition | Pratique | URL_A_COMPLETER | Pratique |  |  |  | Consolidation facultative selon besoins. | asynchrone | 30 | auto_evaluation_4_degres |
| S6 | Classe_virtuelle |  |  | BBB |  | Collaboration | Échange |  | Discussion |  |  |  | Accompagnement et approfondissement. | synchrone | 45 |  |
| S7 | Forum |  |  | Forum |  | Discussion |  |  |  |  |  |  | Partage entre pairs et entraide. | asynchrone | 10 |  |
| S8 | Evaluation |  |  | Questionnaire |  | Enquête |  |  |  |  |  |  | Mesure de l’impact et amélioration continue. | asynchrone | 10 | satisfaction |


