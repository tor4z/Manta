class Worker(object):
    def __init__(self, queue, lock, name):
        self._lock = lock
        self._queue = queue
        self._name  = name

    def _get_task(self):
        self._lock.acquire(*args, **kwargs)
        task = self._queue.get(*args, **kwargs)
        self._lock.release()
        return task

    def _put_task(self, task, *args, **kwargs):
        self._lock.acquire()
        task = self._queue.put(task, *args, **kwargs)
        self._lock.release()

    def _put_back(self, task):
        self._put_task(task)

    def _put_back_period(self, task):
        if task.is_period:
            task.update_time()
            self._put_back(task)

    def _task_done(self, task):
        self._queue.task_done()

    def _runable(self, task):
        return task.runable

    def start(self):
        task = self._get_task(block = True)
        if self._runable(task):
            task.do()
            if task.is_period:
                self._put_back_period(task)
        else:
            self._put_back(task)
        self._task_done(task)
