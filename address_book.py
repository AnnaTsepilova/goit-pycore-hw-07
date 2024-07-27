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
        print("Record not found")
        return None

    def delete(self, name: str) -> bool:
        '''Find and remove record'''
        record = self.find(name)
        if not record:
            return False

        del self.data[name]
        return True
