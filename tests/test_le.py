from liquid_engine import LiquidEngine


class MyLE(LiquidEngine):
    def __init__(self):
        self._designation = "MyLE"
        super().__init__()

    def run(self):
        return self._run()

    def _run_a(self):
        return 1.23

    def _run_b(self):
        return 4.56


def test_myle():
    le = MyLE()
    le.run()
    le.benchmark()
    le.run()