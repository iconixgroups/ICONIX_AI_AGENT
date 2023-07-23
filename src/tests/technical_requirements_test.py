import unittest
from src.technical_requirements import FrontEnd, BackEnd, Database, Hosting, Pipeline, Testing

class TestTechnicalRequirements(unittest.TestCase):

    def setUp(self):
        self.front_end = FrontEnd()
        self.back_end = BackEnd()
        self.database = Database()
        self.hosting = Hosting()
        self.pipeline = Pipeline()
        self.testing = Testing()

    def test_front_end(self):
        self.assertIn(self.front_end.get_framework(), ['React', 'Angular'])

    def test_back_end(self):
        self.assertEqual(self.back_end.get_language(), 'Node.js')

    def test_database(self):
        self.assertEqual(self.database.get_db(), 'MongoDB')

    def test_hosting(self):
        self.assertIn(self.hosting.get_provider(), ['AWS', 'GCP', 'Azure', 'SmarterASP.Net'])

    def test_pipeline(self):
        self.assertTrue(self.pipeline.is_ci_cd_enabled())

    def test_testing(self):
        self.assertTrue(self.testing.has_unit_tests())
        self.assertTrue(self.testing.has_integration_tests())

if __name__ == '__main__':
    unittest.main()
