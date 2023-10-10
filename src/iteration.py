from .agent_creation import Agent
from .result_review import Result
from .task_management import Task

class Iteration:
    def __init__(self, agent: Agent, task: Task, result: Result):
        self.agent = agent
        self.task = task
        self.result = result

    def retrain_agent(self, examples: list):
        """
        Retrain the agent with more examples
        """
        self.agent.train(examples)

    def provide_feedback(self, feedback: str):
        """
        Provide feedback to improve the agent
        """
        self.agent.receive_feedback(feedback)

    def enhance_conversation(self, conversation: dict):
        """
        Enhance the conversation by adding more context or details
        """
        self.task.add_conversation(conversation)

    def iterate(self, examples: list, feedback: str, conversation: dict):
        """
        Iterate over the agent by retraining, providing feedback and enhancing conversation
        """
        self.retrain_agent(examples)
        self.provide_feedback(feedback)
        self.enhance_conversation(conversation)