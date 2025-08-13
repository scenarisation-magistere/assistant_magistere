#!/bin/bash

# Script de déploiement pour Assistant Magistère
# Usage: ./deploy.sh [build|start|stop|restart|logs|clean]

set -e

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
IMAGE_NAME="assistant-magistere"
CONTAINER_NAME="assistant-magistere"
PORT="5000"

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
    echo -e "${BLUE}  Assistant Magistère - Deploy${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Vérifier si Docker est installé
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker n'est pas installé. Veuillez installer Docker d'abord."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose n'est pas installé. Veuillez installer Docker Compose d'abord."
        exit 1
    fi
}

# Vérifier les variables d'environnement
check_env() {
    if [ ! -f .env ]; then
        print_warning "Fichier .env non trouvé. Création d'un template..."
        cp env_template.txt .env
        print_warning "Veuillez configurer votre clé API OpenAI dans le fichier .env"
        print_warning "Exemple: OPENAI_API_KEY=sk-your-api-key-here"
        exit 1
    fi
    
    if ! grep -q "OPENAI_API_KEY=sk-" .env; then
        print_error "Clé API OpenAI non configurée dans .env"
        print_error "Veuillez ajouter votre clé API OpenAI dans le fichier .env"
        exit 1
    fi
}

# Fonction build
build() {
    print_message "Construction de l'image Docker..."
    docker-compose build --no-cache
    print_message "Image construite avec succès!"
}

# Fonction start
start() {
    print_message "Démarrage de l'application..."
    docker-compose up -d
    print_message "Application démarrée!"
    print_message "Accédez à l'application: http://localhost:$PORT"
}

# Fonction stop
stop() {
    print_message "Arrêt de l'application..."
    docker-compose down
    print_message "Application arrêtée!"
}

# Fonction restart
restart() {
    print_message "Redémarrage de l'application..."
    docker-compose down
    docker-compose up -d
    print_message "Application redémarrée!"
    print_message "Accédez à l'application: http://localhost:$PORT"
}

# Fonction logs
logs() {
    print_message "Affichage des logs..."
    docker-compose logs -f
}

# Fonction clean
clean() {
    print_warning "Nettoyage des conteneurs et images..."
    docker-compose down --rmi all --volumes --remove-orphans
    docker system prune -f
    print_message "Nettoyage terminé!"
}

# Fonction status
status() {
    print_message "Statut de l'application..."
    docker-compose ps
}

# Fonction help
show_help() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commandes disponibles:"
    echo "  build     - Construire l'image Docker"
    echo "  start     - Démarrer l'application"
    echo "  stop      - Arrêter l'application"
    echo "  restart   - Redémarrer l'application"
    echo "  logs      - Afficher les logs"
    echo "  status    - Afficher le statut"
    echo "  clean     - Nettoyer les conteneurs et images"
    echo "  help      - Afficher cette aide"
    echo ""
    echo "Exemples:"
    echo "  $0 build    # Construire l'image"
    echo "  $0 start    # Démarrer l'application"
    echo "  $0 logs     # Voir les logs en temps réel"
}

# Main
main() {
    print_header
    
    # Vérifications préliminaires
    check_docker
    
    case "${1:-help}" in
        build)
            check_env
            build
            ;;
        start)
            check_env
            start
            ;;
        stop)
            stop
            ;;
        restart)
            check_env
            restart
            ;;
        logs)
            logs
            ;;
        status)
            status
            ;;
        clean)
            clean
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