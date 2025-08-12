[INSTRUCTION_ASSISTANT] :
- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.
- Importer automatiquement :
  - `ordre_competences` validé dans **A_008_Organisation_Competences.md** (ordre des sections d’apprentissage S2→S5).
  - `formulations_competences` validées dans **A_007_Competences_Visees.md**.
  - `public_cible.besoins_specifiques` validés dans **A_004_Public_Cible.md**.
- Pour chaque section d’apprentissage :
  1) Annoncer la section et rappeler la compétence associée.
  2) Générer une première version du référentiel avec :
     - 4 degrés de progression (`Je débute`, `Je progresse`, `Je suis autonome`, `Je maîtrise avec aisance`).
     - Pour chaque degré : un **indicateur qualitatif** (type “Je suis capable de…”) et un **indicateur quantitatif** (score, fréquence, action réalisée).
     - Une **adaptation CUA optionnelle** :
       - Si `public_cible.besoins_specifiques` est vide → ne rien afficher.
       - Si au moins un besoin est présent → suggérer **une adaptation par besoin**, en lien avec la compétence visée.  
         *Exemples :*
           - Fatigabilité importante → prévoir des pauses et fractionner la tâche.
           - Troubles des fonctions exécutives → fournir un guide pas-à-pas visuel.
           - Trouble de la vision → proposer un support accessible (police agrandie, contraste renforcé).
     - Un badge **"oui"** si degré 3 atteint.
  3) Demander au formateur s’il valide ou souhaite modifier (Oui/Non).
  4) Si Non : recueillir les modifications, mettre à jour et reproposer.
  5) Une fois validé, enregistrer dans `referentiels_par_section`.
- Après la dernière section :
  - Générer le bloc YAML `referentiels_par_section` dans l’ordre S2→S5.
  - Afficher **Synthèse** + **bloc YAML** + consigne **Valider / Corriger**.
  - Si **Corriger**, ne redemander que les champs visés, mettre à jour YAML et réafficher.
- Passer automatiquement à **A_010_Contenus_Par_Section.md** à validation.

---

# 🧭 A_009 — Référentiels d’auto-évaluation par section

## 🎯 Objectif
Générer un **référentiel d’auto-évaluation clair, progressif et accessible** pour chaque section d’apprentissage, à partir des compétences définies dans **A_008_Organisation_Competences.md**.

Ce prompt s’inscrit dans une double logique pédagogique :  
- **Alignement pédagogique** (*Biggs*) : cohérence entre objectifs, activités et évaluation.  
- **Backward Design** (*Wiggins & McTighe*) : partir des résultats attendus (évaluation) pour concevoir la formation.  

👉 Synthèse modèles pédagogiques : [R_02_001_RC_Modeles_Pedagogiques_Inspirants.md](R_02_001_RC_Modeles_Pedagogiques_Inspirants.md)  

> 📌 Chaque compétence est liée à une ressource et à une activité. Le référentiel vient compléter cet alignement.

---

## 1️⃣ Création interactive du référentiel

Pour la section **[numéro]** – compétence : **[formulation compétence]**  
Voici une première proposition :

| Degré | Libellé                        | Indicateur qualitatif                  | Indicateur quantitatif          | Adaptation CUA (si besoin)              | Badge |
|-------|---------------------------------|------------------------------------------|----------------------------------|------------------------------------------|-------|
| 1     | Je débute                       | …                                        | …                                | … *(si applicable)*                      | non   |
| 2     | Je progresse                    | …                                        | …                                | … *(si applicable)*                      | non   |
| 3     | Je suis autonome                | …                                        | …                                | … *(si applicable)*                      | oui   |
| 4     | Je maîtrise avec aisance        | …                                        | …                                | … *(si applicable)*                      | non   |

Souhaitez-vous conserver cette version ? (Oui/Non)  
**Réponse : [à compléter]**

---

## 2️⃣ Modifications (si besoin)
Si **Non**, indiquez vos modifications pour chaque degré et/ou adaptation CUA.  
**Réponse : [à compléter]**

---

## 3️⃣ Validation
Confirmez-vous ce référentiel pour la section **[numéro]** ? (Oui/Non)  
**Réponse : [à compléter]**

---

## 📦 Bloc YAML final

```yaml
referentiels_par_section:
  - section: 2
    competence: "[formulation compétence 1]"
    adaptation_CUA:
      - besoin: "Fatigabilité importante"
        adaptation: "Prévoir des pauses et fractionner la tâche"
      - besoin: "Troubles des fonctions exécutives"
        adaptation: "Fournir un guide pas-à-pas visuel"
    badge: "oui (si degré 3 atteint)"
    niveaux:
      - degre: 1
        observable_qualitatif: "[...]"
        observable_quantitatif: "[...]"
      - degre: 2
        observable_qualitatif: "[...]"
        observable_quantitatif: "[...]"
      - degre: 3
        observable_qualitatif: "[...]"
        observable_quantitatif: "[...]"
      - degre: 4
        observable_qualitatif: "[...]"
        observable_quantitatif: "[...]"
  - section: 3
    competence: "[formulation compétence 2]"
    adaptation_CUA: []
    badge: "oui (si degré 3 atteint)"
    niveaux:
      - degre: 1
        observable_qualitatif: "[...]"
        observable_quantitatif: "[...]"
      ...
