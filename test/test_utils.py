import unittest, os
from manta.utils import run_dir, Log

var = 1
def test_rundir():
    global var
    var += 1

class TestUtils(unittest.TestCase):
    def test_run_dir(self):
        run_dir(os.path.dirname(__file__), "test_rundir")
        self.assertNotEqual(var, 1)

class TestLog(unittest.TestCase):
    def test_log(self):
        print()
        Log.set_level(Log.NOTSET)
        Log.set_name("test")

        Log.info("info msg")
        Log.debug("debug msg")
        Log.warning("warning msg")
        Log.error("error msg")
        Log.fatal("fatal msg")
        Log.critical("critical msg")

