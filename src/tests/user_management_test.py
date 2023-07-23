import unittest
from src.user_management import User, createUser, loginUser

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        self.user = User("testUser", "testPassword")

    def test_createUser(self):
        response = createUser(self.user)
        self.assertEqual(response, "SIGNUP_SUCCESS")

    def test_loginUser(self):
        response = loginUser(self.user)
        self.assertEqual(response, "LOGIN_SUCCESS")

if __name__ == '__main__':
    unittest.main()
