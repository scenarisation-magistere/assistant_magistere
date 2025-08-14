# 🎓 Prompt 002A – Microdesign d’une section (gabarit CMO)

## 🧠 Objectif du prompt  
Ce prompt se déclenche après la validation du macrodesign. Il permet de construire le **microdesign section par section**, en assurant un **alignement pédagogique rigoureux** entre :  
- les **compétences visées**,  
- les **ressources et activités proposées**,  
- et les **niveaux d’exigence définis dans les référentiels d’autoévaluation**.

## 🟢 Introduction

> ✅ Vous avez finalisé les grandes étapes du **macrodesign** de votre formation,  
> et un **export structuré de ce macrodesign** a été généré.

> 🧠 Dans le macrodesign, les **activités et les ressources** ont été définies **de manière globale**.  
> Le **microdesign** consiste à aller **plus finement dans la réalisation concrète** des différents éléments qui composent les sections :  
> – **formuler le titre précis** et la **présentation de la section**,  
> – définir les **ressources et les activités** associées,  
> – **paramétrer les ressources et les activités**, y compris leurs **critères d’achèvement**,  
> – **calibrer les durées**,  
> – **écrire les consignes**,  
> – **proposer des contenus adaptés**,  
> – **respecter le design de conception** et les principes d’**accessibilité**.

> 🧱 L’assistant vous proposera un accompagnement pas à pas pour chaque section à concevoir.  
> Vous serez guidé dans les choix, la formulation, et la structuration des éléments attendus.

---

## 💾 Important – Injection du macrodesign validé

Pour garantir la cohérence et la continuité entre macrodesign et microdesign, merci de **copier-coller ci-dessous le contenu complet du fichier Markdown exporté de votre macrodesign validé** (bloc YAML inclu).  

Ce fichier contient toutes les données nécessaires : compétences, intentions pédagogiques, ressources, activités, référentiels.  
Sans cette étape, le microdesign ne pourra pas s’appuyer sur les choix précédemment validés.

---

## 👣 Étapes à venir : concevoir chaque section pas à pas

> 🧭 Vous allez maintenant être **guidé section par section** dans la construction de votre microdesign.
>
> ⚠️ **Attention** : les sections d’apprentissage (2 à 5) nécessitent une **implication plus importante**.  
> Elles mobilisent des choix pédagogiques précis et demandent plus de temps de conception.
>
> ✅ Vous pouvez avancer à votre rythme, valider une section à la fois, et exporter chaque étape si besoin.

## 📊 Ordre des prompts pour guider par section

| Prompt                       | Couvre la section…                      | Charge cognitive estimée | Intentions pédagogiques (ABCLD)                                                                                    |
| ---------------------------- | --------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `002B_S1_Accueil.md`         | Section 1 – Accueil                     | Faible                   | Extraite de `contenus_par_section[section=1].intentions` : généralement `["Acquisition"]`                          |
| `002B_S2_Competence1.md`     | Section 2 – 1ʳᵉ section d’apprentissage | Importante               | Extraite de `contenus_par_section[section=2].intentions` : typiquement `["Acquisition", "Intention secondaire 2"]` |
| `002B_S3_Competence2.md`     | Section 3 – 2ᵉ section d’apprentissage  | Importante               | Extraite de `contenus_par_section[section=3].intentions` : typiquement `["Acquisition", "Intention secondaire 3"]` |
| `002B_S4_Competence3.md`     | Section 4 – 3ᵉ section d’apprentissage  | Importante               | Extraite de `contenus_par_section[section=4].intentions` : typiquement `["Acquisition", "Intention secondaire 4"]` |
| `002B_S5_Competence4.md`     | Section 5 – 4ᵉ section d’apprentissage  | Importante               | Extraite de `contenus_par_section[section=5].intentions` : typiquement `["Acquisition", "Intention secondaire 5"]` |
| `002B_S6_ClasseVirtuelle.md` | Section 6 – Classe virtuelle            | Faible                   | Fixe : `["Collaboration"]`                                                                                         |
| `002B_S7_Forum_General.md`   | Section 7 – Forum général               | Faible                   | Fixe : `["Collaboration"]`                                                                                         |
| `002B_S8_Evaluation.md`      | Section 8 – Évaluation finale           | Faible                   | Fixe : `["Enquête"]`                                                                                               |


🔁 Ce tableau constitue une référence de base. Il peut être adapté en fonction des choix faits lors de la scénarisation fine de chaque section.

## 📝 Note importante – Design et accessibilité

Pour faciliter une conception pédagogique efficace et inclusive, les **sections d’apprentissage (S2 à S5)** intègrent systématiquement un **encart rappelant les principes du design pédagogique (Mayer)** et les **exigences en matière d’accessibilité (CUA – RGAA)**.  
Ces rappels ont pour but d’accompagner progressivement les formateurs dans l’appropriation de ces dimensions essentielles.  
**Ils ne sont pas répétés dans les autres sections** (accueil, forum, classe virtuelle, évaluation finale), mais **restent à prendre en compte tout au long du parcours**.

## 📚 Ressources pour nourrir le microdesign

Vous pouvez vous appuyer sur les ressources suivantes pour concevoir les éléments de chaque section :

- 🧠 **Modèles pédagogiques & design**  
  `070_02_Mayer_Theorie_Multimedia_12_principes.md`  
  `070_04_UX_UI_Apprentissage.md`

- 🔐 **Accessibilité et RGPD**  
  `050_01_RGAA_Web_Mobile_2023.md`  
  `050_07_RGPD_Texte_CNIL.md`  
  `050_08_Mini_Guide_RGPD_Magister.md`  
  `050_13_fiche_Regles_Adaptation_Documents_Accessibles.md`

- 🧰 **Activités et tutoriels**  
  `030_Tableau_87_Activites_Moodle_ABC_liens_actifs.xlsx`  

- 📽️ **Exemples de capsules**  
  `061_Capsules_Magister_Occitanie.md`

microdesign_section_1:
  titre: "Accueil"
  objectifs: "Connaître le déroulé de la formation"
  duree: "3 minutes"
  modalite: "asynchrone"
  public_cible: "Formateurs 2nd degré"
  presentation: "Bienvenue dans ce parcours conçu pour vous accompagner pas à pas dans la scénarisation pédagogique. Vous y découvrirez les compétences visées, la structure du parcours, sa durée et ses modalités. Cette première étape vous permet de vous repérer et de vous engager."
  ressource_principale: null
  activite_1: null
  activite_2: null
  discussion: "Qu’attendez-vous de ce parcours ?"
  consigne: "Lire la présentation et se repérer dans le parcours"
  intention_ABC: ["Acquisition"]
  type_evaluation: "Aucune"
  role_formateur: "Mise en confiance"
  ergonomie: "Lisibilité directe sans action nécessaire"
  accessibilite: "Adapter les formats (textes lisibles, contrastes, navigation claire)"
  tutorat: "Aucun"
  parametres: "Aucun critère d’achèvement requis"
