from flask import Flask
import os

# Import route modules
from routes.main import register_main_routes
from routes.public_cible import register_public_cible_routes
from routes.contraintes import register_contraintes_routes
from routes.competences import register_competences_routes
from routes.referentiels import register_referentiels_routes
from routes.contenu import register_contenu_routes
from routes.recap import register_recap_routes
from routes.test_header import init_test_routes

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = 'your-secret-key-here'  # Required for session management

# Register all route modules
register_main_routes(app)
register_public_cible_routes(app)
register_contraintes_routes(app)
register_competences_routes(app)
register_referentiels_routes(app)
register_contenu_routes(app)
register_recap_routes(app)
init_test_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
