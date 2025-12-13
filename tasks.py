class Tasks:

    def __init__(self):
        self.tasks_list = []

    def create_task(self, task_name):
        self.tasks_list.append(task_name)

    def delete_task(self, task_name):
        for task in self.tasks_list:
            if task_name == task:
                self.tasks_list.remove(task)

    def delete_all_task(self):
        self.tasks_list.clear()


if __name__ == '__main__':
    t1 = Tasks()
    t1.create_task("apprendre le latin")
    t1.create_task("sport")
    t1.create_task("faire le menage")
    print(t1.tasks_list)
    t1.delete_task("sport")
    t1.delete_all_task()
    print(t1.tasks_list)
