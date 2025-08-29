# Configuration file for page navigation
# Defines the flow between pages with previous and next page information

# Color configuration for headers
HEADER_COLORS = {
    'primary': 'var(--gradient-primary)',    # Blue gradient
    'success': 'var(--gradient-success)',    # Green gradient
    'danger': 'var(--gradient-danger)',      # Red gradient
    'secondary': 'var(--gradient-secondary)', # Purple gradient
    'gray': 'var(--gradient-gray)',          # Gray gradient
    'info': 'var(--gradient-info)'           # Info gradient
}


# --- Palette Bootstrap classique (contrastes) ---
HEADER_COLORS = {
    'primary': 'var(--gradient-primary)',     # Bleu = cadrage
    'danger': 'var(--gradient-danger)',       # Rouge = contraintes
    'secondary': 'var(--gradient-secondary)', # Violet = réflexion/structuration
    'success': 'var(--gradient-success)',     # Vert = validation
    'info': 'var(--gradient-info)',           # Bleu clair = création
    'gray': 'var(--gradient-gray)'            # Gris = clôture
}

# Common configuration
TOTAL_STEPS = 6

def apply_header_color(page_config, color_key):
    """Apply header color gradient to page config"""
    if color_key in HEADER_COLORS:
        page_config['header_gradient'] = HEADER_COLORS[color_key]
    return page_config

# Base page configurations
BASE_PAGES_CONFIG = {
    'public_cible': {
        'name': 'Public Cible',
        'step': 1,
        'previous': None,
        'next': 'contraintes',
        'route': '/public-cible',
        'template': 'public_cible.html'
    },
    'contraintes': {
        'name': 'Contraintes',
        'step': 2,
        'previous': 'public_cible',
        'next': 'competences',
        'route': '/contraintes',
        'template': 'contraintes.html'
    },
    'competences': {
        'name': 'Compétences',
        'step': 3,
        'previous': 'contraintes',
        'next': 'referentiels',
        'route': '/competences',
        'template': 'competences.html'
    },
    'referentiels': {
        'name': 'Référentiels',
        'step': 4,
        'previous': 'competences',
        'next': 'contenu',
        'route': '/referentiels',
        'template': 'referentiels.html'
    },
    'contenu': {
        'name': 'Contenus par Section',
        'step': 5,
        'previous': 'referentiels',
        'next': 'recap',
        'route': '/contenu',
        'template': 'contenu.html'
    },
    'recap': {
        'name': 'Récapitulatif Macrodesign',
        'step': 6,
        'previous': 'contenu',
        'next': None,
        'route': '/recap',
        'template': 'recap.html'
    }
}

# Apply colors to create final PAGES_CONFIG
PAGES_CONFIG = {
    'public_cible': apply_header_color(BASE_PAGES_CONFIG['public_cible'].copy(), 'primary'),
    'contraintes': apply_header_color(BASE_PAGES_CONFIG['contraintes'].copy(), 'danger'),
    'competences': apply_header_color(BASE_PAGES_CONFIG['competences'].copy(), 'secondary'),
    'referentiels': apply_header_color(BASE_PAGES_CONFIG['referentiels'].copy(), 'success'),
    'contenu': apply_header_color(BASE_PAGES_CONFIG['contenu'].copy(), 'info'),
    'recap': apply_header_color(BASE_PAGES_CONFIG['recap'].copy(), 'gray')
}

PAGES_CONFIG = {
    'public_cible': apply_header_color(BASE_PAGES_CONFIG['public_cible'].copy(), 'primary'),
    'contraintes': apply_header_color(BASE_PAGES_CONFIG['contraintes'].copy(), 'danger'),
    'competences': apply_header_color(BASE_PAGES_CONFIG['competences'].copy(), 'secondary'),
    'referentiels': apply_header_color(BASE_PAGES_CONFIG['referentiels'].copy(), 'success'),
    'contenu': apply_header_color(BASE_PAGES_CONFIG['contenu'].copy(), 'info'),
    'recap': apply_header_color(BASE_PAGES_CONFIG['recap'].copy(), 'gray')
}

def get_page_config(page_name):
    """Get configuration for a specific page"""
    return PAGES_CONFIG.get(page_name, {})

def get_navigation_info(page_name):
    """Get navigation information for a page (previous, next, step info)"""
    config = get_page_config(page_name)
    if not config:
        return {}
    
    return {
        'current_page': page_name,
        'current_name': config.get('name', ''),
        'step': config.get('step', 1),
        'total_steps': TOTAL_STEPS,
        'previous_page': config.get('previous'),
        'previous_route': PAGES_CONFIG.get(config.get('previous'), {}).get('route', '#') if config.get('previous') else None,
        'next_page': config.get('next'),
        'next_route': PAGES_CONFIG.get(config.get('next'), {}).get('route', '#') if config.get('next') else None,
        'is_first': config.get('previous') is None,
        'is_last': config.get('next') is None
    }

def get_all_pages():
    """Get list of all pages in order"""
    return list(PAGES_CONFIG.keys())

def get_page_by_step(step):
    """Get page name by step number"""
    for page_name, config in PAGES_CONFIG.items():
        if config.get('step') == step:
            return page_name
    return None

def get_page_name_by_step(step):
    """Get page display name by step number"""
    for page_name, config in PAGES_CONFIG.items():
        if config.get('step') == step:
            return config.get('name', page_name)
    return f'Étape {step}'
