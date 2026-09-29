from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def to_money(value) -> Decimal:
    """Convert a number or numeric string to a Decimal rounded to cents (half up)."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


def allocate(total, parts: int) -> list[Decimal]:
    """Split `total` into `parts` amounts, e.g. to share one invoice between co-payers."""
    if parts <= 0:
        raise ValueError("parts must be positive")
    total = to_money(total)
    cents = int(total / CENT)
    base, extra = divmod(cents, parts)
    # Leftover cents go to the first parts, so no two parts differ by more than a cent.
    return [(base + (1 if i < extra else 0)) * CENT for i in range(parts)]
