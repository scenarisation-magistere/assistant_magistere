#!/bin/bash

# Script de déploiement production pour Assistant Magistère
# Usage: ./deploy-prod.sh [setup|start|stop|restart|logs|ssl-renew|backup]

set -e

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DOMAIN="your-domain.com"
EMAIL="your-email@domain.com"
BACKUP_DIR="./backups"

# Fonction pour afficher les messages
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  Assistant Magistère - Prod${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Vérifier si Docker est installé
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker n'est pas installé."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose n'est pas installé."
        exit 1
    fi
}

# Vérifier les variables d'environnement
check_env() {
    if [ ! -f .env ]; then
        print_error "Fichier .env non trouvé. Créez-le d'abord."
        exit 1
    fi
    
    if ! grep -q "OPENAI_API_KEY=sk-" .env; then
        print_error "Clé API OpenAI non configurée dans .env"
        exit 1
    fi
}

# Configuration initiale
setup_production() {
    print_message "Configuration de la production..."
    
    # Créer les répertoires nécessaires
    mkdir -p logs/nginx logs/certbot ssl backups
    
    # Configurer nginx pour le domaine
    sed -i "s/your-domain.com/$DOMAIN/g" nginx.conf
    sed -i "s/your-email@domain.com/$EMAIL/g" docker-compose.prod.yml
    
    # Configurer les permissions
    chmod 755 logs ssl backups
    chmod 644 nginx.conf
    
    print_message "Configuration terminée!"
}

# Démarrer la production
start_production() {
    print_message "Démarrage de l'application en production..."
    
    # Construire les images
    docker-compose -f docker-compose.prod.yml build
    
    # Démarrer les services
    docker-compose -f docker-compose.prod.yml up -d
    
    print_message "Application démarrée en production!"
    print_message "Accédez à l'application: https://$DOMAIN"
}

# Arrêter la production
stop_production() {
    print_message "Arrêt de l'application en production..."
    docker-compose -f docker-compose.prod.yml down
    print_message "Application arrêtée!"
}

# Redémarrer la production
restart_production() {
    print_message "Redémarrage de l'application en production..."
    docker-compose -f docker-compose.prod.yml down
    docker-compose -f docker-compose.prod.yml up -d
    print_message "Application redémarrée!"
    print_message "Accédez à l'application: https://$DOMAIN"
}

# Afficher les logs
show_logs() {
    print_message "Affichage des logs de production..."
    docker-compose -f docker-compose.prod.yml logs -f
}

# Renouveler SSL
renew_ssl() {
    print_message "Renouvellement du certificat SSL..."
    
    # Arrêter nginx temporairement
    docker-compose -f docker-compose.prod.yml stop nginx
    
    # Renouveler le certificat
    docker-compose -f docker-compose.prod.yml run --rm certbot renew
    
    # Redémarrer nginx
    docker-compose -f docker-compose.prod.yml start nginx
    
    print_message "Certificat SSL renouvelé!"
}

# Sauvegarde
backup_data() {
    print_message "Sauvegarde des données..."
    
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"
    
    # Créer la sauvegarde
    tar -czf "$BACKUP_FILE" output/ logs/ .env
    
    print_message "Sauvegarde créée: $BACKUP_FILE"
    
    # Nettoyer les anciennes sauvegardes (garder les 7 derniers jours)
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete
}

# Monitoring
show_status() {
    print_message "Statut de l'application en production..."
    docker-compose -f docker-compose.prod.yml ps
    
    echo ""
    print_message "Utilisation des ressources:"
    docker stats --no-stream
}

# Nettoyage
clean_production() {
    print_warning "Nettoyage de la production..."
    docker-compose -f docker-compose.prod.yml down --rmi all --volumes --remove-orphans
    docker system prune -f
    print_message "Nettoyage terminé!"
}

# Afficher l'aide
show_help() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commandes disponibles:"
    echo "  setup      - Configuration initiale de la production"
    echo "  start      - Démarrer l'application en production"
    echo "  stop       - Arrêter l'application en production"
    echo "  restart    - Redémarrer l'application en production"
    echo "  logs       - Afficher les logs"
    echo "  status     - Afficher le statut"
    echo "  ssl-renew  - Renouveler le certificat SSL"
    echo "  backup     - Sauvegarder les données"
    echo "  clean      - Nettoyer les conteneurs et images"
    echo "  help       - Afficher cette aide"
    echo ""
    echo "Configuration:"
    echo "  - Modifiez DOMAIN et EMAIL dans ce script"
    echo "  - Configurez votre fichier .env"
    echo "  - Assurez-vous que votre domaine pointe vers ce serveur"
    echo ""
    echo "Exemples:"
    echo "  $0 setup     # Configuration initiale"
    echo "  $0 start     # Démarrer en production"
    echo "  $0 backup    # Sauvegarder les données"
}

# Main
main() {
    print_header
    
    # Vérifications préliminaires
    check_docker
    
    case "${1:-help}" in
        setup)
            check_env
            setup_production
            ;;
        start)
            check_env
            start_production
            ;;
        stop)
            stop_production
            ;;
        restart)
            check_env
            restart_production
            ;;
        logs)
            show_logs
            ;;
        status)
            show_status
            ;;
        ssl-renew)
            renew_ssl
            ;;
        backup)
            backup_data
            ;;
        clean)
            clean_production
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            print_error "Commande inconnue: $1"
            show_help
            exit 1
            ;;
    esac
}

# Exécuter le script
main "$@" 