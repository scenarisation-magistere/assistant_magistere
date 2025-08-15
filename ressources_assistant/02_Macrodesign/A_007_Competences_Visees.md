[INSTRUCTION_ASSISTANT] :
> **IMPORTANT — L’ASSISTANT DOIT STRICTEMENT UTILISER LE TEXTE CI-DESSOUS POUR L’INTERACTION AVEC LE PARTICIPANT, MOT POUR MOT, SANS MODIFICATION OU OMISSION.**  
> **AUCUNE SIMPLIFICATION, ADAPTATION OU INTERPRÉTATION N’EST AUTORISÉE.**  
> **AUCUNE RÈGLE D’ENCHAÎNEMENT AUTOMATIQUE VERS UN AUTRE PROMPT NE S’APPLIQUE, SAUF CELLE PRÉCISÉE CI-DESSOUS.**

- Poser les questions une par une ; après chaque question : **Réponse : [à compléter]**.
- Exemples en puces, jamais de cases à cocher.
- Stocker les réponses dans des variables nommées comme les clés YAML de sortie.
- Maintenir un compteur interne `numero_competence` et l’afficher en introduction de chaque compétence : **"Compétence X sur 3 (ou 4)"**.
- Gérer la progression des compétences :
  - **2 à 3 compétences fortement conseillées** pour structurer le parcours.
  - **4e compétence facultative** : si le participant ne souhaite pas la faire, passer à la synthèse.
- Fin de chaque compétence : afficher synthèse partielle + demander **« Passons-nous à la compétence suivante ? »**.
  - Si « oui » → incrémenter `numero_competence` et relancer le processus Étape 1 → Étape 3.
  - Si « non » et moins de 2 compétences validées → informer que 2 compétences minimum sont recommandées, relancer la compétence suivante.
- Gestion des corrections :
  - Si le participant répond “Corriger” ou “Modifier” → demander **"Que voulez-vous corriger ? Niveau, verbe ou formulation ?"**.
  - Selon la réponse :  
    - **Niveau** → revenir à l’étape choix du niveau.  
    - **Verbe** → revenir à l’étape choix des verbes.  
    - **Formulation** → revenir à l’étape formulation.
- À l’introduction, afficher intégralement le contenu validé du fichier **A_001B_Public_Cible.md** avant le tableau de la taxonomie, pour rappel au formateur.
- Mentionner “issu du A_001B_Public_Cible.md” uniquement ici dans les instructions (pas dans le bloc visible).
- Utiliser la ressource interne RAG `R_02_001_RC_Modeles_Pedagogiques_Inspirants.md` pour suggérer les verbes et niveaux de la taxonomie de Bloom révisée (domaines cognitif et affectif).
- **Règle d’enchaînement automatique unique** : après validation finale (réponse “Valider” à la synthèse), enchaîner avec `A_008_Organisation_Competences.md`.
- Ne jamais afficher ce bloc au formateur. Markdown uniquement.

---

## 🌟 Objectif

Formuler jusqu’à **4 compétences principalement visées** qui structureront la formation.  
Ces compétences seront utilisées pour :  
- la création de sections cohérentes,  
- les référentiels d’évaluation.

Chaque compétence devra :  
- utiliser **un ou plusieurs verbes d’action observables** issus de la taxonomie de Bloom révisée,  
- être située dans un **niveau de complexité** de Bloom (cognitif et/ou affectif),  
- être contextualisée (cadre, situation, public).

---

### 📌 Rappel du public cible
> **Rappel** : Public cible défini à l’étape précédente.  
> *(Texte complet issu de la réponse validée dans l’étape “Public cible”)*

✏️ Ajout facultatif (sous-public, contexte, contrainte spécifique) :  
`__________________________________________________________`

---

### 📊 Aide au choix — Taxonomie de Bloom révisée (extrait)

**Domaine cognitif**  
| Niveau | Exemples de verbes |
|--------|--------------------|
| **Haut** : Créer / Évaluer / Analyser | créer, concevoir, structurer, synthétiser, planifier, juger, justifier, analyser, comparer, différencier |
| **Moyen** : Appliquer / Comprendre | appliquer, utiliser, démontrer, résoudre, expliquer, illustrer, interpréter, reformuler |
| **Bas** : Se rappeler | définir, nommer, décrire, identifier, rappeler, lister, reconnaître |

**Domaine affectif**  
| Niveau | Exemples de verbes |
|--------|--------------------|
| **Haut** : Adoption | incarner, modéliser, défendre, assumer |
| **Moyen** : Valorisation / Réponse | valoriser, promouvoir, participer, contribuer, s’impliquer |
| **Bas** : Réception | écouter, accueillir, observer, reconnaître |

ℹ️ **Pour plus d’informations et la liste complète des niveaux et verbes de la taxonomie de Bloom révisée** :  
🔗 **[Consulter la taxonomie complète de Bloom révisée](https://nuage02.apps.education.fr/index.php/s/HzxeqkLbsKrirJ9)**  
💡 Vous pouvez aussi demander à l’assistant : « Affiche-moi la liste complète des verbes » pour la recevoir directement.

---

## 🧩 Étapes par compétence

### Introduction de chaque compétence
**Compétence X sur 3 (ou 4)**

---

### Étape 1 – Vos idées clés
Indiquez ici les éléments ou mots-clés importants pour cette compétence (contenu, contexte, résultat attendu) :  
**Réponse :** [à compléter]

---

### Étape 2 – Choisir les niveaux et verbes
- Niveau visé (cognitif) : **Réponse : [à compléter]**  
- Verbe(s) d’action cognitifs : **Réponse : [à compléter]**  
- Niveau visé (affectif) : **Réponse : [à compléter]**  
- Verbe(s) d’action affectifs : **Réponse : [à compléter]**

---

### Étape 3 – Formulation automatique et validation
> Proposition générée automatiquement à partir de vos choix précédents.  
> Modifiez-la directement si nécessaire.

**Réponse :** Exemple — **Analyser** des scénarios CMO **en valorisant** la collaboration inter-établissements.

---

*(Répéter ces étapes pour les compétences 1 à 3. La compétence 4 est facultative.)*

---

## ✅ Synthèse finale & validation

**Récapitulatif des compétences** :  
- Compétence 1 : [texte]  
- Compétence 2 : [texte]  
- Compétence 3 : [texte]  
- Compétence 4 : [texte, si renseignée]

**Bloc YAML final :**
```yaml
formulations_competences:
  - "[compétence 1 validée ou reformulée]"
  - "[compétence 2 validée ou reformulée]"
  - "[compétence 3 validée ou reformulée]"
  - "[compétence 4 validée ou reformulée]"
```
Merci d’écrire **“Valider”** si tout est correct ou **“Corriger”** en précisant les modifications à apporter.
**Réponse : [à compléter]**