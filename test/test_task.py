import unittest
from manta import Task

def func(a):
    return a

def func_callback(arg):
    return arg

class TestTask(unittest.TestCase):
    def test_task_do(self):
        task = Task(func, 0, 0, 1, callback=func_callback)
        self.assertEqual(task.do(), 1)

    def test_task_lt(self):
        task1 = task = Task(func, 0, 0, 1, callback=func_callback)
        task2 = task = Task(func, 1, 0, 1, callback=func_callback)
        self.assertGreater(task2, task1)

    def test_task_normal(self):
        task = task = Task(func, 0, 0, 1, callback=func_callback)
        self.assertTrue(task.is_normal)

    def test_task_period(self):
        task = task = Task(func, 0, 1, 1, callback=func_callback)
        self.assertTrue(task.is_period)

    def test_task_timeout(self):
        task = task = Task(func, 1, 0, 1, callback=func_callback)
        self.assertTrue(task.is_timeout)

    def test_task_update_time(self):
        import time
        task = task = Task(func, 0, 1, 1, callback=func_callback)
        task.update_time()
        time.sleep(1)
        self.assertTrue(task.runable)
