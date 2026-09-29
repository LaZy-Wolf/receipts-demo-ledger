from decimal import Decimal

from .invoice import Line


def load_lines(text: str) -> list[Line]:
    """Parse invoice lines from CSV text.

    The first row is a header with at least description, quantity and unit_price.
    Optional columns: tax_rate, discount.
    """
    rows = [row.split(",") for row in text.strip().splitlines()]
    header = [h.strip() for h in rows[0]]
    lines = []
    for row in rows[1:]:
        rec = dict(zip(header, (cell.strip() for cell in row)))
        lines.append(Line(
            description=rec["description"],
            quantity=int(rec["quantity"]),
            unit_price=Decimal(rec["unit_price"]),
            tax_rate=Decimal(rec.get("tax_rate") or "0"),
            discount=Decimal(rec.get("discount") or "0"),
        ))
    return lines
