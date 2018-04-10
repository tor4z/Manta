from manta import Loop
import unittest, time

var = 1

def func():
    global var
    var += 1

def reset_var():
    global var
    var = 1

class TestLoop(unittest.TestCase):
    def test_call(self):
        #Loop.initialize(force=True)
        Loop.call(func)
        Loop.start(_test_timeout=0.1, force=True)
        self.assertNotEqual(var, 1)
        reset_var()

    def test_timeout_call(self):
        #Loop.initialize(force=True)
        Loop.timeout_call(func, timeout=0.05)
        Loop.start(_test_timeout=0.1, force=True)
        self.assertNotEqual(var, 1)
        reset_var()

    def test_period_call(self):
        #Loop.initialize(force=True)
        Loop.periodic_call(func, interval=0.05)
        Loop.start(_test_timeout=0.1, force=True)
        self.assertEqual(var, 3)
        reset_var()
