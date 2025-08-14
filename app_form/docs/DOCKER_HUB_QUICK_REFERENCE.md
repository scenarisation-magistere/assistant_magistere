# Docker Hub Quick Reference - Assistant Magistère

## Configuration Rapide

### 1. Configuration Docker Hub
```bash
# Éditer le fichier .env
nano .env
```

Ajouter les variables Docker Hub :
```env
DOCKER_HUB_USERNAME=votre-username
DOCKER_HUB_REPOSITORY=assistant-magistere
DOCKER_HUB_TAG=latest
```

### 2. Connexion Docker Hub
```bash
docker login
# Entrez votre nom d'utilisateur et mot de passe Docker Hub
```

## Commandes Rapides

### Linux/macOS
```bash
# Build + Tag + Push en une commande
./deploy.sh release v1.0.0

# Ou avec version auto-générée
./deploy.sh release

# Commandes individuelles
./deploy.sh build
./deploy.sh tag v1.0.0
./deploy.sh push v1.0.0
```

### Windows PowerShell
```powershell
# Build + Tag + Push en une commande
.\deploy.ps1 release v1.0.0

# Ou avec version auto-générée
.\deploy.ps1 release

# Commandes individuelles
.\deploy.ps1 build
.\deploy.ps1 tag v1.0.0
.\deploy.ps1 push v1.0.0
```

## Gestion des Versions

### Tags Auto-générés
Le script génère automatiquement des tags basés sur :
- **Timestamp** : `YYYYMMDD_HHMMSS`
- **Git commit** : Hash court du dernier commit

Exemples :
- `v20241201_143022-a1b2c3d`
- `v20241201_143022-unknown` (si pas de git)

### Tags Manuels
Vous pouvez spécifier vos propres tags :
- `v1.0.0`
- `v1.2.3-beta`
- `release-candidate-1`

## Utilisation des Images

### Pull d'une Image
```bash
# Dernière version
docker pull votre-username/assistant-magistere:latest

# Version spécifique
docker pull votre-username/assistant-magistere:v1.0.0
```

### Utilisation avec Docker Compose
Modifier `docker-compose.yml` :
```yaml
services:
  assistant-magistere:
    image: votre-username/assistant-magistere:latest
    # ... autres configurations
```

## Workflow Typique

### 1. Développement Local
```bash
# Construire et tester localement
./deploy.sh build
./deploy.sh start
```

### 2. Release
```bash
# Release complète avec version
./deploy.sh release v1.0.0

# Ou release avec version auto-générée
./deploy.sh release
```

### 3. Déploiement Production
```bash
# Sur le serveur de production
docker pull votre-username/assistant-magistere:v1.0.0
docker-compose up -d
```

## Dépannage

### Erreurs Courantes

#### 1. "DOCKER_HUB_USERNAME non configuré"
```bash
# Vérifier la configuration
cat .env | grep DOCKER_HUB

# Ajouter la configuration manquante
echo "DOCKER_HUB_USERNAME=votre-username" >> .env
```

#### 2. "Vous n'êtes pas connecté à Docker Hub"
```bash
# Se connecter à Docker Hub
docker login
```

#### 3. "Repository not found"
- Vérifier que le repository existe sur Docker Hub
- Créer le repository si nécessaire via l'interface web

#### 4. "Permission denied"
- Vérifier les permissions sur le repository Docker Hub
- S'assurer que vous êtes le propriétaire ou collaborateur

### Commandes de Diagnostic
```bash
# Vérifier la configuration
cat .env

# Vérifier la connexion Docker Hub
docker info

# Lister les images locales
docker images | grep assistant-magistere

# Vérifier les tags
docker images votre-username/assistant-magistere
```

## Bonnes Pratiques

### 1. Versioning
- Utilisez le versioning sémantique : `v1.0.0`, `v1.1.0`, etc.
- Gardez toujours un tag `latest` à jour
- Utilisez des tags descriptifs pour les releases

### 2. Sécurité
- Ne jamais commiter le fichier `.env` avec les vraies clés
- Utiliser des tokens d'accès Docker Hub plutôt que le mot de passe
- Limiter les permissions sur les repositories

### 3. CI/CD
- Automatiser les releases avec GitHub Actions ou GitLab CI
- Tester les images avant de les pousser
- Utiliser des tags de staging pour les tests

### 4. Monitoring
- Surveiller l'espace disque utilisé par les images
- Nettoyer régulièrement les anciennes images
- Monitorer les pulls et l'utilisation des images

## Exemples Complets

### Workflow de Release
```bash
# 1. Développement
./deploy.sh build
./deploy.sh start
# ... tests ...

# 2. Tag et push
./deploy.sh tag v1.0.0
./deploy.sh push v1.0.0

# 3. Ou release complète
./deploy.sh release v1.0.0
```

### Déploiement Multi-environnement
```bash
# Développement
./deploy.sh release v1.0.0-dev

# Staging
./deploy.sh release v1.0.0-staging

# Production
./deploy.sh release v1.0.0
```

---

**Note** : Ce guide couvre les fonctionnalités de base. Pour des workflows avancés, consultez la documentation complète dans `DEPLOYMENT.md`.
