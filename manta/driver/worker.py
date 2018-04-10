from queue import Empty

class Worker(object):
    def __init__(self, queue, lock, name, event, timeout=0.05):
        self._lock = lock
        self._queue = queue
        self._name  = name
        self._release = event
        self._timeout = timeout

    def _get_task(self, block=True):
        self._lock.acquire()
        try:
            task = self._queue.get(block, self._timeout)
        except Empty:
            task = None
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
        while not self._release.is_set():
            task = self._get_task(block = True)
            if task is not None:
                if self._runable(task):
                    task.do()
                    if task.is_period:
                        self._put_back_period(task)
                else:
                    self._put_back(task)
                self._task_done(task)
