from flask import Flask
import os
from datetime import datetime

# App version - UPDATE THIS WHEN YOU DEPLOY A NEW VERSION
APP_VERSION = "1.0.0"

# Import route modules
from routes.main import register_main_routes
from routes.public_cible import register_public_cible_routes
from routes.contraintes import register_contraintes_routes
from routes.competences import register_competences_routes
from routes.referentiels import register_referentiels_routes
from routes.contenu import register_contenu_routes
from routes.recap import register_recap_routes

# Get startup timestamp
startup_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"🚀 App starting at: {startup_timestamp}")
print(f"📦 App Version: {APP_VERSION}")

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = 'your-secret-key-here'  # Required for session management

# Store startup timestamp and version in app config for access in routes
app.config['STARTUP_TIMESTAMP'] = startup_timestamp
app.config['APP_VERSION'] = APP_VERSION

# Register all route modules
register_main_routes(app)
register_public_cible_routes(app)
register_contraintes_routes(app)
register_competences_routes(app)
register_referentiels_routes(app)
register_contenu_routes(app)
register_recap_routes(app)

if __name__ == '__main__':
    print(f"📅 Last app update: {startup_timestamp}")
    print(f"🎯 Running version: {APP_VERSION}")
    app.run(debug=True, host='0.0.0.0', port=5000)
