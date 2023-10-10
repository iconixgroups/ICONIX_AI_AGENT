# Import modules
import src.user_management  # Ensure this line starts at the beginning of the line
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
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, EmailField
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import googleanalytics as ga
import segment
import dialogflow_v2 as dialogflow
from zendesk import Zendesk

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

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize JWTManager
jwt = JWTManager(app)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['iconix_ai_agent']
tasks_collection = db['tasks']

# Shared schemas
from src.shared_schemas import TaskSchema

# User model
class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

# User schema
class UserSchema:
    # define schema

# Run the application
if __name__ == '__main__':
    app.run(debug=True)