from threading import Thread, Lock
from manta.driver.worker import Worker

class WorkingTread(Thread):
    def __init__(self, queue, lock, name):
        Thread.__init__(self)
        self._queue = queue
        self._lock  = lock
        self._name  = name
        self._worker = Worker(self._queue, self._lock, self._name)

    def run(self):
        self._worker.start()

class ThreadPool(object):
    def __init__(self, size, queue):
        self._size = size
        self._nloops = range(self._size)
        self._queue = queue
        self._lock = Lock()
        self._threadpool = []

    def _init_tp(self):
        for i in self._nloops:
            name = "manta_worker_{0}".format(i)
            worker = WorkingTread(self._queue, self._lock, name)
            self._threadpool.append(worker)

    def start(self):
        for i in self._nloops:
            self._threadpool[1].start()

    def join(self):
        for i in self._nloops:
            self._threadpool[1].join()