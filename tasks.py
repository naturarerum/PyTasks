

class Tasks:

    def __init__(self, task_name):
        self.task_name = task_name
        self.tasks_list = []

    def create_task(self):
        self.tasks_list.append(self.task_name)

    def delete_task(self):
        pass
    