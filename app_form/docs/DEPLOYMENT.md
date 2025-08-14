# Guide de Déploiement - Assistant Magistère

## Vue d'ensemble

Ce guide vous accompagne dans le déploiement de l'Assistant Magistère avec Docker. L'application est containerisée et prête pour la production.

## Prérequis

### 1. Docker et Docker Compose
- **Docker** : Version 20.10 ou supérieure
- **Docker Compose** : Version 2.0 ou supérieure

### 2. Clé API OpenAI
- Une clé API OpenAI valide
- Accès aux modèles GPT-4o-mini ou supérieurs

## Installation et Configuration

### 1. Cloner le projet
```bash
git clone <repository-url>
cd assistant_magistere/app_form
```

### 2. Configurer les variables d'environnement
```bash
# Copier le template
cp env_template.txt .env

# Éditer le fichier .env
nano .env
```

**Contenu du fichier .env :**
```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional: Model configuration
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7

# Docker Hub Configuration (pour le déploiement)
DOCKER_HUB_USERNAME=your-docker-hub-username
DOCKER_HUB_REPOSITORY=assistant-magistere
DOCKER_HUB_TAG=latest
```

### 3. Rendre le script de déploiement exécutable
```bash
chmod +x deploy.sh
```

## Déploiement Rapide

### Option 1 : Script de déploiement (Recommandé)

#### Linux/macOS
```bash
# Construire et démarrer l'application
./deploy.sh build
./deploy.sh start

# Vérifier le statut
./deploy.sh status

# Voir les logs
./deploy.sh logs
```

#### Windows PowerShell
```powershell
# Construire et démarrer l'application
.\deploy.ps1 build
.\deploy.ps1 start

# Vérifier le statut
.\deploy.ps1 status

# Voir les logs
.\deploy.ps1 logs
```

### Option 2 : Docker Compose manuel
```bash
# Construire l'image
docker-compose build

# Démarrer l'application
docker-compose up -d

# Vérifier le statut
docker-compose ps
```

## Commandes de Gestion

### Script de déploiement

#### Linux/macOS (deploy.sh)
```bash
./deploy.sh build      # Construire l'image
./deploy.sh start      # Démarrer l'application
./deploy.sh stop       # Arrêter l'application
./deploy.sh restart    # Redémarrer l'application
./deploy.sh logs       # Afficher les logs
./deploy.sh status     # Afficher le statut
./deploy.sh clean      # Nettoyer les conteneurs
./deploy.sh tag        # Tagger l'image pour Docker Hub
./deploy.sh push       # Pousser l'image vers Docker Hub
./deploy.sh release    # Build + Tag + Push (release complète)
./deploy.sh help       # Afficher l'aide
```

#### Windows PowerShell (deploy.ps1)
```powershell
.\deploy.ps1 build      # Construire l'image
.\deploy.ps1 start      # Démarrer l'application
.\deploy.ps1 stop       # Arrêter l'application
.\deploy.ps1 restart    # Redémarrer l'application
.\deploy.ps1 logs       # Afficher les logs
.\deploy.ps1 status     # Afficher le statut
.\deploy.ps1 clean      # Nettoyer les conteneurs
.\deploy.ps1 tag        # Tagger l'image pour Docker Hub
.\deploy.ps1 push       # Pousser l'image vers Docker Hub
.\deploy.ps1 release    # Build + Tag + Push (release complète)
.\deploy.ps1 help       # Afficher l'aide
```

### Docker Compose
```bash
# Gestion de base
docker-compose up -d           # Démarrer en arrière-plan
docker-compose down            # Arrêter
docker-compose restart         # Redémarrer
docker-compose logs -f         # Logs en temps réel

# Maintenance
docker-compose build --no-cache # Reconstruire l'image
docker-compose pull            # Mettre à jour les images
docker system prune            # Nettoyer Docker
```

## Déploiement Docker Hub

### Configuration Docker Hub

1. **Créer un compte Docker Hub** (si pas déjà fait)
   - Allez sur [hub.docker.com](https://hub.docker.com)
   - Créez un compte et notez votre nom d'utilisateur

2. **Configurer les variables Docker Hub**
   ```bash
   # Éditer le fichier .env
   nano .env
   ```
   
   Ajoutez vos informations Docker Hub :
   ```env
   DOCKER_HUB_USERNAME=votre-username
   DOCKER_HUB_REPOSITORY=assistant-magistere
   DOCKER_HUB_TAG=latest
   ```

3. **Se connecter à Docker Hub**
   ```bash
   docker login
   # Entrez votre nom d'utilisateur et mot de passe Docker Hub
   ```

### Commandes de déploiement Docker Hub

#### Tagging d'images

**Linux/macOS :**
```bash
# Tagger avec version auto-générée
./deploy.sh tag

# Tagger avec version spécifique
./deploy.sh tag v1.0.0
./deploy.sh tag v1.2.3-beta
```

**Windows PowerShell :**
```powershell
# Tagger avec version auto-générée
.\deploy.ps1 tag

# Tagger avec version spécifique
.\deploy.ps1 tag v1.0.0
.\deploy.ps1 tag v1.2.3-beta
```

#### Push vers Docker Hub

**Linux/macOS :**
```bash
# Pousser la dernière version taggée
./deploy.sh push

# Pousser une version spécifique
./deploy.sh push v1.0.0
```

**Windows PowerShell :**
```powershell
# Pousser la dernière version taggée
.\deploy.ps1 push

# Pousser une version spécifique
.\deploy.ps1 push v1.0.0
```

#### Release complète (Build + Tag + Push)

**Linux/macOS :**
```bash
# Release avec version auto-générée
./deploy.sh release

# Release avec version spécifique
./deploy.sh release v1.0.0
```

**Windows PowerShell :**
```powershell
# Release avec version auto-générée
.\deploy.ps1 release

# Release avec version spécifique
.\deploy.ps1 release v1.0.0
```

### Gestion des versions

Le script génère automatiquement des tags de version basés sur :
- **Timestamp** : Date et heure de build (YYYYMMDD_HHMMSS)
- **Git commit** : Hash court du dernier commit (si disponible)

Exemple de tags générés :
- `v20241201_143022-a1b2c3d` (timestamp + commit)
- `v20241201_143022-unknown` (si pas de git)

### Utilisation des images Docker Hub

Une fois poussées, les images peuvent être utilisées sur d'autres serveurs :

```bash
# Pull de l'image
docker pull votre-username/assistant-magistere:latest
docker pull votre-username/assistant-magistere:v1.0.0

# Utilisation avec docker-compose
# Modifier docker-compose.yml :
services:
  assistant-magistere:
    image: votre-username/assistant-magistere:latest
    # ... autres configurations
```

## Accès à l'Application

### URL d'accès
- **Local** : http://localhost:5000
- **Réseau** : http://[IP-SERVEUR]:5000

### Vérification de santé
```bash
# Vérifier que l'application répond
curl http://localhost:5000/

# Vérifier les logs
docker-compose logs assistant-magistere
```

## Structure des Volumes

### Volumes montés
- `./output:/app/output` - Fichiers YAML générés
- `./logs:/app/logs` - Logs de l'application

### Données persistantes
Les données suivantes sont sauvegardées :
- Formations YAML dans `./output/`
- Logs d'application dans `./logs/`
- Sessions utilisateur

## Configuration Avancée

### Variables d'environnement
```env
# Configuration Flask
FLASK_APP=app.py
FLASK_ENV=production

# Configuration OpenAI
OPENAI_API_KEY=sk-your-key
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7
```

### Ports personnalisés
Modifier `docker-compose.yml` :
```yaml
ports:
  - "8080:5000"  # Port externe:interne
```

### Ressources système
```yaml
services:
  assistant-magistere:
    # ... autres configurations
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: '0.5'
        reservations:
          memory: 512M
          cpus: '0.25'
```

## Monitoring et Logs

### Logs en temps réel
```bash
# Tous les services
docker-compose logs -f

# Service spécifique
docker-compose logs -f assistant-magistere
```

### Monitoring de santé
```bash
# Vérifier le statut
docker-compose ps

# Vérifier les ressources
docker stats assistant-magistere
```

### Logs d'application
```bash
# Accéder aux logs
tail -f logs/app.log

# Logs Docker
docker logs assistant-magistere
```

## Sécurité

### Bonnes pratiques
- ✅ Utilisation d'un utilisateur non-root dans le conteneur
- ✅ Variables d'environnement pour les secrets
- ✅ Health checks configurés
- ✅ Volumes montés en lecture seule quand possible

### Recommandations
- Utiliser un reverse proxy (nginx) en production
- Configurer HTTPS avec Let's Encrypt
- Mettre en place un firewall
- Surveiller les logs d'accès

## Dépannage

### Problèmes courants

#### 1. Port déjà utilisé
```bash
# Vérifier les ports utilisés
netstat -tulpn | grep :5000

# Changer le port dans docker-compose.yml
ports:
  - "8080:5000"
```

#### 2. Erreur de clé API
```bash
# Vérifier la configuration
cat .env

# Tester la clé
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
     https://api.openai.com/v1/models
```

#### 3. Problème de permissions
```bash
# Corriger les permissions
sudo chown -R $USER:$USER output/ logs/

# Redémarrer le conteneur
docker-compose restart
```

#### 4. Conteneur ne démarre pas
```bash
# Vérifier les logs
docker-compose logs assistant-magistere

# Reconstruire l'image
docker-compose build --no-cache
docker-compose up -d
```

#### 5. Erreur Docker Hub
```bash
# Vérifier la connexion Docker Hub
docker login

# Vérifier la configuration
cat .env | grep DOCKER_HUB

# Tester le push manuel
docker push votre-username/assistant-magistere:latest
```

#### 6. Erreur de permissions Docker Hub
```bash
# Vérifier les permissions du repository
# Assurez-vous que le repository existe sur Docker Hub

# Créer le repository si nécessaire
# Via l'interface web Docker Hub ou API
```

### Commandes de diagnostic
```bash
# Informations système
docker system df
docker system info

# Espace disque
df -h

# Mémoire
free -h

# Processus
docker-compose ps
```

## Production

### Recommandations pour la production
1. **Reverse Proxy** : Utiliser nginx ou traefik
2. **SSL/TLS** : Configurer HTTPS
3. **Monitoring** : Prometheus + Grafana
4. **Backup** : Sauvegarder les volumes
5. **Logs** : Centraliser les logs (ELK stack)
6. **Sécurité** : Scanner de vulnérabilités

### Exemple avec nginx
```nginx
server {
    listen 80;
    server_name votre-domaine.com;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Support

### Ressources utiles
- [Documentation Docker](https://docs.docker.com/)
- [Documentation Docker Compose](https://docs.docker.com/compose/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

### Logs et diagnostics
En cas de problème, fournir :
- Sortie de `docker-compose logs`
- Contenu du fichier `.env` (sans la clé API)
- Version de Docker et Docker Compose
- Système d'exploitation

---

**Note** : Ce guide couvre le déploiement de base. Pour un environnement de production, consultez les recommandations de sécurité et de performance. 