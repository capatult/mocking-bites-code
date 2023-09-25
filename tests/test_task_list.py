from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False


def test_add_one_item():
    task_list = TaskList()
    mock_task = Mock()
    task_list.add(mock_task)
    assert task_list.tasks == [mock_task]

def test_add_two_items():
    task_list = TaskList()
    mock_task01 = Mock()
    mock_task02 = Mock()
    task_list.add(mock_task01)
    task_list.add(mock_task02)
    assert task_list.tasks == [mock_task01, mock_task02]
    
def test_all():
    task_list = TaskList()
    mock_task = Mock()
    task_list.add(mock_task)
    assert task_list.tasks == task_list.all()

def test_tasks_incomplete_after_one_added():
    task_list = TaskList()
    mock_task = Mock()
    mock_task.is_complete.return_value = False
    task_list.add(mock_task)
    assert task_list.all_complete() == False


def test_tasks_complete_after_one_complete_added():
    task_list = TaskList()
    mock_task = Mock()
    mock_task.is_complete.return_value = True
    task_list.add(mock_task)
    assert task_list.all_complete() == True

def test_task_complete_and_incomplete_added():
    task_list = TaskList()
    mock_task = Mock()
    mock_task.is_complete.return_value = True
    task_list.add(mock_task)
    mock_task01 = Mock()
    mock_task01.is_complete.return_value = False
    task_list.add(mock_task01)
    assert task_list.all_complete() == False


# Unit test `#tasks` and `#all_complete` behaviour



# class TaskList:
#     def __init__(self):
#         self.tasks = []

#     def add(self, task):
#         self.tasks.append(task)

#     def all(self):
#         return self.tasks

#     def all_complete(self):
#         if len(self.tasks) == 0:
#             return False
#         return all([task.is_complete() for task in self.tasks])
    