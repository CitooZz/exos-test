from decimal import Decimal
from xlwt import XFStyle
import random


def get_random_number():
    return random.choice(range(1, 101))


class ExcelWriter(object):

    def __init__(self, sheet):
        self.sheet = sheet
        self._row = 0

    def writerow(self, row):
        for cell, data in enumerate(row):
            if data is None:
                data = ''

            elif not isinstance(data, (int, float, Decimal)):
                data = unicode(data)

            style = XFStyle()
            style.alignment.wrap = 1
            self.sheet.write(self._row, cell, data, style)

        self._row += 1
