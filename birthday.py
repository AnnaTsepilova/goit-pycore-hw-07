from datetime import datetime
from field import Field

class Birthday(Field):
    _dateFormat = "%d.%m.%Y"

    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, self._dateFormat)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime(self._dateFormat)

    @staticmethod
    def format():
        return Birthday._dateFormat
