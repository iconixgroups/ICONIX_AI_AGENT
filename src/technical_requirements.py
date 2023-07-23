# src/technical_requirements.py

# Import necessary libraries
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)

# Enable CORS
CORS(app)

# Configure MongoDB settings
app.config['MONGODB_SETTINGS'] = {
    'db': 'iconix_db',
    'host': 'localhost',
    'port': 27017
}

# Initialize MongoEngine
db = MongoEngine()
db.init_app(app)

# Import modules
import src.user_management
import src.template_library
import src.agent_templates
import src.onboarding
import src.agent_creation
import src.task_management
import src.result_review
import src.iteration
import src.integrations
import src.chat_platforms
import src.tools
import src.ui.landing_page
import src.ui.dashboard
import src.ui.template_library
import src.ui.agent_builder
import src.ui.agent_analytics
import src.ui.agent_settings
import src.installation_guide
import src.infrastructure_setup

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
