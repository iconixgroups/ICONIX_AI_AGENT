```python
import unittest
from src.agent_creation import createAgent

class TestAgentCreation(unittest.TestCase):

    def setUp(self):
        self.user = {
            'username': 'testUser',
            'password': 'testPassword'
        }
        self.agent = {
            'name': 'testAgent',
            'model': 'GPT-3',
            'goals': ['Answer FAQs', 'Schedule appointments']
        }

    def test_create_agent(self):
        response = createAgent(self.user, self.agent)
        self.assertEqual(response['message'], 'AGENT_CREATED')
        self.assertEqual(response['agent']['name'], self.agent['name'])
        self.assertEqual(response['agent']['model'], self.agent['model'])
        self.assertEqual(response['agent']['goals'], self.agent['goals'])

    def test_create_agent_without_goals(self):
        self.agent.pop('goals')
        response = createAgent(self.user, self.agent)
        self.assertEqual(response['message'], 'AGENT_CREATED')
        self.assertEqual(response['agent']['name'], self.agent['name'])
        self.assertEqual(response['agent']['model'], self.agent['model'])
        self.assertNotIn('goals', response['agent'])

    def test_create_agent_without_name(self):
        self.agent.pop('name')
        response = createAgent(self.user, self.agent)
        self.assertEqual(response['message'], 'AGENT_CREATED')
        self.assertNotIn('name', response['agent'])
        self.assertEqual(response['agent']['model'], self.agent['model'])
        self.assertEqual(response['agent']['goals'], self.agent['goals'])

    def test_create_agent_without_model(self):
        self.agent.pop('model')
        response = createAgent(self.user, self.agent)
        self.assertEqual(response['message'], 'AGENT_CREATED')
        self.assertEqual(response['agent']['name'], self.agent['name'])
        self.assertNotIn('model', response['agent'])
        self.assertEqual(response['agent']['goals'], self.agent['goals'])

if __name__ == '__main__':
    unittest.main()
```