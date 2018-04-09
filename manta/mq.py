from manta.loop import Loop
from random import choices

def gen_name(size=10):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(choices(string, k = size))

class Channel(object):
    def __init__(self, name="", exchange=None):
        self.name = name or gen_name()
        self._exchange = exchange
        self._body = None
        self._func = None

    def set_exchange(self, exchange):
        self._exchange = exchange

    def comsume(self, func):
        self._func = func

    def publish(self, body):
        self._body = body
        Loop.call(self._comsume)

    def _comsume(self):
        if self._func and self._body:
            self._func(self._body)

class Exchange(object):
    def __init__(self, name=""):
        self.name = name or gen_name()
        self._channels = []
        self._body = None

    def bind(self, chan):
        chan.set_exchange(self)
        self._channels.append(chan)

    def publish(self, body):
        self._body = body
        Loop.call(self._comsume)

    def _comsume(self):
        if self._body and self._channels:
        for chan in self._channels:
            chan.publish(self._body)


class MessageQueue(object):
    _CHANNELS = {}
    _EXCHANGES = {}

    @classmethod
    def get_channel(cls, name):
        return cls._CHANNELS.get(name)

    @classmethod
    def get_exchange(cls, name):
        return cls._EXCHANGES.get(name)

    @classmethod
    def declare_channel(cls, name="", exchange=None):
        chan = cls._CHANNELS.get(name)
        if not chan:
            chan = Channel(name)
            cls._CHANNELS[name] = chan
            exchange.bind(chan)
        return chan

    @classmethod
    def declare_exchange(cls, name=""):
        exch = cls._EXCHANGES.get(name)
        if not exch:
            exch = Exchange(name)
            cls._EXCHANGES[name] = exch
        return exch

    @classmethod
    def start(cls, thread_size=1, task_queue_size=0):
        Loop.start(thread_size = thread_size, 
                   task_queue_size= task_queue_size)
