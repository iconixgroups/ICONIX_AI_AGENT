from flask import Flask, request, jsonify
from src.user_management import signup, login
from src.template_library import browse_template
from src.agent_creation import create_agent
from src.task_management import submit_task
from src.result_review import review_result
from src.iteration import retrain
from src.integrations import integrate
from src.chat_platforms import chat
from src.tools import use_tools

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    return signup(request)

@app.route('/login', methods=['POST'])
def login():
    return login(request)

@app.route('/browse-template', methods=['GET'])
def browse_template():
    return browse_template(request)

@app.route('/create-agent', methods=['POST'])
def create_agent():
    return create_agent(request)

@app.route('/submit-task', methods=['POST'])
def submit_task():
    return submit_task(request)

@app.route('/review-result', methods=['GET'])
def review_result():
    return review_result(request)

@app.route('/retrain', methods=['POST'])
def retrain():
    return retrain(request)

@app.route('/integrate', methods=['POST'])
def integrate():
    return integrate(request)

@app.route('/chat', methods=['POST'])
def chat():
    return chat(request)

@app.route('/tools', methods=['POST'])
def use_tools():
    return use_tools(request)

if __name__ == '__main__':
    app.run(debug=True)