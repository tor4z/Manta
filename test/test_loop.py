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
        Loop.timeout_call(func, 0.05)
        time.sleep(0.06)
        Loop.start(_test_timeout=0.1, force=True)
        self.assertNotEqual(var, 1)
        reset_var()

    def test_period_call(self):
        #Loop.initialize(force=True)
        Loop.timeout_call(func, 0.05)
        time.sleep(0.1)
        Loop.start(_test_timeout=0.1, force=True)
        self.assertEqual(var, 2)
        reset_var()
