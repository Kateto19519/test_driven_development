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
