from flask import Blueprint, render_template
from src.user_management import User
from src.agent_creation import Agent
from src.result_review import Result
from src.task_management import Task

agent_analytics_bp = Blueprint('agent_analytics_bp', __name__)

@agent_analytics_bp.route('/agent-analytics', methods=['GET'])
def agent_analytics():
    user = User.get_current_user()
    agents = Agent.get_agents_by_user(user)
    agent_analytics = []

    for agent in agents:
        tasks = Task.get_tasks_by_agent(agent)
        results = Result.get_results_by_agent(agent)
        agent_analytics.append({
            'agent': agent,
            'tasks': tasks,
            'results': results,
            'users': len(set([task.user for task in tasks])),
            'conversations': len(tasks),
            'usage': sum([result.usage for result in results]),
            'sentiment': sum([result.sentiment for result in results]) / len(results) if results else 0,
            'missed_questions': sum([result.missed_questions for result in results]) if results else 0,
            'feedback': sum([result.feedback for result in results]) if results else 0
        })

    return render_template('agent-analytics.html', agent_analytics=agent_analytics)
