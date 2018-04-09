import time

class Task(object):
    """
    Priority of the task:normal_task > timeout_task > period_task
    """
    def __init__(self, func, timeout=0, interval=0, *args, **kwargs):
        self.timeout = timeout
        self._interval = interval
        self._func = func
        self._callback = kwargs.pop("callback")
        self._args = args
        self._kwargs = kwargs
        self._run_time_ = 0 
        self._time_updated = False
        self.update_time()

    def update_time(self):
        if not self._time_updated or self.is_period:
            if self.is_period and not self.timeout:
                self.timeout = self._interval
            if not self.is_normal:
                self._run_time = self.timeout + time.time()
            self._time_updated = True

    @property
    def is_timeout(self):
        return not self.timeout is 0

    @property
    def is_period(self):
        return not self._interval is 0

    @property
    def is_normal(self):
        return not self.is_period or not self.is_timeout

    def _cmp(self, other):
        if self.is_period:
            if other.is_period: return 0
            else:                 return -1
        elif self.is_timeout:
            if other.is_period:  return 1
            elif other.is_timeout: return 0
            else:                  return -1
        else:
            if other.is_period or other.is_timeout:
                return 1
            else:
                return 0
    
    def __lt__(self, other):
        return self._cmp(other) is 1

    def __gt__(self, other):
        return not self.__lt__(other)

    @property
    def runable(self):
        if self.is_normal:
            return True
        else:
            now = time.time()
            return now >= self._run_time

    def do(self):
        res = self._func(*self._args, **self._kwargs)
        if self._callback is not None:
            return self._callback(res)
        else:
            return res