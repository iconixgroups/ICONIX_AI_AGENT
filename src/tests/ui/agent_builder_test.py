```python
import unittest
from src.ui.agent_builder import AgentBuilder

class TestAgentBuilder(unittest.TestCase):

    def setUp(self):
        self.agent_builder = AgentBuilder()

    def test_create_agent(self):
        agent_name = "Test Agent"
        ai_model = "GPT-3"
        self.agent_builder.create_agent(agent_name, ai_model)
        self.assertEqual(self.agent_builder.agent.name, agent_name)
        self.assertEqual(self.agent_builder.agent.model, ai_model)

    def test_set_goals(self):
        goals = ["Answer FAQs", "Collect data"]
        self.agent_builder.set_goals(goals)
        self.assertEqual(self.agent_builder.agent.goals, goals)

    def test_auto_generate_tasks(self):
        self.agent_builder.set_goals(["Answer FAQs"])
        self.agent_builder.auto_generate_tasks()
        self.assertTrue(len(self.agent_builder.agent.tasks) > 0)

    def test_customize_task(self):
        self.agent_builder.set_goals(["Answer FAQs"])
        self.agent_builder.auto_generate_tasks()
        task_id = self.agent_builder.agent.tasks[0].id
        new_task_description = "Answer questions about pricing"
        self.agent_builder.customize_task(task_id, new_task_description)
        self.assertEqual(self.agent_builder.agent.tasks[0].description, new_task_description)

    def test_train_agent(self):
        self.agent_builder.set_goals(["Answer FAQs"])
        self.agent_builder.auto_generate_tasks()
        self.agent_builder.train_agent()
        self.assertTrue(self.agent_builder.agent.is_trained)

    def test_add_api_key(self):
        api_key = "1234567890"
        self.agent_builder.add_api_key(api_key)
        self.assertEqual(self.agent_builder.agent.api_key, api_key)

    def test_simulate_conversation(self):
        self.agent_builder.set_goals(["Answer FAQs"])
        self.agent_builder.auto_generate_tasks()
        self.agent_builder.train_agent()
        conversation = self.agent_builder.simulate_conversation("What is your pricing?")
        self.assertTrue(len(conversation) > 0)

if __name__ == '__main__':
    unittest.main()
```