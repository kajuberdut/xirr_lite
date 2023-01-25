from datetime import datetime
from unittest import TestCase, main

from xirr_lite import xirr
from xirr_lite.main import secant_method, newton


def mdt(d: str) -> datetime:
    "makes an iso string into a datetime"
    return datetime.fromisoformat(d)


class TestCaseless(TestCase):
    @property
    def cashflow(self):
        return [
            (mdt("2020-01-01"), -5000),
            (mdt("2020-04-07"), 500),
            (mdt("2020-08-05"), 500),
            (mdt("2020-09-01"), 500),
            (mdt("2020-12-01"), 1000),
            (mdt("2021-01-02"), 1000),
            (mdt("2021-04-05"), 1000),
            (mdt("2021-08-09"), 1500),
        ]

    def test_basic(self):
        result = xirr(cashflows=self.cashflow, guess=0.1, condenser=secant_method)
        self.assertAlmostEqual(result, 0.1906935199)

    def test_newton(self):
        result = xirr(cashflows=self.cashflow, guess=0.1, condenser=newton)
        self.assertAlmostEqual(result, 0.1906935199)


if __name__ == "__main__":
    main()  # pragma: no cover
