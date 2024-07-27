import re
from field import Field

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate(number)

    def validate(self, number):
        ''' Simple phone number validation '''
        if not re.match(r"^\+?(\d{10})$", number.strip()):
            raise ValueError("Phone number should contain 10 digits")

        return number
