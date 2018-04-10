from manta.driver.threadpool import ThreadPool
from manta.exp import LoopNotInstanlizeExp, InvalidArgExp, LoopNotInitExp
from manta.task import Task
from queue import PriorityQueue
from threading import Timer

class Loop(object):
    _INSTANCE        = None
    _TASK_QUEUE      = PriorityQueue()
    _THREAD_SIZE     = 1
    _THREAD_POOL     = None
    _STARTED         = False
    _INITIALIZE      = False

    @classmethod
    def _initialize(cls, force=False):
        if cls._THREAD_POOL is None or force:
            cls._THREAD_POOL = ThreadPool(cls._THREAD_SIZE, cls._TASK_QUEUE)

    @classmethod
    def _new_task(cls, func, *args, **kwargs):
        return Task(func, *args, **kwargs)

    @classmethod
    def _new_period_task(cls, func, interval, *args, **kwargs):
        return cls._new_task(func, interval = interval, *args, **kwargs)

    @classmethod
    def _new_timeout_task(cls, func, timeout, *args, **kwargs):
        return cls._new_task(func, timeout = timeout, *args, **kwargs)

    @classmethod
    def periodic_call(cls, func, interval, *args, **kwargs):
        task = cls._new_period_task(func, interval, *args, **kwargs)
        cls.add_task(task)

    @classmethod
    def timeout_call(cls, func, timeout, *args, **kwargs):
        task = cls._new_timeout_task(func, timeout, *args, **kwargs)
        cls.add_task(task)
    
    @classmethod
    def call(cls, func, *args, **kwargs):
        task = cls._new_task(func, *args, **kwargs)
        cls.add_task(task)
    
    @classmethod
    def add_task(cls, task):
        cls._TASK_QUEUE.put(task)

    @classmethod
    def initialize(cls, thread_size=1, force=False):
        if not cls._INITIALIZE or force:
            cls._THREAD_SIZE = thread_size
            cls._initialize(force=True)
            cls._INITIALIZE = True

    @classmethod
    def start(cls, thread_size=1, force=False, _test_timeout=0):
        if not cls._STARTED or force:
            cls.initialize(thread_size, force)
            cls._THREAD_POOL.start()
            if _test_timeout:
                import time
                time.sleep(_test_timeout)
                cls._THREAD_POOL.release()
            cls._STARTED=True
            cls._THREAD_POOL.join()
