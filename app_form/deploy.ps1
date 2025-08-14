# Script de déploiement PowerShell pour Assistant Magistère
# Usage: .\deploy.ps1 [build|start|stop|restart|logs|clean|tag|push|release]

param(
    [Parameter(Position=0)]
    [string]$Command = "help",
    
    [Parameter(Position=1)]
    [string]$VersionTag = ""
)

# Configuration
$ImageName = "app_form-assistant-magistere"
$ContainerName = "assistant-magistere"
$Port = "5000"

# Configuration Docker Hub (à configurer dans .env)
$DockerHubUsername = ""
$DockerHubRepository = "assistant-magistere"
$DockerHubTag = "latest"

# Fonction pour afficher les messages
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
    Write-Host "================================" -ForegroundColor Blue
    Write-Host "  Assistant Magistère - Deploy" -ForegroundColor Blue
    Write-Host "================================" -ForegroundColor Blue
}

# Vérifier si Docker est installé
function Test-Docker {
    try {
        docker --version | Out-Null
        docker-compose --version | Out-Null
    }
    catch {
        Write-Error "Docker ou Docker Compose n'est pas installé. Veuillez installer Docker Desktop d'abord."
        exit 1
    }
}

# Vérifier les variables d'environnement
function Test-Environment {
    if (-not (Test-Path ".env")) {
        Write-Warning "Fichier .env non trouvé. Création d'un template..."
        Copy-Item "env_template.txt" ".env"
        Write-Warning "Veuillez configurer votre clé API OpenAI dans le fichier .env"
        Write-Warning "Exemple: OPENAI_API_KEY=sk-your-api-key-here"
        exit 1
    }
    
    $envContent = Get-Content ".env"
    if (-not ($envContent | Select-String "OPENAI_API_KEY=sk-")) {
        Write-Error "Clé API OpenAI non configurée dans .env"
        Write-Error "Veuillez ajouter votre clé API OpenAI dans le fichier .env"
        exit 1
    }
}

# Charger les variables Docker Hub depuis .env
function Load-DockerHubConfig {
    if (Test-Path ".env") {
        $envContent = Get-Content ".env"
        foreach ($line in $envContent) {
            if ($line -match "^DOCKER_HUB_USERNAME=(.+)$") {
                $script:DockerHubUsername = $matches[1]
            }
            elseif ($line -match "^DOCKER_HUB_REPOSITORY=(.+)$") {
                $script:DockerHubRepository = $matches[1]
            }
            elseif ($line -match "^DOCKER_HUB_TAG=(.+)$") {
                $script:DockerHubTag = $matches[1]
            }
        }
    }
    
    if ([string]::IsNullOrEmpty($DockerHubUsername)) {
        $script:DockerHubUsername = ""
    }
    if ([string]::IsNullOrEmpty($DockerHubRepository)) {
        $script:DockerHubRepository = "assistant-magistere"
    }
    if ([string]::IsNullOrEmpty($DockerHubTag)) {
        $script:DockerHubTag = "latest"
    }
}

# Générer un tag de version
function Get-VersionTag {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    try {
        $gitCommit = git rev-parse --short HEAD 2>$null
        if ($LASTEXITCODE -ne 0) {
            $gitCommit = "unknown"
        }
    }
    catch {
        $gitCommit = "unknown"
    }
    return "v${timestamp}-${gitCommit}"
}

# Fonction build
function Build-Image {
    Write-Info "Construction de l'image Docker..."
    docker-compose build --no-cache
    if ($LASTEXITCODE -eq 0) {
        Write-Info "Image construite avec succès!"
    }
    else {
        Write-Error "Erreur lors de la construction de l'image"
        exit 1
    }
}

# Fonction tag
function Tag-Image {
    param([string]$VersionTag = "")
    
    Load-DockerHubConfig
    
    if ([string]::IsNullOrEmpty($DockerHubUsername)) {
        Write-Error "DOCKER_HUB_USERNAME non configuré dans .env"
        Write-Error "Ajoutez DOCKER_HUB_USERNAME=votre-username dans le fichier .env"
        exit 1
    }
    
    if ([string]::IsNullOrEmpty($VersionTag)) {
        $VersionTag = Get-VersionTag
    }
    
    $fullImageName = "${DockerHubUsername}/${DockerHubRepository}:${VersionTag}"
    $latestTag = "${DockerHubUsername}/${DockerHubRepository}:latest"
    
    Write-Info "Tagging de l'image..."
    Write-Info "Version: ${VersionTag}"
    Write-Info "Image: ${fullImageName}"
    
    # Tagger l'image avec la version
    docker tag "${ImageName}:latest" $fullImageName
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Erreur lors du tagging de l'image"
        exit 1
    }
    
    # Tagger aussi comme latest si ce n'est pas déjà latest
    if ($VersionTag -ne "latest") {
        docker tag "${ImageName}:latest" $latestTag
    }
    
    Write-Info "Images taggées avec succès!"
    Write-Info "Version: ${fullImageName}"
    Write-Info "Latest: ${latestTag}"
    
    # Sauvegarder le tag de version
    $VersionTag | Out-File -FilePath ".version_tag" -Encoding UTF8
}

# Fonction push
function Push-Image {
    param([string]$VersionTag = "")
    
    Load-DockerHubConfig
    
    if ([string]::IsNullOrEmpty($DockerHubUsername)) {
        Write-Error "DOCKER_HUB_USERNAME non configuré dans .env"
        exit 1
    }
    
    if ([string]::IsNullOrEmpty($VersionTag)) {
        if (Test-Path ".version_tag") {
            $VersionTag = Get-Content ".version_tag" -Raw
        }
        else {
            $VersionTag = "latest"
        }
    }
    
    $fullImageName = "${DockerHubUsername}/${DockerHubRepository}:${VersionTag}"
    $latestTag = "${DockerHubUsername}/${DockerHubRepository}:latest"
    
    Write-Info "Pushing vers Docker Hub..."
    Write-Info "Version: ${VersionTag}"
    
    # Vérifier si l'utilisateur est connecté à Docker Hub
    $dockerInfo = docker info 2>$null
    if ($dockerInfo -notmatch "Username") {
        Write-Warning "Vous n'êtes pas connecté à Docker Hub"
        Write-Info "Exécutez: docker login"
        exit 1
    }
    
    # Pousser l'image versionnée
    docker push $fullImageName
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Erreur lors du push de l'image"
        exit 1
    }
    
    # Pousser aussi le tag latest
    if ($VersionTag -ne "latest") {
        docker push $latestTag
    }
    
    Write-Info "Images poussées avec succès vers Docker Hub!"
    Write-Info "Version: ${fullImageName}"
    Write-Info "Latest: ${latestTag}"
}

# Fonction release (build + tag + push)
function Release-Image {
    param([string]$VersionTag = "")
    
    if ([string]::IsNullOrEmpty($VersionTag)) {
        $VersionTag = Get-VersionTag
    }
    
    Write-Info "Démarrage du processus de release..."
    Write-Info "Version: ${VersionTag}"
    
    # Build
    Build-Image
    
    # Tag
    Tag-Image $VersionTag
    
    # Push
    Push-Image $VersionTag
    
    Write-Info "Release ${VersionTag} terminée avec succès!"
    Write-Info "Image disponible sur Docker Hub: ${DockerHubUsername}/${DockerHubRepository}:${VersionTag}"
}

# Fonction start
function Start-Application {
    Write-Info "Démarrage de l'application..."
    docker-compose up -d
    if ($LASTEXITCODE -eq 0) {
        Write-Info "Application démarrée!"
        Write-Info "Accédez à l'application: http://localhost:$Port"
    }
    else {
        Write-Error "Erreur lors du démarrage de l'application"
        exit 1
    }
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
function Clean-Environment {
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
    Write-Host "Usage: .\deploy.ps1 [COMMAND] [VERSION_TAG]"
    Write-Host ""
    Write-Host "Commandes disponibles:"
    Write-Host "  build     - Construire l'image Docker"
    Write-Host "  start     - Démarrer l'application"
    Write-Host "  stop      - Arrêter l'application"
    Write-Host "  restart   - Redémarrer l'application"
    Write-Host "  logs      - Afficher les logs"
    Write-Host "  status    - Afficher le statut"
    Write-Host "  clean     - Nettoyer les conteneurs et images"
    Write-Host "  tag       - Tagger l'image pour Docker Hub"
    Write-Host "  push      - Pousser l'image vers Docker Hub"
    Write-Host "  release   - Build + Tag + Push (release complète)"
    Write-Host "  help      - Afficher cette aide"
    Write-Host ""
    Write-Host "Exemples:"
    Write-Host "  .\deploy.ps1 build                    # Construire l'image"
    Write-Host "  .\deploy.ps1 tag v1.0.0              # Tagger avec version spécifique"
    Write-Host "  .\deploy.ps1 tag                     # Tagger avec version auto-générée"
    Write-Host "  .\deploy.ps1 push v1.0.0             # Pousser version spécifique"
    Write-Host "  .\deploy.ps1 release v1.0.0          # Release complète"
    Write-Host "  .\deploy.ps1 release                  # Release avec version auto-générée"
    Write-Host ""
    Write-Host "Configuration Docker Hub (.env):"
    Write-Host "  DOCKER_HUB_USERNAME=votre-username"
    Write-Host "  DOCKER_HUB_REPOSITORY=assistant-magistere"
    Write-Host "  DOCKER_HUB_TAG=latest"
}

# Main
function Main {
    Write-Header
    
    # Vérifications préliminaires
    Test-Docker
    
    switch ($Command.ToLower()) {
        "build" {
            Test-Environment
            Build-Image
        }
        "start" {
            Test-Environment
            Start-Application
        }
        "stop" {
            Stop-Application
        }
        "restart" {
            Test-Environment
            Restart-Application
        }
        "logs" {
            Show-Logs
        }
        "status" {
            Show-Status
        }
        "clean" {
            Clean-Environment
        }
        "tag" {
            Test-Environment
            Tag-Image $VersionTag
        }
        "push" {
            Test-Environment
            Push-Image $VersionTag
        }
        "release" {
            Test-Environment
            Release-Image $VersionTag
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