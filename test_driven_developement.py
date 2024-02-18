

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True


import unittest

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task({'description': 'Do laundry', 'completed': False})
        self.assertEqual(len(self.todo_list.get_tasks()), 1)

    def test_get_tasks(self):
        self.todo_list.add_task({'description': 'Do laundry', 'completed': False})
        self.todo_list.add_task({'description': 'Buy groceries', 'completed': False})
        self.assertEqual(len(self.todo_list.get_tasks()), 2)

    def test_mark_task_completed(self):
        self.todo_list.add_task({'description': 'Do laundry', 'completed': False})
        self.todo_list.add_task({'description': 'Buy groceries', 'completed': False})
        self.todo_list.mark_task_completed(0)
        self.assertTrue(self.todo_list.get_tasks()[0]['completed'])

if __name__ == '__main__':
    unittest.main()
