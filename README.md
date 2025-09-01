### Assistant Magistère – Application Flask

Application pour assister la conception de parcours de formation (public cible, contraintes, scénario CMO, compétences) avec intégrations IA.

### Fonctionnalités clés
- Public cible, contraintes, scénario CMO et compétences avec suggestions IA
- Export YAML dans `app_form/output/` et logs dans `app_form/logs/`
- Utilisation d'OpenAI (configurable), mode fallback possible
- Exécution locale ou via Docker

### Structure du dépôt
- `app_form/` – Application Flask (code, templates, Docker)
- `excel_to_json.py` – Script conversion Excel → JSON
- `ressources_*` – Ressources pédagogiques/RAG
- `LICENCE.md` – Licence

### Prérequis
- Python 3.11+
- (Optionnel) Docker et Docker Compose
- Clé API OpenAI pour les fonctionnalités IA

### Installation (locale)
1) Aller dans l’app Flask
```bash
cd app_form
```
2) Créer et activer un environnement virtuel (Windows PowerShell)
```bash
py -m venv .venv
./.venv/Scripts/Activate.ps1
```
3) Installer les dépendances
```bash
pip install -r requirements.txt
```

### Configuration
1) Copier le template d’environnement et renseigner votre clé
```bash
copy env_template.txt .env
# Ouvrez .env et renseignez : OPENAI_API_KEY=VOTRE_CLE
```
2) Variables utiles (avec valeurs par défaut si non définies)
- `OPENAI_API_KEY` (requis pour l’IA)
- `OPENAI_MODEL` (par défaut: gpt-4o-mini)
- `OPENAI_MAX_TOKENS` (par défaut: 1000)
- `OPENAI_TEMPERATURE` (par défaut: 0.7)

### Lancer l’application (locale)
```bash
cd app_form
python app.py
# Ouvrir http://localhost:5000
```

### Exécution avec Docker
Depuis `app_form/`:
```bash
# 1) Docker Compose
docker-compose up -d --build

# 2) ou build/run manuels
docker build -t assistant-magistere .
docker run -d --name assistant-magistere -p 5000:5000 \
  -e OPENAI_API_KEY=VOTRE_CLE assistant-magistere
```
Application disponible sur http://localhost:5000.

### Tests (optionnel)
Des tests sont présents dans `app_form/tests/`. Si `pytest` est installé:
```bash
pip install pytest
cd app_form
pytest -q
```

### Outil Excel → JSON
Le script racine `excel_to_json.py` convertit un fichier Excel en JSON.
```bash
python excel_to_json.py
# Par défaut, lit le fichier d’exemple et écrit output.json
```
Utilisation programmatique:
```python
from excel_to_json import excel_to_json
excel_to_json("mon_fichier.xlsx", "sortie.json")
```

### Déploiement
- Fichiers utiles dans `app_form/` : `Dockerfile`, `docker-compose.yml`, `deploy.sh`, `deploy.ps1`, `docker-compose.prod.yml`, `nginx.conf`
- Voir aussi `app_form/docs/` pour des guides détaillés (Docker, cloud, etc.)

### Licence
Voir `LICENCE.md`.


