from threading import Thread, Lock, Event
from manta.driver.worker import Worker

class WorkingTread(Thread):
    def __init__(self, queue, lock, name, release):
        Thread.__init__(self)
        self._queue = queue
        self._lock  = lock
        self._name  = name
        self._release = release
        self._worker = Worker(self._queue, self._lock, self._name, self._release)
        self.setName(name)

    def run(self):
        self._worker.start()

class ThreadPool(object):
    def __init__(self, size, queue):
        self._size = size
        self._queue = queue
        self._lock = Lock()
        self._release = Event()
        self._threadpool = []
        self._join = False

    def _init_tp(self):
        for i in range(self._size):
            name = "manta_worker_{0}".format(i)
            worker = WorkingTread(self._queue, self._lock, name, self._release)
            self._threadpool.append(worker)

    def start(self):
        self._init_tp()
        for thread in self._threadpool:
            thread.start()

    def join(self):
        if not self._join:
            for thread in self._threadpool:
                thread.join()
                del thread
            self._join = True

    def release(self):
        self._release.set()
        self.join()