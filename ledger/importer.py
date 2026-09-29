import csv
import io
from decimal import Decimal

from .invoice import Line


def load_lines(text: str) -> list[Line]:
    """Parse invoice lines from CSV text.

    The first row is a header with at least description, quantity and unit_price.
    Optional columns: tax_rate, discount.
    """
    reader = csv.DictReader(io.StringIO(text.strip()), skipinitialspace=True)
    lines = []
    for row in reader:
        rec = {key.strip(): (value or "").strip() for key, value in row.items() if key}
        lines.append(Line(
            description=rec["description"],
            quantity=int(rec["quantity"]),
            unit_price=Decimal(rec["unit_price"]),
            tax_rate=Decimal(rec.get("tax_rate") or "0"),
            discount=Decimal(rec.get("discount") or "0"),
        ))
    return lines
