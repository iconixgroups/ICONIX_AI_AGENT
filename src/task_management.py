from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['iconix_ai_agent']
tasks_collection = db['tasks']

# Shared schemas
from src.shared_schemas import TaskSchema

def submit_task(user_id, agent_id, task):
    """
    Function to submit a task to an agent
    """
    task_data = {
        'user_id': ObjectId(user_id),
        'agent_id': ObjectId(agent_id),
        'task': task,
        'status': 'pending'
    }
    result = tasks_collection.insert_one(TaskSchema().load(task_data))
    return str(result.inserted_id)

def view_tasks(user_id, agent_id):
    """
    Function to view tasks of an agent
    """
    tasks = tasks_collection.find({'user_id': ObjectId(user_id), 'agent_id': ObjectId(agent_id)})
    return [TaskSchema().dump(task) for task in tasks]

def update_task_status(task_id, status):
    """
    Function to update the status of a task
    """
    tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'status': status}})

def resubmit_task(task_id):
    """
    Function to resubmit a task
    """
    tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'status': 'pending'}})

def regenerate_task(task_id, new_task):
    """
    Function to regenerate a task
    """
    tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'task': new_task, 'status': 'pending'}})