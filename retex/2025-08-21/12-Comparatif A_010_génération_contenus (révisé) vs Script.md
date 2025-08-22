# 📊 Analyse comparative — A_010_Contenus_Par_Section vs Script Python (contenus)

## 1. Points de conformité

- ✔️ Le script **intègre déjà** le squelette d’instructions `INSTRUCTION_ASSISTANT` tel que prévu dans A_010.  
- ✔️ Il charge bien les compétences depuis `etape_4_competences` (ordre validé).  
- ✔️ Il appelle les ressources RAG (`Tableau_Activites_Ressources.json`) comme spécifié.  
- ✔️ La structure du tableau Markdown + YAML de sortie est respectée (mêmes colonnes).  
- ✔️ Les sections fixes (S1, S6, S7, S8) sont bien prévues avec contenu pré-rempli.

---

## 2. Écarts et ajustements nécessaires

### a) **Priorités pédagogiques (ABC + CMO hybride)**
- **Markdown (A_010)** : insiste sur la priorisation hybride spécifique au scénario CMO :  
  1. Acquisition  
  2. Collaboration  
  3. Discussion  
  4. Pratique  
  (Production et Enquête uniquement en complément).  
- **Script** : reprend les priorités ABC générales, mais ne fait pas explicitement le lien avec le **scénario hybride CMO**.  
- **Correction** : adapter le bloc `## RÈGLES DE FILTRAGE` dans `prepare_contenus_prompt` pour mentionner explicitement **scénario CMO hybride** + ordonnancement strict.

---

### b) **Filtrage par type (lien avec le tableur R_03)**
- **Markdown** :  
  - Ressource principale **toujours** avec intention Acquisition.  
  - Doit provenir des entrées type `Ressource` ou `Ressource H5P` *(selon le tableur)*.  
  - Activité 1 doit être issue des lignes `Activité` ou `Activité H5P`.  
  - Activité 2 proposée **uniquement si compétence complexe** (pas seulement “intention complémentaire”).  
- **Script** :  
  - Mentionne bien Ressource / Activité, mais **n’associe pas explicitement** les types aux colonnes du tableur RAG.  
  - Activité 2 reste décrite comme “optionnelle” sans condition de complexité.  
- **Correction** :  
  - Ajouter des filtres explicites en fonction des colonnes `type` du RAG.  
  - Conditionner Activité 2 à la **complexité de la compétence** (ex. longueur de formulation, verbes de haut niveau Bloom, etc.).

---

### c) **Justification obligatoire**
- **Markdown** : demande une justification distincte **pour chaque choix** (ressource, activité 1, activité 2).  
- **Script** : demande une justification globale (colonne unique).  
- **Correction** :  
  - Séparer justification par item (ou enrichir la justification globale avec explication des 3 choix).  
  - Ajouter consigne dans le prompt : *« expliquer pourquoi cette ressource, pourquoi cette activité 1, pourquoi cette activité 2 »*.

---

### d) **Gestion des sections fixes**
- **Markdown** : précise **S8 = Sondage Magistère (Enquête)**, pas juste “Sondage”.  
- **Script** : génère S8 avec `Sondage`.  
- **Correction** : remplacer par `Sondage Magistère`.

---

### e) **Format de sortie**
- **Markdown** : impose chaînes vides `""` pour champs vides.  
- **Script** : déjà prévu (fonction `safe_get`), mais la conversion YAML peut encore retourner `null`.  
- **Correction** : ajouter un post-traitement garantissant que tous les `None` → `""` avant export.

---

## 3. Recommandations techniques

1. **Adapter la fonction `prepare_contenus_prompt`** :
   - Ajouter mention explicite du **scénario CMO hybride**.  
   - Mettre la hiérarchie des intentions pédagogiques dans l’ordre correct.  
   - Clarifier filtrage Ressource/Activité par type **lié au RAG**.  
   - Ajouter condition sur Activité 2 (compétence complexe).  
   - Ajouter justification détaillée par ressource/activité.

2. **Modifier la fonction `generate_mock_contenus`** (fallback) :  
   - Ressource par défaut → intention Acquisition.  
   - Activité 1 → en cohérence avec type de compétence.  
   - Activité 2 → générée seulement si compétence complexe.  
   - Corriger S8 → `Sondage Magistère`.

3. **Améliorer `parse_ai_contenus_response`** :  
   - Vérifier que `null` est converti en `""`.  
   - Normaliser les champs pour éviter variations (`justification_activite_s` vs autres variantes).

---

## 4. Conclusion

Le script de Guillaume est déjà bien aligné mais doit être **ajusté sur 5 points stratégiques** pour correspondre strictement au Markdown mis à jour :  
1. Préciser **priorités pédagogiques CMO hybride**.  
2. Filtrage explicite Ressource/Activité en lien avec le tableur.  
3. Activité 2 générée uniquement si compétence complexe.  
4. Justification obligatoire pour **chaque choix**.  
5. Correction du libellé **Sondage Magistère** et gestion stricte des `""`.

Avec ces ajustements, le script respectera parfaitement le dernier A_010 et produira des contenus cohérents, conformes et exploitables.

