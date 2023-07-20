```python
from flask import Flask, render_template, request, session
from src.user_management import User
from src.agent_creation import Agent

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        user = User(session['username'])
        agents = Agent.get_agents_by_user(user)
        return render_template('dashboard.html', user=user, agents=agents)
    else:
        return redirect(url_for('login'))

@app.route('/create_agent', methods=['POST'])
def create_agent():
    if 'username' in session:
        user = User(session['username'])
        agent_name = request.form['agent_name']
        agent_model = request.form['agent_model']
        agent = Agent.create_agent(user, agent_name, agent_model)
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/access_template', methods=['GET'])
def access_template():
    if 'username' in session:
        return redirect(url_for('template_library'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```