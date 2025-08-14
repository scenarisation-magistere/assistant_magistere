[INSTRUCTION_ASSISTANT] :
- **But** : Générer automatiquement, pour les sections S2 à S5, un tableau complet des contenus pédagogiques à partir :
  - du bloc `ordre_competences` validé (A_008_Organisation_Competences.md),
  - du fichier Markdown `R_03_001_Tableau_Activites_Ressources.md` (col.1 = id, col.2 = type, col.3 = nom, col.4 = recommandation),
  - des règles ABC Learning Design (A_010a_Consignes_Choix_Intentions_Ressources_Activites.md).

- **Règles de sélection** :
  1. **Filtrage par priorité** :
     - Priorité aux entrées avec `recommandation = 3`.
     - Si besoin de diversité ou absence d’option pertinente, élargir à `recommandation = 2`.
  2. **Filtrage par type** :
     - Ressource principale : `Ressource` ou `Ressource H5P`.
     - Activités : `Activité` ou `Activité H5P`.
  3. **Externes (SCORM, LTI, etc.)** :
     - Autorisés si pertinence pédagogique claire.
     - Indiquer dans la justification toute implication importante (RGPD, hébergement, compatibilité Magistère).
  4. **Contraintes pédagogiques** :
     - “Acquisition” toujours incluse comme intention.
     - Activité 1 obligatoire.
     - Activité 2 optionnelle uniquement si valeur ajoutée pédagogique.

- **Procédure interne** :
  1. Identifier l’intention secondaire ABC pour chaque compétence selon le tableau suivant :

    | Type de compétence | Intention secondaire |
    |--------------------|----------------------|
    | Mémorisation, compréhension | Acquisition (déjà incluse) |
    | Application, entraînement | Entraînement |
    | Restitution, réalisation | Production |
    | Réflexion, posture, point de vue | Discussion |
    | Coopération, co-construction | Collaboration |
    | Exploration, investigation | Enquête |

  2. Filtrer `R_03_001_Tableau_Activites_Moodle_H5P.md` selon le type et la recommandation.
  3. Pour chaque section S2 à S5, sélectionner :
     - Ressource principale (avec `id`).
     - Activité 1 (avec `id`).
     - Activité 2 optionnelle (avec `id` si choisie).
     - Discussion contextualisée.
     - Badge fixe : `"Réussite si atteinte du degré 3 (autoévaluation)"`.
  4. Justifier chaque choix pour le participant :
     - Alignement avec la compétence.
     - Pertinence pédagogique.
     - Spécificités / précautions si ressource externe.

- **Variables internes** :
  - `ordre_competences` ← bloc YAML A_008.
  - `tableur_activites` ← contenu du `R_03_001_Tableau_Activites_Moodle_H5P.md`.
  - `contenus_sections` ← tableau final généré.

- **Sorties attendues** :
  - Tableau Markdown complet (sections 1 à 8).
  - Bloc YAML `contenus_sections` conforme au format attendu par A_011_Generation_Recap_Macrodesign.md.
  - Justifications pédagogiques détaillées pour S2 à S5.

- **Étape suivante après validation** :
  - Passer à A_011_Generation_Recap_Macrodesign.md pour assemblage final et export.
