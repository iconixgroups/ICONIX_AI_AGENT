from flask import Flask, render_template, request, redirect, url_for
from src.agent_creation import createAgent, submitTask, customizeTask
from src.integrations import connectAIPlatform

app = Flask(__name__)

@app.route('/agent_builder', methods=['GET', 'POST'])
def agent_builder():
    if request.method == 'POST':
        agent_name = request.form['agentNameInput']
        agent_model = request.form['agentModelSelect']
        ai_platform = request.form['aiPlatformSelect']
        agent = createAgent(agent_name, agent_model)
        connectAIPlatform(agent, ai_platform)
        return redirect(url_for('dashboard'))
    return render_template('agent_builder.html')

@app.route('/task_submission', methods=['POST'])
def task_submission():
    task = request.form['taskInput']
    agent_id = request.form['agentId']
    submitTask(agent_id, task)
    return redirect(url_for('dashboard'))

@app.route('/task_customization', methods=['POST'])
def task_customization():
    task_id = request.form['taskId']
    customization = request.form['customizationInput']
    customizeTask(task_id, customization)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
