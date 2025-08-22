# 📊 Comparatif — Script “Référentiels” (Guillaume) vs **A_009** mis à jour + Gabarit export v5

## 🎯 But
Aligner le **script de génération du référentiel** avec le **prompt A_009 (v2)** et le **gabarit tableur export v5** (3 onglets), afin d’obtenir des sorties strictement conformes (noms de champs, valeurs, structure YAML finale). Références : A_009 (v2) et gabarit export v5. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧾 Résumé exécutif (écarts majeurs)

- **Badge** : le script **ajoute/valorise “badge”** (oui/non). → **À supprimer** (le badge n’existe plus en v5). :contentReference[oaicite:2]{index=2}
- **Libellés de niveaux** : le script utilise **“Je maîtrise avec aisance”** ; le prompt v2 exige **“Je maîtrise”**. → **À corriger**. :contentReference[oaicite:3]{index=3}
- **Champs quanti/quali** : le script sort **`observable_qualitatif` / `observable_quantitatif`** ; le prompt v2 et le gabarit demandent **`indicateur_qualitatif` / `indicateur_quantitatif`**. → **À renommer**. :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
- **Valeurs quantitatives** : le script laisse libre (score/fréquence) ; le prompt v2 impose **textes fixes** “Au moins 25 % / 50 % / 75 % / 100 %”. → **À figer**. :contentReference[oaicite:6]{index=6}
- **CUA** : le script **insère des adaptations CUA** si besoins spécifiques ; le prompt v2 précise **“pas d’adaptations CUA par défaut”**. → **À désactiver par défaut** (n’activer que si l’utilisateur le demande). :contentReference[oaicite:7]{index=7}
- **Clé de rattachement** : le script sauvegarde par **`section_{n}`** sous `etape_5_referentiels` ; la sortie attendue (v5) est une **liste** `referentiels_par_section` avec **`competence_id` + `competence_formulation`** (et non l’index de section). → **À aligner sur la nouvelle structure**. :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

---

## 🗂️ Tableau comparatif détaillé

| Élément | Exigence A_009 / Gabarit v5 | Script actuel | Écart | Action requise |
|---|---|---|---|---|
| **Nombre de degrés** | 4 : 1–4 | 4 | — | — |
| **Libellés degrés** | `Je débute`, `Je progresse`, `Je suis autonome`, `Je maîtrise` | idem sauf dernier : **“Je maîtrise avec aisance”** | ⚠️ libellé | Remplacer par **“Je maîtrise”**. 【72】 |
| **Indicateur qualitatif** | Champ **`indicateur_qualitatif`** (texte lié à la compétence) | **`observable_qualitatif`** | ❌ nom de champ | Renommer en **`indicateur_qualitatif`**. 【72】【64】 |
| **Indicateur quantitatif** | **Textes fixes** : “Au moins 25 % / 50 % / 75 % / 100 %” | Valeurs libres “Score/Fréquence/Action” | ❌ contenu + nom de champ | Forcer **`indicateur_quantitatif`** avec **valeurs imposées**. 【72】 |
| **Badge** | **Supprimé** (non présent) | Géré (oui au degré 3, non sinon) | ❌ champ obsolète | **Retirer** le champ `badge`. 【72】 |
| **Structure finale** | Liste YAML `referentiels_par_section` avec `competence_id`, `competence_formulation`, `niveaux[degre,libelle,indicateur_*]` | JSON par section + sauvegarde `etape_5_referentiels.section_{n}` | ❌ structure et clés | Émettre une **liste** et **sauvegarder** sous `referentiels_par_section` (par **compétence**, pas par numéro de section). 【72】【64】 |
| **Alignement tableur v5** | Doit remplir **02_Référentiels** (blocs par compétence) | Champs ne correspondent pas 1:1 | ❌ mapping | Utiliser exactement les **en-têtes/clé** du gabarit v5. 【64】 |
| **CUA** | “Ne pas inclure par défaut” | Ajout auto si `besoins_specifiques` non vide | ⚠️ politique | **Désactiver** l’ajout auto ; exposer une **option explicite**. 【63】 |
| **Température** | N/A (mais stabilité souhaitée) | 0.7 | ⚠️ variabilité | Baisser à **0.2–0.3** pour cohérence. |
| **Validation** | Contraintes figées (libellés/ratios) | Aucune validation a posteriori | ❌ | Ajouter un **contrôleur** post‑génération (libellés exacts, valeurs quanti exactes, clés attendues). |

---

## ✅ Spécification cible — schéma de sortie attendu

> À respecter par `generate_referentiel_suggestions()` **et** par la sauvegarde.

```yaml
referentiels_par_section:
  - competence_id: C1
    competence_formulation: "…"
    niveaux:
      - degre: 1
        libelle: "Je débute"
        indicateur_qualitatif: "…"
        indicateur_quantitatif: "Au moins 25 %"
      - degre: 2
        libelle: "Je progresse"
        indicateur_qualitatif: "…"
        indicateur_quantitatif: "Au moins 50 %"
      - degre: 3
        libelle: "Je suis autonome"
        indicateur_qualitatif: "…"
        indicateur_quantitatif: "Au moins 75 %"
      - degre: 4
        libelle: "Je maîtrise"
        indicateur_qualitatif: "…"
        indicateur_quantitatif: "100 %"


