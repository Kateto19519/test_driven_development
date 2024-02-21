# test_integration.py
import unittest
from to_do import TodoList

class TestIntegration(unittest.TestCase):
    def test_todo_list_integration(self):
        # Simulate interaction between modules
        todo_list = TodoList()

        todo_list.add_task({'description': 'Do laundry', 'completed': False})
        self.assertEqual(len(todo_list.get_tasks()), 1)

        todo_list.add_task({'description': 'Buy groceries', 'completed': False})
        self.assertEqual(len(todo_list.get_tasks()), 2)

        todo_list.mark_task_completed(0)
        self.assertTrue(todo_list.get_tasks()[0]['completed'])

if __name__ == '__main__':
    unittest.main()
