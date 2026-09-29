from dataclasses import dataclass, field
from decimal import Decimal

from .money import to_money

ZERO = Decimal("0.00")


@dataclass
class Line:
    description: str
    quantity: int
    unit_price: Decimal
    tax_rate: Decimal = Decimal("0")  # 0.20 means 20%
    discount: Decimal = Decimal("0")  # absolute amount taken off the whole line

    @property
    def net(self) -> Decimal:
        """Line amount after discount, before tax."""
        return to_money(self.quantity * self.unit_price - self.discount)

    @property
    def tax(self) -> Decimal:
        return to_money(self.net * self.tax_rate)


@dataclass
class Invoice:
    lines: list[Line] = field(default_factory=list)

    def subtotal(self) -> Decimal:
        return sum((line.net for line in self.lines), ZERO)

    def tax(self) -> Decimal:
        return sum((line.tax for line in self.lines), ZERO)

    def total(self) -> Decimal:
        return self.subtotal() + self.tax()
