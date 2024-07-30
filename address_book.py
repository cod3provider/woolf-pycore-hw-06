from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Only Record instances can be added")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, "Contact not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")