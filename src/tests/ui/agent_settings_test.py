import unittest
from src.ui.agent_settings import AgentSettings

class TestAgentSettings(unittest.TestCase):

    def setUp(self):
        self.agent_settings = AgentSettings()

    def test_update_agent_settings(self):
        self.agent_settings.updateAgentSettings('Test Agent', 'avatar1', 'This is a test agent')
        self.assertEqual(self.agent_settings.agentName, 'Test Agent')
        self.assertEqual(self.agent_settings.agentAvatar, 'avatar1')
        self.assertEqual(self.agent_settings.agentDescription, 'This is a test agent')

    def test_backup_agent(self):
        self.assertTrue(self.agent_settings.backupAgent())

    def test_add_collaborator(self):
        self.agent_settings.addCollaborator('testUser')
        self.assertIn('testUser', self.agent_settings.collaborators)

    def test_version_agent(self):
        self.agent_settings.versionAgent('1.0.0')
        self.assertEqual(self.agent_settings.version, '1.0.0')

    def test_deploy_agent(self):
        self.assertTrue(self.agent_settings.deployAgent('website'))

if __name__ == '__main__':
    unittest.main()
