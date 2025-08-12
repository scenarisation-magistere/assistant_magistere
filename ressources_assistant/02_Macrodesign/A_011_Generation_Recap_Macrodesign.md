## 🎯 Objectif du prompt

Ce prompt permet de **générer une fiche complète de macrodesign pédagogique**, en synthétisant automatiquement :

- les données générales issues des prompts `001B` à `001D`,
- les compétences visées (`001E`) et leur organisation (`001F`),
- les référentiels d’autoévaluation par section (`001G`),
- les contenus pédagogiques détaillés pour chaque section (`001H`).

Il produit une fiche en **deux blocs YAML prêts à l’export**, selon le scénario hybride structuré de la **Communauté Magistère Occitanie (CMO)**.

---

## 🧾 Étapes du prompt

### 🔹 Étape 1 – Génération des deux blocs YAML

#### 📦 Bloc 1 – Généralités

```yaml
macrodesign_generalites:
  titre_formation: "[titre validé]"
  public_cible:
    type: "[enseignants / formateurs / autres]"
    profil: "[homogène / hétérogène]"
    niveau_expertise: "[débutant / intermédiaire / avancé]"
    besoins_specifiques:
      - "[besoin 1]"
      - "[besoin 2]"
  contraintes_formation:
    type_parcours: "[création / migration]"
    hybridation: "asynchrone (majeure) + synchrone (mineure)"
    temps_total: "moins de 3h"
    autonomie: "formation tutorée"
    animation: "[individuelle / coanimée]"
    calendrier: "[à préciser]"
    horaires: "[à préciser]"
    nombre_participants: "[valeur]"
  scenario_hybride:
    reference: "CMO"
    structure:
      - Accueil
      - Apprentissage 1
      - Apprentissage 2
      - Apprentissage 3
      - Apprentissage 4
      - Classe virtuelle
      - Forum général
      - Évaluation finale
  competences_visées:
    - "[formulation compétence 1]"
    - "[formulation compétence 2]"
    - "[formulation compétence 3]"
    - "[formulation compétence 4]"
  referentiels_autoévaluation:
    - section: 2
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
    - section: 3
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
    - section: 4
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"
    - section: 5
      competence: "[...]"
      badge: "Réussite si atteinte du degré 3"

contenus_par_section:
  - section: 1
    titre: "Bienvenue dans la formation"
    intentions: ["Acquisition"]
    ressource: "Page d’accueil"
    activite_1: null
    activite_2: null
    discussion: "Présentation du parcours, modalités, contacts"
    badge: null
    modalite: "Asynchrone"

  - section: 2
    titre: "[titre section 2]"
    intentions: ["Acquisition", "[intention secondaire 2]"]
    ressource: "[ressource section 2]"
    activite_1: "[activité 1 section 2]"
    activite_2: "[activité 2 section 2]"
    discussion: "[discussion section 2]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 3
    titre: "[titre section 3]"
    intentions: ["Acquisition", "[intention secondaire 3]"]
    ressource: "[ressource section 3]"
    activite_1: "[activité 1 section 3]"
    activite_2: "[activité 2 section 3]"
    discussion: "[discussion section 3]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 4
    titre: "[titre section 4]"
    intentions: ["Acquisition", "[intention secondaire 4]"]
    ressource: "[ressource section 4]"
    activite_1: "[activité 1 section 4]"
    activite_2: "[activité 2 section 4]"
    discussion: "[discussion section 4]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 5
    titre: "[titre section 5]"
    intentions: ["Acquisition", "[intention secondaire 5]"]
    ressource: "[ressource section 5]"
    activite_1: "[activité 1 section 5]"
    activite_2: "[activité 2 section 5]"
    discussion: "[discussion section 5]"
    badge: "Réussite si atteinte du degré 3"
    modalite: "Asynchrone"

  - section: 6
    titre: "Classe virtuelle – mise en pratique"
    intentions: ["Collaboration"]
    ressource: "Lien vers classe virtuelle (BBB)"
    activite_1: null
    activite_2: null
    discussion: null
    badge: null
    modalite: "Synchrone"

  - section: 7
    titre: "Forum général – échanges libres"
    intentions: ["Discussion", "Collaboration"]
    ressource: null
    activite_1: "Forum"
    activite_2: null
    discussion: "Fils issus des discussions des sections S2 à S5"
    badge: null
    modalite: "Asynchrone"

  - section: 8
    titre: "Évaluation finale et perspectives"
    intentions: ["Enquête"]
    ressource: "Sondage Magistère"
    activite_1: null
    activite_2: null
    discussion: "Questionnaire de satisfaction à 3 temporalités"
    badge: null
    modalite: "Asynchrone"
    
```

Souhaites-tu maintenant :
1. Que je te renvoie **tout le bloc YAML proprement formé** (début + fin correcte),
2. Que je te crée directement un fichier `.md` exportable ?

Dis-moi ce que tu préfères.


## 📝 Étape 3 – Validation du macrodesign

> ⚠️ Une fois que vous avez validé ce récapitulatif, **aucune modification ne sera possible**.

Merci de bien relire toutes les informations générées (bloc YAML ci-dessus) :  
– données générales,  
– compétences par section,  
– intentions pédagogiques,  
– ressources et activités.

> Si vous constatez une erreur importante, il est nécessaire de **recommencer l’ensemble du parcours depuis le début** (en relançant le prompt de macrodesign).  
> Il n’est **pas possible** de modifier ce bloc YAML partiellement ou de corriger une seule section.


## 💾 Important – Continuité macrodesign → microdesign

> 🧭 Le microdesign (construction détaillée des sections) s’appuiera **directement** sur ce fichier YAML.

### ❗ Ce qu’il faut retenir :

- **Une fois que vous avez commencé le macrodesign, vous devez aller jusqu’à cette validation complète.**
- Vous ne pouvez interrompre le travail **qu’une fois le fichier final exporté**.
- Ce fichier exporté sera **la seule base fiable** pour commencer ou reprendre le microdesign plus tard.

> ⚠️ Toute interruption avant l’export entraîne une **perte totale des données**.

## 📂 Reprendre plus tard : mode d’emploi

Si vous souhaitez faire une pause après cette étape :

1. **Exportez le fichier YAML** (voir ci-dessous).
2. **Sauvegardez-le localement** sur votre ordinateur ou dans votre espace de travail (Nuage, clé USB…).
3. Lors de la reprise, **copiez-collez ce fichier dans le prompt de microdesign (`002A_Presentation_Microdesign.md`)**.
4. L’assistant pourra alors poursuivre le travail à partir de vos choix validés.

---

## 📤 Étape 4 – Export

Quel(s) format(s) souhaitez-vous générer ?

- [ ] Fichier Markdown `.md`  
- [ ] Fichier CSV (tableur compatible Excel/LibreOffice)  
- [ ] Les deux formats

---

## 🆘 Besoin d’aide ? Une question ?

👉 Vous pouvez contacter l’équipe de formateurs de la **Communauté Magistère Occitanie** :  
🔗 [Consulter les contacts formateurs CMO (Nuage Éducation nationale)](https://nuage02.apps.education.fr/index.php/apps/files/files/171289979?dir=/Magist%C3%A8re/Ressources%20grain%20migration&openfile=true)

**Principaux contacts** :  
- **Laurent Castillo – DRANE Occitanie**  
  📧 laurent.castillo@ac-toulouse.fr – ☎️ 05 36 25 72 82  
- **Caroline Menanteau – DRANE Occitanie**  
  📧 caroline.menanteau@ac-toulouse.fr – ☎️ 05 36 25 87 60  
- **EAFC Toulouse – Ingénierie Magistère**  
  📧 eafc-inge10@ac-toulouse.fr – ☎️ 05 36 25 70 24



