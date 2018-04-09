import unittest
from queue import Queue
from manta import Task
from manta.driver.threadpool import ThreadPool

var = 1
def func():
    global var
    var = 2

class TestThreadPool(unittest.TestCase):
    def test_worker_thread(self):
        q = Queue()
        tp = ThreadPool(10, q)
        task = Task(func)
        q.put(task)
        tp.start()
        self.assertNotEqual(var, 1)
        tp.release()