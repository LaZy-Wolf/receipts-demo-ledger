from decimal import Decimal as D

from ledger import load_lines


def test_basic_csv():
    lines = load_lines("description,quantity,unit_price\nWidget,2,9.99\nGadget,1,20\n")
    assert [line.description for line in lines] == ["Widget", "Gadget"]
    assert lines[0].quantity == 2
    assert lines[0].unit_price == D("9.99")


def test_optional_columns_default_to_zero():
    (line,) = load_lines("description,quantity,unit_price\nWidget,1,5.00")
    assert line.tax_rate == D("0")
    assert line.discount == D("0")


def test_optional_columns_read():
    (line,) = load_lines("description,quantity,unit_price,tax_rate,discount\nWidget,1,5.00,0.2,1.00")
    assert line.tax_rate == D("0.2")
    assert line.discount == D("1.00")
