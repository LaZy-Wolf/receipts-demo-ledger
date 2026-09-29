from decimal import Decimal as D

from ledger import Invoice, Line


def test_single_line_with_tax():
    inv = Invoice([Line("Widget", 2, D("10.00"), tax_rate=D("0.20"))])
    assert inv.subtotal() == D("20.00")
    assert inv.tax() == D("4.00")
    assert inv.total() == D("24.00")


def test_mixed_tax_rates():
    inv = Invoice([
        Line("Book", 1, D("12.00"), tax_rate=D("0")),
        Line("Pen", 3, D("1.50"), tax_rate=D("0.20")),
    ])
    assert inv.tax() == D("0.90")
    assert inv.total() == D("17.40")


def test_discount_reduces_net():
    line = Line("Service", 1, D("100.00"), discount=D("15.00"))
    assert line.net == D("85.00")
    assert Invoice([line]).total() == D("85.00")


def test_empty_invoice():
    assert Invoice().total() == D("0.00")
