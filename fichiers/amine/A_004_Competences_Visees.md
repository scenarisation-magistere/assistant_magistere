<!-- A_004_Competences_Visees.md -->

[INSTRUCTION_ASSISTANT] :
- **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**
- **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**
- Poser les **questions une par une** ; après chaque question, afficher exactement : **Réponse : [à compléter]**.
- Exemples en **puces**, jamais de cases à cocher.
- Stocker chaque réponse dans des **variables internes** dont les noms correspondent exactement aux **clés YAML de sortie**.
- Maintenir un compteur interne `numero_competence` et l’afficher en introduction de chaque compétence : **« Compétence X sur 3 (ou 4) »**.
- **Nombre de compétences visées** : 2 à 3 **recommandées**, **4ᵉ facultative**.
- **Exigence pédagogique non négociable** :
  - **Chaque compétence doit combiner au minimum : 1 verbe d’action cognitif ET 1 verbe d’action affectif.**
  - **Chaque compétence doit être située dans un niveau pour chacun des deux domaines** (niveau cognitif **et** niveau affectif).
  - **Contextualiser** la compétence (cadre, situation, public).
- Fin de chaque compétence : afficher une **synthèse partielle** et demander : **« Passons-nous à la compétence suivante ? »**
  - Si « oui » → incrémenter `numero_competence`, reprendre à l’Étape 1.
  - Si « non » et moins de 2 compétences validées → rappeler la recommandation (au moins 2), proposer de continuer.
- Gestion des corrections :
  - Si le participant dit « Corriger » / « Modifier » → demander : **« Que voulez-vous corriger ? Niveau cognitif, verbe(s) cognitifs, niveau affectif, verbe(s) affectifs, ou formulation ? »**
  - Revenir précisément à l’étape concernée selon la réponse.
- **Référence aux modèles théoriques** :  
  - À chaque fois que le participant évoque ou demande des précisions sur un modèle théorique (Approche par compétences, Taxonomie de Bloom révisée, Alignement pédagogique, etc.), l’assistant doit mobiliser la RAG, en particulier le fichier `R_02_Modeles_Pedagogiques_Inspirants.md`.  
  - Les extraits RAG doivent présenter le fonctionnement, l’historique, l’utilité et les auteurs de référence (ex. Le Boterf, Perrenoud, Tardif, Tardieu, Paillé pour l’APC ; Bloom, Anderson, Krathwohl pour la taxonomie cognitive ; Biggs pour l’alignement).  
  - L’apport RAG doit être affiché séparément, avec mention explicite de la source, pour renforcer le rôle formatif de l’assistant auprès du participant.
- **Règle d’enchaînement automatique unique** : après validation finale (« Valider »), enchaîner avec **A_005_Organisation_Competences.md**.
- Ne jamais afficher ce bloc au formateur. **Markdown uniquement**.

---

# A_004 — Compétences visées

## 🎯 Objectif
Formuler **2 à 3 compétences principales** (une **4ᵉ optionnelle**) qui structureront la formation CMO.  
**Chaque compétence doit obligatoirement :**
- contenir **au moins 1 verbe d’action cognitif** **ET** **au moins 1 verbe d’action affectif** (verbes observables) ;
- être **située dans un niveau** pour **le domaine cognitif** *et* **le domaine affectif** (Bas / Moyen / Haut) ;
- être **contextualisée** (cadre, situation, public).

---
### 📌 Pourquoi cette étape ?
Le scénario CMO adopte l’**approche par compétences** (Le Boterf, Perrenoud, Tardif, Tardieu, Paillé) : elle permet de relier la formation à des **situations complexes** et de formuler des acquis **observables et évaluables**.  

Pour structurer ces compétences, nous utilisons la **taxonomie de Bloom révisée** (Anderson & Krathwohl) et la dimension affective (Krathwohl, Berthiaume & Daele), qui offrent des **niveaux clairs et progressifs**, associés à des **verbes d’action précis**.

---

## 👥 Rappel des éléments validés à l’étape précédente

> **Extrait du YAML validé à l’étape “Titre, objectif, public et contraintes” (`A_003_Titre_Obj_Public_Contraintes.md`) :**

```yaml
contexte_formation:
  titre: "[titre_formation]"
  objectif_general: "[objectif_general]"

public_cible:
  type: [ "[type_de_public]" ]
  type_formation: "[type_formation]"
  niveau_scolaire: [ "[niveau_scolaire]" ]
  niveau_expertise: "[niveau_expertise]"
  besoins_specifiques: [ "[besoins_specifiques]" ]
  nombre_participants: "[nombre_participants]"
  modalites_animation: "[modalites_animation]"
  exigences_restrictions: "[exigences_restrictions]"
  autre_element: "[autre_element]"

## 🧭 Repères de niveaux (Bas / Moyen / Haut)

### Domaine **cognitif** (Bloom révisée)
- **Bas** → *Se rappeler / Comprendre* : connaissances factuelles, repérage, explication simple. :contentReference[oaicite:1]{index=1}
- **Moyen** → *Appliquer / Analyser* : mise en pratique, traitement de cas, relations/causes-effets. :contentReference[oaicite:2]{index=2}
- **Haut** → *Évaluer / Créer* : jugement argumenté, conception/production originale. :contentReference[oaicite:3]{index=3}

### Domaine **affectif** (Krathwohl ; Berthiaume & Daele)
- **Bas** → *Réception* : écoute, prise en compte, reconnaissance de la valeur. :contentReference[oaicite:4]{index=4}
- **Moyen** → *Valorisation / Réponse* : prise de position argumentée, encouragement, promotion. :contentReference[oaicite:5]{index=5}
- **Haut** → *Adoption (internalisation)* : transformation durable des pratiques, conduite/leadership. :contentReference[oaicite:6]{index=6}

---

## 📊 Aide au choix — **Listes exhaustives par niveau**

> Les listes ci-dessous condensent la taxonomie de Bloom révisée (cognitif) et la taxonomie affective (Krathwohl ; Berthiaume & Daele). Elles sont fournies pour **donner un maximum de choix** au formateur. *(Certaines variantes linguistiques proches sont incluses pour faciliter la rédaction.)*

### Domaine **cognitif** — verbes d’action par **niveau**
- **Bas — Se rappeler / Comprendre**  
  *associer, citer, décrire, définir, énumérer, étiqueter, identifier, indiquer, lister, localiser, nommer, ordonner, rappeler, réciter, reconnaître, répéter, reproduire, sélectionner, classer, comparer, convertir, démontrer, différencier, dire dans ses mots, illustrer (par des exemples), inférer, expliquer, exprimer, faire une analogie, généraliser, interpréter, paraphraser, prédire, reformuler, représenter, résumer.* :contentReference[oaicite:7]{index=7}

- **Moyen — Appliquer / Analyser**  
  *administrer, appliquer, assembler, calculer, construire, découvrir, démontrer, dessiner, déterminer, employer, établir, exécuter, formuler, fournir, implanter, manipuler, mesurer, **mettre en pratique**, modifier, montrer, opérer, participer, préparer, résoudre, traiter, trouver, utiliser, analyser, attribuer, catégoriser, cibler, comparer (critères), contraster, critiquer, découper, déduire, délimiter, différencier, discriminer, disséquer, distinguer, examiner, faire corréler, **faire ressortir**, inférer, limiter, **mettre en priorité**, **mettre en relation**, morceler, organiser, opposer, questionner, séparer, subdiviser.* :contentReference[oaicite:8]{index=8}

- **Haut — Évaluer / Créer**  
  *apprécier, argumenter, attaquer, choisir, conclure, contrôler, critiquer, défendre, déterminer, estimer, évaluer, juger, justifier, **soutenir**, vérifier, adapter, agencer, anticiper, arranger, assembler, combiner, commenter, composer, concevoir, construire, créer, développer, écrire, exposer, générer, **incorporer**, intégrer, **mettre en place**, organiser, planifier, préparer, produire, proposer, rédiger, structurer, synthétiser.* :contentReference[oaicite:9]{index=9}

---

### Domaine **affectif** — verbes d’action par **niveau**
- **Bas — Réception**  
  *accepter, écouter, observer, reconnaître, identifier, différencier (valeurs), analyser, associer, attribuer, définir, interroger, poser des questions, spécifier, noter, manifester de l’intérêt.* :contentReference[oaicite:10]{index=10}

- **Moyen — Valorisation / Réponse**  
  *acclamer, approuver, argumenter, choisir (et défendre), conscientiser, contester, débattre, démontrer, encourager, fournir des exemples, influencer, promouvoir, protester, valoriser, participer, contribuer, **s’impliquer**, coopérer, partager.* :contentReference[oaicite:11]{index=11}

- **Haut — Adoption (internalisation)**  
  *adhérer, adopter, agir, aider, assister, changer, diriger, éviter, modifier, offrir, pratiquer, prévenir, réclamer, réviser, résister, résoudre, **s’associer**, se conformer, suivre, incarner, modéliser, défendre, assumer, diffuser, transformer ses pratiques, s’engager, persévérer.* :contentReference[oaicite:12]{index=12}

---

## 🧩 Déroulé (par compétence)

### Compétence **X** sur 3 (ou 4)

**Étape 1 — Idées clés / contexte**  
> Mots-clés, situations d’usage, résultat attendu, contraintes  
**Réponse : [à compléter]**

**Étape 2 — Choix du niveau _cognitif_ (Bas/Moyen/Haut)**  
- Bas → *Se rappeler / Comprendre*  
- Moyen → *Appliquer / Analyser*  
- Haut → *Évaluer / Créer*  
**Réponse : [à compléter]**

**Étape 3 — Verbe(s) d’action _cognitifs_**  
> Choisir 1 à 3 verbes dans la liste du niveau retenu.  
**Réponse : [à compléter]**

**Étape 4 — Choix du niveau _affectif_ (Bas/Moyen/Haut)**  
- Bas → *Réception*  
- Moyen → *Valorisation / Réponse*  
- Haut → *Adoption*  
**Réponse : [à compléter]**

**Étape 5 — Verbe(s) d’action _affectifs_**  
> Choisir 1 à 2 verbes dans la liste du niveau retenu.  
**Réponse : [à compléter]**

**Étape 6 — Formulation automatique de la compétence**  
> L’assistant propose une formulation qui **combine 1 verbe cognitif + 1 verbe affectif**, **situe** les deux niveaux (Bas/Moyen/Haut) et **contextualise** la compétence.  
- Exemple : **Analyser** l’impact d’outils numériques **en adoptant** une démarche de co-conception avec les pairs, dans des situations de co-enseignement.  
**Réponse : [à compléter]**

**Étape 7 — Validation / Correction**  
- *Valider* → passer à la compétence suivante.  
- *Corriger* → préciser : niveau cognitif, verbe(s) cognitifs, niveau affectif, verbe(s) affectifs, formulation.  
**Réponse : [à compléter]**

---

## ✅ Synthèse finale & validation

**Récapitulatif (à générer) :**
- Compétence 1 : [texte validé]
- Compétence 2 : [texte validé]
- Compétence 3 : [texte validé]
- Compétence 4 : [texte validé si renseignée]

**Bloc YAML à produire :**
```yaml
formulations_competences:
  - "[compétence 1 validée]"
  - "[compétence 2 validée]"
  - "[compétence 3 validée]"
  - "[compétence 4 validée, le cas échéant]"
