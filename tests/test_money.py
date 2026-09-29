from decimal import Decimal

import pytest

from ledger import allocate, to_money


def test_to_money_rounds_half_up():
    assert to_money("2.675") == Decimal("2.68")


def test_to_money_from_int():
    assert to_money(5) == Decimal("5.00")


def test_allocate_even():
    assert allocate(Decimal("10.00"), 2) == [Decimal("5.00"), Decimal("5.00")]


def test_allocate_even_three():
    assert allocate(Decimal("9.00"), 3) == [Decimal("3.00")] * 3


def test_allocate_zero():
    assert allocate(0, 4) == [Decimal("0.00")] * 4


def test_allocate_rejects_zero_parts():
    with pytest.raises(ValueError):
        allocate(10, 0)
