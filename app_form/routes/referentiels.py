from flask import render_template
from questions.referentiels import referentiels_page, generate_referentiel, save_referentiel, update_referentiel
from .main import check_previous_steps_completed
from config.pages_config import get_navigation_info, get_page_config

def register_referentiels_routes(app):
    """Register referentiels routes with the Flask app"""
    
    @app.route('/referentiels')
    def referentiels():
        """Handle the referentiels page"""
        # Check if previous steps are completed
        completed, message = check_previous_steps_completed(['etape_1_public_cible', 'etape_2_contraintes', 'etape_4_competences'])
        if not completed:
            return render_template('error.html', message=f"Veuillez d'abord compléter les étapes précédentes. {message}")
        
        nav_info = get_navigation_info('referentiels')
        page_config = get_page_config('referentiels')
        return referentiels_page(nav_info=nav_info, header_gradient=page_config.get('header_gradient', 'var(--gradient-success)'))

    @app.route('/generate_referentiel', methods=['POST'])
    def generate_referentiel_route():
        """Generate a referentiel for a specific section"""
        return generate_referentiel()

    @app.route('/save_referentiel', methods=['POST'])
    def save_referentiel_route():
        """Save the referentiel to YAML"""
        return save_referentiel()

    @app.route('/update_referentiel', methods=['POST'])
    def update_referentiel_route():
        """Update an existing referentiel based on user feedback"""
        return update_referentiel()
