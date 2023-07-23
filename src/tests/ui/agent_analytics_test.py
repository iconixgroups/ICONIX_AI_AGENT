import unittest
from src.ui.agent_analytics import AgentAnalytics

class TestAgentAnalytics(unittest.TestCase):

    def setUp(self):
        self.analytics = AgentAnalytics()

    def test_evaluateAgentPerformance(self):
        self.analytics.evaluateAgentPerformance()
        self.assertTrue(self.analytics.performance_evaluated)

    def test_receiveFeedback(self):
        feedback = "The agent is very helpful."
        self.analytics.receiveFeedback(feedback)
        self.assertEqual(self.analytics.feedback, feedback)

    def test_users(self):
        self.assertEqual(self.analytics.users, 0)
        self.analytics.incrementUsers()
        self.assertEqual(self.analytics.users, 1)

    def test_conversations(self):
        self.assertEqual(self.analytics.conversations, 0)
        self.analytics.incrementConversations()
        self.assertEqual(self.analytics.conversations, 1)

    def test_usageMetrics(self):
        self.assertEqual(self.analytics.usageMetrics, 0)
        self.analytics.incrementUsageMetrics()
        self.assertEqual(self.analytics.usageMetrics, 1)

    def test_sentiment(self):
        sentiment = "Positive"
        self.analytics.updateSentiment(sentiment)
        self.assertEqual(self.analytics.sentiment, sentiment)

    def test_missedQuestions(self):
        self.assertEqual(self.analytics.missedQuestions, 0)
        self.analytics.incrementMissedQuestions()
        self.assertEqual(self.analytics.missedQuestions, 1)

if __name__ == '__main__':
    unittest.main()
