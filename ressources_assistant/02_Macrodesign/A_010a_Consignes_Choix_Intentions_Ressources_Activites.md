[INSTRUCTION_ASSISTANT] :
- **But** : Sélectionner automatiquement, pour chaque section d’apprentissage (S2 à S5), les intentions, ressources et activités à partir :
  - du bloc `ordre_competences` validé (A_008_Organisation_Competences.md),
  - du fichier `R_03_001_Tableau_Activites_Ressources.md` intégré dans la RAG (col.1 = id, col.2 = type, col.3 = nom, col.4 = recommandation),
  - des règles ABC Learning Design.

- **Sélections à produire** :
  - Intention secondaire ABC Learning Design (obligatoire).
  - Ressource principale (obligatoire, 1 seule par section).
  - Activité principale (obligatoire).
  - Activité secondaire (optionnelle si utile).
  - Discussion contextualisée pour le forum.
  - Badge avec formulation fixe : `"Réussite si atteinte du degré 3 (autoévaluation)"`.

- **Règles de filtrage** :
  1. **Priorité par recommandation** :
     - Sélectionner en priorité les éléments **recommandation = 3**.
     - Élargir à recommandation = 2 uniquement si besoin de diversité ou absence d’option pertinente.
  2. **Filtrage par type** :
     - `Ressource` ou `Ressource H5P` pour la ressource principale.
     - `Activité` ou `Activité H5P` pour les activités.
  3. **Externes (SCORM, LTI, etc.)** :
     - Autorisés si valeur pédagogique claire.
     - Fournir au participant les implications (RGPD, hébergement, compatibilité Magistère) dans la justification.
  4. **Contraintes pédagogiques** :
     - Intention “Acquisition” toujours incluse.
     - Activité 1 obligatoire.
     - Activité 2 optionnelle uniquement si valeur ajoutée pédagogique.

- **Procédure** :
  1. Analyser la compétence de la section pour déterminer le type d’engagement (cognitif ou affectif).
  2. Associer l’intention secondaire ABC selon le tableau suivant :

    | Type de compétence | Intention secondaire |
    |--------------------|----------------------|
    | Mémorisation, compréhension | Acquisition (déjà incluse) |
    | Application, entraînement | Entraînement |
    | Restitution, réalisation | Production |
    | Réflexion, posture, point de vue | Discussion |
    | Coopération, co-construction | Collaboration |
    | Exploration, investigation | Enquête |

  3. Filtrer `R_03_001_Tableau_Activites_Moodle_H5P.md` selon les règles ci-dessus.
  4. Pour chaque section S2 à S5, proposer :
     - Ressource principale (avec son `id`).
     - Activité 1 (avec son `id`).
     - Activité 2 (si pertinente, avec son `id`).
     - Discussion contextualisée.
     - Badge fixe.
  5. Justifier chaque choix :
     - Alignement avec la compétence.
     - Pertinence pédagogique.
     - Spécificités ou précautions si ressource externe.

- **Variables internes** :
  - `ordre_competences` ← bloc YAML A_008.
  - `tableur_activites` ← données filtrées du `R_03_001_Tableau_Activites_Moodle_H5P.md`.
  - `choix_section` ← propositions retenues pour chaque section.

- **Étape suivante** :
  - Transmettre ces choix à **A_010B_Contenus_Par_Section.md** pour la génération du tableau final et des justifications visibles pour le participant.
