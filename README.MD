Here is the translation of the provided text into English:

---

Our assistant already knows how to interact with the user via the command line, receiving commands and arguments, and performing the necessary actions. In this task, you will need to work on the internal logic of the assistant, specifically on how data is stored, what data is stored, and what can be done with it.
☝ We will add the actual logic to the bot in the next task assignment.

We will use object-oriented programming for these purposes. First, let's identify several entities (models) that we will work with.
The user will have an address book or contact book. This contact book contains records. Each record contains a set of fields.

Thus, we have described the entities (classes) that need to be implemented. Next, we will look at the requirements for these classes and establish their relationships and the rules by which they will interact.
The user interacts with the contact book by adding, deleting, and editing records. The user should also be able to search the contact book for records by one or more criteria (fields).
It can also be said that fields can be mandatory (name) or optional (phone or email, for example). Records can also contain multiple fields of the same type (e.g., multiple phones). The user should be able to add/remove/edit fields in any record.

### Technical Description of the Task

Develop a system for managing an address book.

#### Entities:
- **Field**: Base class for record fields.
- **Name**: Class for storing the contact's name. Mandatory field.
- **Phone**: Class for storing the phone number. Has format validation (10 digits).
- **Record**: Class for storing contact information, including name and a list of phone numbers.
- **AddressBook**: Class for storing and managing records.

#### Functionality:
- **AddressBook**:
  - Adding records.
  - Searching records by name.
  - Deleting records by name.
- **Record**:
  - Adding phones.
  - Deleting phones.
  - Editing phones.
  - Searching for a phone.

### Recommendations for Implementation

As a starting point, you can use the following base code to implement this task assignment:
```python
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # implementation of the class
    pass

class Phone(Field):
    # implementation of the class
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # implementation of the class

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # implementation of the class
    pass
```

After implementation, your code should execute as follows:
```python
# Creating a new address book
book = AddressBook()

# Creating a record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John's record to the address book
book.add_record(john_record)

# Creating and adding a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Displaying all records in the book
for name, record in book.data.items():
    print(record)

# Finding and editing a phone number for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Searching for a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555

# Deleting Jane's record
book.delete("Jane")
```

In the next task assignment, we will add this logic to our bot.