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
        self._nloops = range(self._size)
        self._queue = queue
        self._lock = Lock()
        self._release = Event()
        self._threadpool = []
        self._join = False

    def _init_tp(self):
        for i in self._nloops:
            name = "manta_worker_{0}".format(i)
            worker = WorkingTread(self._queue, self._lock, name, self._release)
            self._threadpool.append(worker)

    def start(self):
        self._init_tp()
        for i in self._nloops:
            self._threadpool[i].start()

    def join(self):
        if not self._join:
            for i in self._nloops:
                self._threadpool[i].join()
            self._join = True

    def release(self):
        self._release.set()
        self.join()