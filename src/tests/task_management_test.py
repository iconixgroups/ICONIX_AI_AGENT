```python
import unittest
from src.task_management import Task, submitTask, viewTasks

class TestTaskManagement(unittest.TestCase):

    def setUp(self):
        self.task = Task("Test Task", "Test Goal", "Test Agent")

    def test_task_creation(self):
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.goal, "Test Goal")
        self.assertEqual(self.task.agent, "Test Agent")

    def test_submit_task(self):
        response = submitTask(self.task)
        self.assertEqual(response, "TASK_SUBMITTED")

    def test_view_tasks(self):
        submitTask(self.task)
        tasks = viewTasks()
        self.assertIn(self.task, tasks)

if __name__ == '__main__':
    unittest.main()
```