class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def all(self):
        return self.tasks

    def all_complete(self):
        if len(self.tasks) == 0:
            return False
        return all([task.is_complete() for task in self.tasks])
    





# def test_task_list_initially_empty():
#     task_list = TaskList()
#     assert task_list.tasks == []


# def test_tasks_initially_not_all_complete():
#     task_list = TaskList()
#     assert task_list.all_complete() == False