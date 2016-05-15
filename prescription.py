import re
from functools import total_ordering

RE_HAS_DIGIT = re.compile('\d+')


@total_ordering
class Prescription:
    def __init__(self, drug, amount, unit, frequency):
        self.drug = drug
        self.amount = amount
        self.unit = unit
        self.frequency = frequency

    def __str__(self):
        return "{}{} of {} for {}".format(self.amount, self.unit, self.drug,
                                          self.frequency)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        if self.unit != other.unit:
            raise ValueError("Units not equivalent.")
        return self.amount < other.amount


def is_quantity(word):
    return RE_HAS_DIGIT.match(word)
