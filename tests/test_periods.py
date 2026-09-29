from datetime import date
from decimal import Decimal

from ledger import add_months, billing_periods, prorate


def test_add_months_simple():
    assert add_months(date(2026, 1, 15), 1) == date(2026, 2, 15)


def test_add_months_across_year():
    assert add_months(date(2026, 11, 10), 3) == date(2027, 2, 10)


def test_monthly_periods():
    assert billing_periods(date(2026, 1, 15), date(2026, 4, 15)) == [
        (date(2026, 1, 15), date(2026, 2, 15)),
        (date(2026, 2, 15), date(2026, 3, 15)),
        (date(2026, 3, 15), date(2026, 4, 15)),
    ]


def test_quarterly_periods_last_one_cut_short():
    assert billing_periods(date(2026, 1, 1), date(2026, 8, 1), months=3) == [
        (date(2026, 1, 1), date(2026, 4, 1)),
        (date(2026, 4, 1), date(2026, 7, 1)),
        (date(2026, 7, 1), date(2026, 8, 1)),
    ]


def test_prorate_half_period():
    period = (date(2026, 4, 1), date(2026, 5, 1))
    assert prorate(Decimal("30.00"), period, 15) == Decimal("15.00")
