from flask import Blueprint
from src.user_management import signup, login
from src.template_library import browse_templates, get_template, add_template, update_template, delete_template
from src.agent_creation import create_agent
from src.task_management import submit_task, view_tasks, update_task_status, resubmit_task, regenerate_task
from src.result_review import get_results, get_result, download_result, share_result
from src.iteration import retrain
from src.integrations import connect_ai
from src.tools import useAnalyticsTool, integrateSegment, integrateDialogflow, integrateZendesk
from src.shared_dependencies import app

main = Blueprint('main', __name__)

main.route('/signup', methods=['POST'])(signup)
main.route('/login', methods=['POST'])(login)
main.route('/browse-template', methods=['GET'])(browse_templates)
main.route('/get-template', methods=['GET'])(get_template)
main.route('/add-template', methods=['POST'])(add_template)
main.route('/update-template', methods=['PUT'])(update_template)
main.route('/delete-template', methods=['DELETE'])(delete_template)
main.route('/create-agent', methods=['POST'])(create_agent)
main.route('/submit-task', methods=['POST'])(submit_task)
main.route('/view-tasks', methods=['GET'])(view_tasks)
main.route('/update-task-status', methods=['PUT'])(update_task_status)
main.route('/resubmit-task', methods=['PUT'])(resubmit_task)
main.route('/regenerate-task', methods=['PUT'])(regenerate_task)
main.route('/get-results', methods=['GET'])(get_results)
main.route('/get-result', methods=['GET'])(get_result)
main.route('/download-result', methods=['GET'])(download_result)
main.route('/share-result', methods=['POST'])(share_result)
main.route('/retrain', methods=['POST'])(retrain)
main.route('/integrate', methods=['POST'])(connect_ai)
main.route('/use-analytics-tool', methods=['POST'])(useAnalyticsTool)
main.route('/integrate-segment', methods=['POST'])(integrateSegment)
main.route('/integrate-dialogflow', methods=['POST'])(integrateDialogflow)
main.route('/integrate-zendesk', methods=['POST'])(integrateZendesk)

app.register_blueprint(main)