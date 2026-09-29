from datetime import date
from decimal import Decimal

from .money import to_money


def add_months(d: date, months: int) -> date:
    """Return the same day-of-month `months` later."""
    m = d.month - 1 + months
    return d.replace(year=d.year + m // 12, month=m % 12 + 1)


def billing_periods(start: date, end: date, months: int = 1) -> list[tuple[date, date]]:
    """Split [start, end) into consecutive billing periods of `months` months.

    Each period is (period_start, period_end) with period_end exclusive. Periods are
    anchored to `start`, so a subscription that begins on the 15th renews on the 15th.
    The last period is cut short at `end`.
    """
    periods = []
    current = start
    i = 0
    while current < end:
        i += 1
        nxt = min(add_months(start, i * months), end)
        periods.append((current, nxt))
        current = nxt
    return periods


def prorate(amount, period: tuple[date, date], used_days: int) -> Decimal:
    """Charge for `used_days` of a period whose full price is `amount`."""
    days = (period[1] - period[0]).days
    return to_money(Decimal(str(amount)) * used_days / days)
