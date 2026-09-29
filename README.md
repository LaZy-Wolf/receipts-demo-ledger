# ledger

Invoice maths for small billing systems. Standard library only, Python 3.10+.

- `to_money`, `allocate`: cent rounding and splitting an amount between payers
- `Line`, `Invoice`: per-line discount and tax, invoice totals
- `add_months`, `billing_periods`, `prorate`: subscription periods
- `load_lines`: import invoice lines from CSV

```python
from decimal import Decimal as D
from ledger import Invoice, Line

inv = Invoice([Line("Widget", 2, D("10.00"), tax_rate=D("0.20"))])
inv.total()  # Decimal('24.00')
```

## Development

```bash
pip install -e ".[test]"
pytest
```
