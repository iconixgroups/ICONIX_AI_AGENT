from flask import Flask, request, jsonify
from src.user_management import user_management
from src.template_library import template_library
from src.agent_creation import agent_creation
from src.task_management import task_management
from src.result_review import result_review
from src.iteration import iteration
from src.integrations import integrations
from src.chat_platforms import chat_platforms
from src.tools import tools

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    return user_management.createUser(request)

@app.route('/login', methods=['POST'])
def login():
    return user_management.loginUser(request)

@app.route('/browse-template', methods=['GET'])
def browse_template():
    return template_library.browseTemplate(request)

@app.route('/create-agent', methods=['POST'])
def create_agent():
    return agent_creation.createAgent(request)

@app.route('/submit-task', methods=['POST'])
def submit_task():
    return task_management.submitTask(request)

@app.route('/review-result', methods=['GET'])
def review_result():
    return result_review.generateResult(request)

@app.route('/retrain', methods=['POST'])
def retrain():
    return iteration.retrainAgent(request)

@app.route('/integrate', methods=['POST'])
def integrate():
    return integrations.connectAIPlatform(request)

@app.route('/chat', methods=['POST'])
def chat():
    return chat_platforms.integrateChatPlatform(request)

@app.route('/tools', methods=['POST'])
def use_tools():
    return tools.useAnalyticsTool(request)

if __name__ == '__main__':
    app.run(debug=True)