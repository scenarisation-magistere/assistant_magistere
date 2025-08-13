# Script de déploiement PowerShell pour Assistant Magistère
# Usage: .\deploy.ps1 [build|start|stop|restart|logs|clean]

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

# Configuration
$ImageName = "assistant-magistere"
$ContainerName = "assistant-magistere"
$Port = "5000"

# Fonctions pour les messages
function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Write-Header {
    Write-Host "=================================" -ForegroundColor Blue
    Write-Host "  Assistant Magistère - Deploy" -ForegroundColor Blue
    Write-Host "=================================" -ForegroundColor Blue
}

# Vérifier si Docker est installé
function Test-Docker {
    try {
        $null = docker --version
        $null = docker-compose --version
        return $true
    }
    catch {
        Write-Error "Docker ou Docker Compose n'est pas installé."
        Write-Error "Veuillez installer Docker Desktop pour Windows."
        return $false
    }
}

# Vérifier les variables d'environnement
function Test-Environment {
    if (-not (Test-Path ".env")) {
        Write-Warning "Fichier .env non trouvé. Création d'un template..."
        Copy-Item "env_template.txt" ".env"
        Write-Warning "Veuillez configurer votre clé API OpenAI dans le fichier .env"
        Write-Warning "Exemple: OPENAI_API_KEY=sk-your-api-key-here"
        return $false
    }
    
    $envContent = Get-Content ".env" -Raw
    if ($envContent -notmatch "OPENAI_API_KEY=sk-") {
        Write-Error "Clé API OpenAI non configurée dans .env"
        Write-Error "Veuillez ajouter votre clé API OpenAI dans le fichier .env"
        return $false
    }
    
    return $true
}

# Fonction build
function Build-Application {
    Write-Info "Construction de l'image Docker..."
    docker-compose build --no-cache
    Write-Info "Image construite avec succès!"
}

# Fonction start
function Start-Application {
    Write-Info "Démarrage de l'application..."
    docker-compose up -d
    Write-Info "Application démarrée!"
    Write-Info "Accédez à l'application: http://localhost:$Port"
}

# Fonction stop
function Stop-Application {
    Write-Info "Arrêt de l'application..."
    docker-compose down
    Write-Info "Application arrêtée!"
}

# Fonction restart
function Restart-Application {
    Write-Info "Redémarrage de l'application..."
    docker-compose down
    docker-compose up -d
    Write-Info "Application redémarrée!"
    Write-Info "Accédez à l'application: http://localhost:$Port"
}

# Fonction logs
function Show-Logs {
    Write-Info "Affichage des logs..."
    docker-compose logs -f
}

# Fonction clean
function Clean-Application {
    Write-Warning "Nettoyage des conteneurs et images..."
    docker-compose down --rmi all --volumes --remove-orphans
    docker system prune -f
    Write-Info "Nettoyage terminé!"
}

# Fonction status
function Show-Status {
    Write-Info "Statut de l'application..."
    docker-compose ps
}

# Fonction help
function Show-Help {
    Write-Host "Usage: .\deploy.ps1 [COMMAND]"
    Write-Host ""
    Write-Host "Commandes disponibles:"
    Write-Host "  build     - Construire l'image Docker"
    Write-Host "  start     - Démarrer l'application"
    Write-Host "  stop      - Arrêter l'application"
    Write-Host "  restart   - Redémarrer l'application"
    Write-Host "  logs      - Afficher les logs"
    Write-Host "  status    - Afficher le statut"
    Write-Host "  clean     - Nettoyer les conteneurs et images"
    Write-Host "  help      - Afficher cette aide"
    Write-Host ""
    Write-Host "Exemples:"
    Write-Host "  .\deploy.ps1 build    # Construire l'image"
    Write-Host "  .\deploy.ps1 start    # Démarrer l'application"
    Write-Host "  .\deploy.ps1 logs     # Voir les logs en temps réel"
}

# Fonction principale
function Main {
    Write-Header
    
    # Vérifications préliminaires
    if (-not (Test-Docker)) {
        exit 1
    }
    
    switch ($Command.ToLower()) {
        "build" {
            if (Test-Environment) {
                Build-Application
            } else {
                exit 1
            }
        }
        "start" {
            if (Test-Environment) {
                Start-Application
            } else {
                exit 1
            }
        }
        "stop" {
            Stop-Application
        }
        "restart" {
            if (Test-Environment) {
                Restart-Application
            } else {
                exit 1
            }
        }
        "logs" {
            Show-Logs
        }
        "status" {
            Show-Status
        }
        "clean" {
            Clean-Application
        }
        "help" {
            Show-Help
        }
        default {
            Write-Error "Commande inconnue: $Command"
            Show-Help
            exit 1
        }
    }
}

# Exécuter le script
Main 