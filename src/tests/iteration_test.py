import unittest
from iteration import retrainAgent, receiveFeedback

class TestIteration(unittest.TestCase):

    def setUp(self):
        self.user = User("test_user")
        self.agent = Agent("test_agent", self.user)
        self.task = Task("test_task", self.agent)
        self.result = Result("test_result", self.task)

    def test_retrainAgent(self):
        retrainAgent(self.agent)
        self.assertEqual(self.agent.status, "retrained")

    def test_receiveFeedback(self):
        feedback = "The agent needs to improve its response time."
        receiveFeedback(self.user, self.agent, feedback)
        self.assertIn(feedback, self.agent.feedback)

if __name__ == '__main__':
    unittest.main()
