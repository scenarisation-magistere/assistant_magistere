# 📊 Comparatif A_007 (révisé) vs Script Python (Guillaume)

## 🎯 Objectif
Aligner le script de génération/ordonnancement des compétences avec les exigences définies dans **A_007_Competences_Visees.md**.

---

## 📝 Tableau comparatif

| Élément | Exigence A_007 (révisé) | Script Python actuel | Écart constaté | Améliorations nécessaires |
|---------|--------------------------|----------------------|----------------|---------------------------|
| **Nombre de compétences** | 2–3 compétences (4ᵉ facultative) | Génère systématiquement **6** compétences | Cardinalité incorrecte | Limiter la génération à **3–4** (paramétrable : 3 par défaut, 4 si besoin) |
| **Domaines obligatoires** | Chaque compétence = **1 verbe cognitif** + **1 verbe affectif** | Un seul champ `niveau` + `verbes_suggere[]` (pas de séparation) | Domaine affectif totalement absent | Ajouter deux sous-structures distinctes : `cognitif {verbe, niveau}` et `affectif {verbe, niveau}` |
| **Niveaux** | Un niveau **par domaine** : Bas / Moyen / Haut (cognitif & affectif) | Un seul champ `niveau` (mélange) | Perte de granularité | Forcer `cognitif.niveau` et `affectif.niveau` séparés |
| **Listes de verbes** | Listes **exhaustives** par niveau fournies (Bloom + Krathwohl) | Aucune validation sur les verbes produits | Risque de verbes hors référentiel | Intégrer un **contrôle** : verbe ∈ liste exhaustive du niveau choisi |
| **Progressivité** | Progression implicite : Bas → Moyen → Haut | `evaluate_and_order_competences` impose progression, mais barème interne erroné (ex. *Créer* classé Moyen) | Erreur de mapping niveaux | Reprendre les tables de verbes/niveaux depuis A_007 pour fiabiliser l’ordonnancement |
| **Compétence complémentaire** | 4ᵉ compétence facultative seulement si besoin | Ajout **obligatoire** d’une compétence complémentaire | Excès de compétences | Ne suggérer une compétence complémentaire **que si un “gap” réel** est détecté |
| **Formulation** | Combiner cognitif + affectif + contexte | Formulation libre basée sur objectif général | Formulations incomplètes / non alignées | Pattern contrôlé : *« [verbe cognitif] … en [verbe affectif] … (contextualisé) »* |
| **Sortie attendue** | Bloc YAML : `formulations_competences: [...]` avec suivi des 2 domaines | JSON puis YAML simplifié, sans séparation cognitif/affectif | Perte des attributs essentiels | Étendre la sortie YAML avec : <br>`cognitif: {verbe, niveau}` <br>`affectif: {verbe, niveau}` |
| **Validation** | Validation à chaque étape, corrections possibles | Aucune validation, température 0.7 (réponses variables) | Risque de réponses incohérentes | Ajouter **validation stricte** + baisser température (0.2–0.3) pour cohérence |
| **Déroulé opératoire** | Questions une à une, corrections, validation finale | Script → génération directe par API | Écart de logique (mais partiellement hors script) | Si intégré côté assistant : respecter déroulé A_007 pour cohérence formateur |

---

## ✅ Synthèse des améliorations prioritaires

1. **Limiter à 3–4 compétences** (jamais 6 fixes).
2. **Séparer cognitif et affectif** dans la structure (`cognitif{verbe,niveau}`, `affectif{verbe,niveau}`).
3. **Appliquer les listes exhaustives** de verbes par niveau (Bloom/affectif).
4. **Corriger le barème** des niveaux (ex. *Créer* = Haut, pas Moyen).
5. **Ne pas imposer** de compétence complémentaire (seulement si gap réel).
6. **Sortie YAML enrichie** : conserver cognitif + affectif dans l’ordonnancement.
7. **Validation stricte** + **température réduite** pour stabilité.

---

## 📌 Exemple de structure attendue (par compétence)

```yaml
competences:
  - code: C1
    intitule: "Analyser l’impact d’outils numériques en adoptant une démarche collaborative"
    cognitif:
      verbe: "analyser"
      niveau: "Moyen"
    affectif:
      verbe: "adopter"
      niveau: "Haut"
    idees_cles: ["numérique", "collaboration", "co-conception"]
    formulation: "Analyser l’impact d’outils numériques en adoptant une démarche collaborative avec les pairs"


