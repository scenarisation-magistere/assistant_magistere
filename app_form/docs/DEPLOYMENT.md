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
```

### 3. Rendre le script de déploiement exécutable
```bash
chmod +x deploy.sh
```

## Déploiement Rapide

### Option 1 : Script de déploiement (Recommandé)
```bash
# Construire et démarrer l'application
./deploy.sh build
./deploy.sh start

# Vérifier le statut
./deploy.sh status

# Voir les logs
./deploy.sh logs
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
```bash
./deploy.sh build      # Construire l'image
./deploy.sh start      # Démarrer l'application
./deploy.sh stop       # Arrêter l'application
./deploy.sh restart    # Redémarrer l'application
./deploy.sh logs       # Afficher les logs
./deploy.sh status     # Afficher le statut
./deploy.sh clean      # Nettoyer les conteneurs
./deploy.sh help       # Afficher l'aide
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