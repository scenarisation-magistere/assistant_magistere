# 🐳 Déploiement Docker - Assistant Magistère

## Vue d'ensemble

Ce guide vous accompagne dans le déploiement de l'Assistant Magistère avec Docker. L'application est entièrement containerisée et prête pour la production.

## 📁 Structure des fichiers Docker

```
app_form/
├── Dockerfile                 # Image de l'application
├── .dockerignore             # Fichiers exclus du build
├── docker-compose.yml        # Déploiement développement
├── docker-compose.prod.yml   # Déploiement production
├── nginx.conf               # Configuration nginx
├── deploy.sh                # Script de déploiement (Linux/Mac)
├── deploy.ps1               # Script de déploiement (Windows)
├── deploy-prod.sh           # Script de déploiement production
├── env.example              # Template des variables d'environnement
└── DEPLOYMENT.md            # Guide détaillé de déploiement
```

## 🚀 Déploiement Rapide

### Prérequis
- Docker Desktop (Windows/Mac) ou Docker Engine (Linux)
- Docker Compose
- Clé API OpenAI

### 1. Configuration initiale

```bash
# Cloner le projet
git clone <repository-url>
cd assistant_magistere/app_form

# Configurer les variables d'environnement
cp env.example .env
# Éditer .env avec votre clé API OpenAI
```

### 2. Déploiement développement

```bash
# Linux/Mac
chmod +x deploy.sh
./deploy.sh build
./deploy.sh start

# Windows
.\deploy.ps1 build
.\deploy.ps1 start
```

### 3. Déploiement production

```bash
# Configuration initiale
chmod +x deploy-prod.sh
# Modifier DOMAIN et EMAIL dans deploy-prod.sh
./deploy-prod.sh setup

# Démarrage
./deploy-prod.sh start
```

## 🛠️ Commandes de gestion

### Développement
```bash
./deploy.sh build      # Construire l'image
./deploy.sh start      # Démarrer l'application
./deploy.sh stop       # Arrêter l'application
./deploy.sh restart    # Redémarrer l'application
./deploy.sh logs       # Afficher les logs
./deploy.sh status     # Afficher le statut
./deploy.sh clean      # Nettoyer les conteneurs
```

### Production
```bash
./deploy-prod.sh setup     # Configuration initiale
./deploy-prod.sh start     # Démarrer en production
./deploy-prod.sh stop      # Arrêter la production
./deploy-prod.sh restart   # Redémarrer la production
./deploy-prod.sh logs      # Afficher les logs
./deploy-prod.sh status    # Afficher le statut
./deploy-prod.sh ssl-renew # Renouveler SSL
./deploy-prod.sh backup    # Sauvegarder les données
```

## 🔧 Configuration

### Variables d'environnement (.env)
```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7

# Configuration Flask
FLASK_ENV=production
FLASK_DEBUG=False
```

### Configuration production
Modifiez dans `deploy-prod.sh` :
```bash
DOMAIN="your-domain.com"
EMAIL="your-email@domain.com"
```

## 📊 Monitoring et logs

### Logs en temps réel
```bash
# Développement
./deploy.sh logs

# Production
./deploy-prod.sh logs
```

### Statut des services
```bash
# Développement
./deploy.sh status

# Production
./deploy-prod.sh status
```

### Health checks
```bash
# Vérifier l'application
curl http://localhost:5000/

# Vérifier nginx (production)
curl http://localhost/health
```

## 🔒 Sécurité

### Bonnes pratiques implémentées
- ✅ Utilisateur non-root dans les conteneurs
- ✅ Variables d'environnement pour les secrets
- ✅ Health checks configurés
- ✅ Rate limiting avec nginx
- ✅ Headers de sécurité
- ✅ SSL/TLS en production

### Recommandations supplémentaires
- Utiliser un firewall
- Surveiller les logs d'accès
- Mettre en place des sauvegardes automatiques
- Scanner régulièrement les vulnérabilités

## 📦 Sauvegarde et restauration

### Sauvegarde automatique
```bash
./deploy-prod.sh backup
```

### Sauvegarde manuelle
```bash
# Sauvegarder les données
tar -czf backup_$(date +%Y%m%d_%H%M%S).tar.gz output/ logs/ .env

# Restaurer les données
tar -xzf backup_YYYYMMDD_HHMMSS.tar.gz
```

## 🔄 Mise à jour

### Mise à jour de l'application
```bash
# Arrêter l'application
./deploy.sh stop

# Récupérer les dernières modifications
git pull

# Reconstruire et redémarrer
./deploy.sh build
./deploy.sh start
```

### Mise à jour en production
```bash
./deploy-prod.sh stop
git pull
./deploy-prod.sh start
```

## 🐛 Dépannage

### Problèmes courants

#### 1. Port déjà utilisé
```bash
# Vérifier les ports
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
./deploy.sh restart
```

#### 4. Conteneur ne démarre pas
```bash
# Vérifier les logs
./deploy.sh logs

# Reconstruire l'image
./deploy.sh clean
./deploy.sh build
./deploy.sh start
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

## 🌐 Accès à l'application

### Développement
- **URL** : http://localhost:5000
- **Logs** : `./deploy.sh logs`
- **Statut** : `./deploy.sh status`

### Production
- **URL** : https://your-domain.com
- **Logs** : `./deploy-prod.sh logs`
- **Statut** : `./deploy-prod.sh status`

## 📈 Performance

### Optimisations Docker
- Image Python slim pour réduire la taille
- Multi-stage build pour optimiser les couches
- Cache des dépendances Python
- Compression gzip avec nginx

### Monitoring des ressources
```bash
# Utilisation des ressources
docker stats

# Logs de performance
docker-compose logs assistant-magistere | grep -i performance
```

## 🔧 Configuration avancée

### Personnalisation des ports
```yaml
# docker-compose.yml
ports:
  - "8080:5000"  # Port externe:interne
```

### Limitation des ressources
```yaml
# docker-compose.yml
deploy:
  resources:
    limits:
      memory: 1G
      cpus: '0.5'
    reservations:
      memory: 512M
      cpus: '0.25'
```

### Variables d'environnement supplémentaires
```env
# Configuration avancée
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
PYTHONPATH=/app
```

## 📚 Ressources utiles

- [Documentation Docker](https://docs.docker.com/)
- [Documentation Docker Compose](https://docs.docker.com/compose/)
- [Guide de déploiement complet](DEPLOYMENT.md)
- [Configuration nginx](nginx.conf)

## 🆘 Support

En cas de problème :
1. Vérifiez les logs : `./deploy.sh logs`
2. Consultez le statut : `./deploy.sh status`
3. Vérifiez la configuration : `cat .env`
4. Consultez ce guide et `DEPLOYMENT.md`

---

**Note** : Ce guide couvre le déploiement de base. Pour un environnement de production critique, consultez les recommandations de sécurité et de performance dans `DEPLOYMENT.md`. 