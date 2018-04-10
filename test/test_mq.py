from manta import MessageQueue as MQ
import unittest, time

var = 0
var1 = 0

def ch_var(arg):
    global var
    var = arg

def ch_var1(arg):
    global var1
    var1 = arg


def reset_var():
    global var
    var = 0

class TestMQ(unittest.TestCase):
    def test_channel(self):
        chan1 = MQ.declare_channel("test_ch")
        chan1.comsume(ch_var)
        chan2 = MQ.declare_channel("test_ch")
        chan2.publish(2)
        MQ.start(_test_timeout=0.1, force=True)
        self.assertEqual(var, 2)

        reset_var()
        chan3 = MQ.declare_channel("test_ch1")
        chan3.publish(3)
        MQ.start(_test_timeout=0.1, force=True)
        self.assertNotEqual(var, 3)
        reset_var()

    def test_exchange(self):
        ex = MQ.declare_exchange("test_ex")
        chan1 = MQ.declare_channel("test_ch2", ex)
        chan1.comsume(ch_var)
        chan2 = MQ.declare_channel("test_ch3", ex)
        chan2.comsume(ch_var1)

        ex1 = MQ.declare_exchange("test_ex")
        ex1.publish(2)
        MQ.start(_test_timeout=0.1, force=True)
        self.assertEqual(var, 2)
        self.assertEqual(var1, 2)
        reset_var()

        ex1 = MQ.declare_exchange("test_ex1")
        ex1.publish(3)
        MQ.start(_test_timeout=0.1, force=True)
        self.assertNotEqual(var, 3)
        self.assertNotEqual(var1, 3)
    