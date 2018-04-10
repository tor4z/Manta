from manta.loop import Loop
from random import choices

def gen_name(size=10):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(choices(string, k = size))

class Channel(object):
    def __init__(self, name="", exchange=None):
        self.name = name or gen_name()
        self._exchange = exchange
        self._func = None

    def set_exchange(self, exchange):
        self._exchange = exchange

    def comsume(self, func):
        self._func = func

    def publish(self, body):
        self._exchange.publish(body)

    def execute(self, body):
        if self._func:
            self._func(body)

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
        Loop.call(self.execute)

    def execute(self):
        for chan in self._channels:
            chan.execute(self._body)


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
            if exchange is None: 
                exchange = Exchange()    
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
    def start(cls, thread_size=1, force=True, _test_timeout=0):
        Loop.start(thread_size = thread_size, 
                    _test_timeout = _test_timeout, force=force)
