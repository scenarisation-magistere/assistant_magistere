#!/bin/bash

# Script de déploiement pour Assistant Magistère
# Usage: ./deploy.sh [build|start|stop|restart|logs|clean|tag|push|release]

set -e

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
IMAGE_NAME="app_form-assistant-magistere"
CONTAINER_NAME="assistant-magistere"
PORT="5000"

# Configuration Docker Hub (à configurer dans .env)
DOCKER_HUB_USERNAME=""
DOCKER_HUB_REPOSITORY="assistant-magistere"
DOCKER_HUB_TAG="latest"


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

# Charger les variables Docker Hub depuis .env
load_docker_hub_config() {
    if [ -f .env ]; then
        export $(grep -v '^#' .env | xargs)
        DOCKER_HUB_USERNAME=${DOCKER_HUB_USERNAME:-""}
        DOCKER_HUB_REPOSITORY=${DOCKER_HUB_REPOSITORY:-"assistant-magistere"}
        DOCKER_HUB_TAG=${DOCKER_HUB_TAG:-"latest"}
    fi
}

# Générer un tag de version
generate_version_tag() {
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local git_commit=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
    echo "v${timestamp}-${git_commit}"
}

# Charger les variables Docker Hub depuis .env
load_docker_hub_config() {
    if [ -f .env ]; then
        export $(grep -v '^#' .env | xargs)
        DOCKER_HUB_USERNAME=${DOCKER_HUB_USERNAME:-""}
        DOCKER_HUB_REPOSITORY=${DOCKER_HUB_REPOSITORY:-"assistant-magistere"}
        DOCKER_HUB_TAG=${DOCKER_HUB_TAG:-"latest"}
    fi
}

# Générer un tag de version
generate_version_tag() {
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local git_commit=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
    echo "v${timestamp}-${git_commit}"
}

# Fonction build
build() {
    print_message "Construction de l'image Docker..."
    docker-compose build --no-cache
    print_message "Image construite avec succès!"
}

# Fonction tag
tag() {
    load_docker_hub_config
    
    if [ -z "$DOCKER_HUB_USERNAME" ]; then
        print_error "DOCKER_HUB_USERNAME non configuré dans .env"
        print_error "Ajoutez DOCKER_HUB_USERNAME=votre-username dans le fichier .env"
        exit 1
    fi
    
    local version_tag=${1:-$(generate_version_tag)}
    local full_image_name="${DOCKER_HUB_USERNAME}/${DOCKER_HUB_REPOSITORY}:${version_tag}"
    local latest_tag="${DOCKER_HUB_USERNAME}/${DOCKER_HUB_REPOSITORY}:latest"
    
    print_message "Tagging de l'image..."
    print_message "Version: ${version_tag}"
    print_message "Image: ${full_image_name}"
    
    # Tagger l'image avec la version
    docker tag ${IMAGE_NAME}:latest ${full_image_name}
    
    # Tagger aussi comme latest si ce n'est pas déjà latest
    if [ "$version_tag" != "latest" ]; then
        docker tag ${IMAGE_NAME}:latest ${latest_tag}
    fi
    
    print_message "Images taggées avec succès!"
    print_message "Version: ${full_image_name}"
    print_message "Latest: ${latest_tag}"
    
    # Sauvegarder le tag de version
    echo "$version_tag" > .version_tag
}

# Fonction push
push() {
    load_docker_hub_config
    
    if [ -z "$DOCKER_HUB_USERNAME" ]; then
        print_error "DOCKER_HUB_USERNAME non configuré dans .env"
        exit 1
    fi
    
    local version_tag=${1:-$(cat .version_tag 2>/dev/null || echo "latest")}
    local full_image_name="${DOCKER_HUB_USERNAME}/${DOCKER_HUB_REPOSITORY}:${version_tag}"
    local latest_tag="${DOCKER_HUB_USERNAME}/${DOCKER_HUB_REPOSITORY}:latest"
    
    print_message "Pushing vers Docker Hub..."
    print_message "Version: ${version_tag}"
    
    # Vérifier si l'utilisateur est connecté à Docker Hub
    if ! docker info | grep -q "Username"; then
        print_warning "Vous n'êtes pas connecté à Docker Hub"
        print_message "Exécutez: docker login"
        exit 1
    fi
    
    # Pousser l'image versionnée
    docker push ${full_image_name}
    
    # Pousser aussi le tag latest
    if [ "$version_tag" != "latest" ]; then
        docker push ${latest_tag}
    fi
    
    print_message "Images poussées avec succès vers Docker Hub!"
    print_message "Version: ${full_image_name}"
    print_message "Latest: ${latest_tag}"
}

# Fonction release (build + tag + push)
release() {
    local version_tag=${1:-$(generate_version_tag)}
    
    print_message "Démarrage du processus de release..."
    print_message "Version: ${version_tag}"
    
    # Build
    build
    
    # Tag
    tag "$version_tag"
    
    # Push
    push "$version_tag"
    
    print_message "Release ${version_tag} terminée avec succès!"
    print_message "Image disponible sur Docker Hub: ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_REPOSITORY}:${version_tag}"
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
    echo "Usage: $0 [COMMAND] [VERSION_TAG]"
    echo ""
    echo "Commandes disponibles:"
    echo "  build     - Construire l'image Docker"
    echo "  start     - Démarrer l'application"
    echo "  stop      - Arrêter l'application"
    echo "  restart   - Redémarrer l'application"
    echo "  logs      - Afficher les logs"
    echo "  status    - Afficher le statut"
    echo "  clean     - Nettoyer les conteneurs et images"
    echo "  tag       - Tagger l'image pour Docker Hub"
    echo "  push      - Pousser l'image vers Docker Hub"
    echo "  release   - Build + Tag + Push (release complète)"
    echo "  help      - Afficher cette aide"
    echo ""
    echo "Exemples:"
    echo "  $0 build                    # Construire l'image"
    echo "  $0 tag v1.0.0              # Tagger avec version spécifique"
    echo "  $0 tag                     # Tagger avec version auto-générée"
    echo "  $0 push v1.0.0             # Pousser version spécifique"
    echo "  $0 release v1.0.0          # Release complète"
    echo "  $0 release                  # Release avec version auto-générée"
    echo ""
    echo "Configuration Docker Hub (.env):"
    echo "  DOCKER_HUB_USERNAME=votre-username"
    echo "  DOCKER_HUB_REPOSITORY=assistant-magistere"
    echo "  DOCKER_HUB_TAG=latest"
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
        tag)
            check_env
            tag "$2"
            ;;
        push)
            check_env
            push "$2"
            ;;
        release)
            check_env
            release "$2"
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