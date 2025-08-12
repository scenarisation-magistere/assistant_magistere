<!-- Instructions pour l'assistant -->

[INSTRUCTION_ASSISTANT] :
- Ce fichier **déclenche l’assistant de manière contrôlée** et **impose un passage strictement séquentiel** du macrodesign.
- Ne **résumez** ni **reformulez** aucun des fichiers suivants. L’assistant doit **présenter intégralement** chaque fichier dans l’ordre indiqué.
- **Afficher immédiatement** le contenu du fichier `A_000_Prompt_Assistant.md` sans commentaire ni transition.
- Après avoir présenté `A_000_Prompt_Assistant.md`, l’assistant doit procéder à l'étape suivante, **une par une**, dans l’ordre des fichiers listés :
  - **1️⃣ A_001A_Presentation_Macrodesign.md**
  - **2️⃣ A_001B_Public_Cible.md**
  - **3️⃣ A_001C_Contraintes_Formation.md**
  - **4️⃣ A_001D_Scenario_Hybridation.md**
  - **5️⃣ A_001E_Competences_Visees.md**
  - **6️⃣ A_001F_Organisation_Competences.md**
  - **7️⃣ A_001G_Referentiels_Par_Section.md**
  - **8️⃣ A_001H_Contenus_Par_Section.md**
  - **9️⃣ A_001I_Generation_Recap_Macrodesign.md**
  - **🔟 A_001I_Tableur_Modele_Macro_Export.xlsx**
- À chaque étape, l’assistant doit vérifier que l'étape précédente est validée avant de passer à la suivante.
- Utiliser le bloc `etat_progression` pour suivre l’avancement de chaque étape.  
  Le statut des étapes doit être marqué comme **"en attente"** jusqu'à leur validation, puis mis à jour lorsque l’étape est complétée.
- Le fichier **A_001I_Generation_Recap_Macrodesign.md** doit générer un bloc YAML complet qui sera **exporté et sauvegardé localement**.
- Le bloc YAML généré doit être utilisé pour l’export dans le fichier Excel **A_001I_Tableur_Modele_Macro_Export.xlsx**.

---

## ✅ Suivi de progression

```yaml
etat_progression:
  etape_001A: en attente
  etape_001B: en attente
  etape_001C: en attente
  etape_001D: en attente
  etape_001E: en attente
  etape_001F: en attente
  etape_001G: en attente
  etape_001H: en attente
  etape_001I: en attente
  tableur_export: en attente

---

## 📂 En fin de parcours

- Le bloc YAML généré doit être **exporté et sauvegardé localement**.
- Il peut être utilisé dans le fichier Excel `A_001I_Tableur_Modele_Macro_Export.xlsx` pour un export automatique des données.
- Ce fichier YAML permettra également d’enchaîner avec le microdesign (`A_002A_...`).

---

## 📌 Résumé

- Ce prompt **contient uniquement des instructions techniques destinées à l’assistant** pour gérer l’enchaînement des étapes du macrodesign.
- **Aucun contenu n'est destiné au formateur**, et les instructions sont données strictement pour l'assistant afin de garantir que le processus soit exécuté dans l'ordre.