from birthday import Birthday
from phone import Phone
from name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, number) -> None:
        '''Function add phone number to record'''
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        '''Function removes phone number from record'''
        for i, phone in enumerate(self.phones):
            if str(phone) == str(number):
                del self.phones[i]
                return True

        return False

    def edit_phone(self, old_number, new_number):
        '''Function change phone number in record'''
        for i, phone in enumerate(self.phones):
            if str(phone) == str(old_number):
                self.phones[i] = Phone(new_number)
                return True
        raise ValueError(f"Phone number {old_number} not found.")

    def find_phone(self, number):
        '''Search phone in record'''
        result = [n.value for n in self.phones if number == n.value]
        if result:
            return result[0]

        return False

    def add_birthday(self, birthday):
        '''Add birthdate to record'''
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
