import unittest, os
from manta.utils import run_dir

var = 1
def test_rundir():
    global var
    var += 1

class TestUtils(unittest.TestCase):
    def test_run_dir(self):
        run_dir(os.path.dirname(__file__), "test_rundir")
        self.assertNotEqual(var, 1)

