```python
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from schemas import AgentSchema

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['iconix_db']
agents = db['agents']

@app.route('/create_agent', methods=['POST'])
def create_agent():
    data = request.get_json()
    agent_name = data.get('agent_name')
    ai_model = data.get('ai_model')
    goals = data.get('goals')
    tasks = auto_generate_tasks(goals)
    agent_data = {
        'agent_name': agent_name,
        'ai_model': ai_model,
        'goals': goals,
        'tasks': tasks
    }
    agent_schema = AgentSchema()
    errors = agent_schema.validate(agent_data)
    if errors:
        return jsonify(errors), 400
    agent_id = agents.insert_one(agent_data).inserted_id
    return jsonify({'message': 'AGENT_CREATED', 'agent_id': str(agent_id)}), 201

def auto_generate_tasks(goals):
    tasks = []
    for goal in goals:
        task = {
            'goal': goal,
            'status': 'pending'
        }
        tasks.append(task)
    return tasks

if __name__ == '__main__':
    app.run(debug=True)
```