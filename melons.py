"""Classes for melon orders."""

from random import randint
from datetime import datetime, date

# create Abstract class


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax=0):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.datetime = datetime.today()

    def get_base_price(self):

        base_price = randint(5, 10)
        weekday = date.weekday(self.datetime)
        hour_day = self.datetime.hour
        if (weekday != 5 and weekday != 6) and (hour_day >= 8 and hour_day <= 11):
            base_price = base_price + 4
            import pdb; pdb.set_trace()
        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", .08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code   

    # def __repr__(self):
    #     return f'{self.species}'

    def get_total(self):
        """Calculate price, including tax."""

        total = super().get_total()

        if self.qty < 10:
            total = total + 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ New class for government orders. No tax. New method for inspections."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic")
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
