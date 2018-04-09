from manta.driver.threadpool import ThreadPool
from manta.exp import LoopNotInstanlizeExp, InvalidArgExp
from manta.task import Task
from queue import PriorityQueue
from threading import Timer

class Loop(object):
    _INSTANCE        = None
    _TASK_QUEUE      = None
    _TASK_QUEUE_SIZE = 0
    _THREAD_SIZE     = 1
    _LOCK            = threading.Lock()
    _THREAD_POOL     = None
    _STARTED         = False

    @classmethod
    def _initialize(cls):
        if cls._INSTANCE is None: raise LoopNotInstanlizeExp
        if cls._TASK_QUEUE is None:
            cls._TASK_QUEUE = PriorityQueue(cls._TASK_QUEUE_SIZE)
        if cls._THREAD_POOL is None:
            cls._THREAD_POOL = ThreadPool(cls._THREAD_SIZE)

    @classmethod
    def _new_task(cls, func, timeout=0, interval=0, *args, **kwargs):
        return Task(func, timeout, interval, *args, **kwargs))

    @classmethod
    def _new_period_task(cls, func, interval, *args, **kwargs):
        return cls._new_task(func, 0, interval, *args, **kwargs)

    @classmethod
    def _new_timeout_task(cls, func, timeout, *args, **kwargs):
        return cls._new_task(func, timeout, 0, *args, **kwargs)

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
        cls.add_task(tash)
    
    @classmethod
    def add_task(cls, task):
        cls._TASK_QUEUE.put(task)

    @classmethod
    def add_task(cls, task):
        cls._TASK_QUEUE.put(task)

    @classmethod
    def start(cls, thread_size=1, task_queue_size=0):
        if not cls._STARTED:
            cls._TASK_QUEUE_SIZE = queue_size
            cls._THREAD_SIZE = thread_size
            cls._initialize()
            cls._THREAD_POOL.start()
            cls._THREAD_POOL.join()
            cls._TASK_QUEUE.join()
