import time
from liquid_engine import LiquidEngine


class MyLE(LiquidEngine):
    def __init__(self, *args, **kwargs):
        self._designation = "MyLE"
        super().__init__(*args, **kwargs)

    def run(self, var, run_type=None):
        return self._run(var, run_type=run_type)

    def _run_a(self, var):
        time.sleep(0.1)
        return 1.23

    def _run_b(self, var):
        time.sleep(1)
        return 1.23

    def _run_c(self, var):
        return asdas  #forcing an error to be handled by the LE

    def _compare_runs(self, a, b):
        return a == b


def test_myle():
    le = MyLE(testing=False)
    le.benchmark("var_2")
    le.benchmark("var_2")
    le.benchmark("var_2")
    le.run("var_2", run_type="c")
    le.run("var_2")


def test_myle_testing():
    le = MyLE(testing=True)
    le.benchmark("var_2")
    le.benchmark("var_2")
    le.benchmark("var_2")
    le.run("var_2", run_type="c")
    le.run("var_2")
