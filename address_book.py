from datetime import datetime
from datetime import timedelta
from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record):
        '''Function add record to address book'''
        if self.data.get(record.name.value):
            print("Record already exist")
            return False

        self.data[record.name.value] = record
        return True

    def find(self, name: str) -> Record | None:
        '''Function add record to address book'''
        result = self.data.get(name)
        if result:
            return result

        return None

    def delete(self, name: str) -> bool:
        '''Find and remove record'''
        record = self.find(name)
        if not record:
            return False

        del self.data[name]
        return True

    def get_upcoming_birthdays(self) -> list:
        """
        Function return upcomming birthdays.
        """
        birthdays = []

        today = datetime.today().date()

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value.date()

            specific_date = datetime(year=today.year, month=birthday.month, day=birthday.day).date()

            ## Birthday next 7 days
            if (specific_date - today).days <= 7 and (specific_date - today).days >= 0:
                weekend_correction = 0
                if specific_date.isoweekday() > 5:
                    weekend_correction = 7 - specific_date.isoweekday() + 1

                congratulation_date = specific_date + timedelta(days=weekend_correction)
                birthdays.append(
                    {
                        'name': record.name.value,
                        'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
                    }
                )

        return birthdays
