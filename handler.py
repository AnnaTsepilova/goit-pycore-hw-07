from typing import Callable
from functools import wraps
from address_book import AddressBook
from record import Record
from birthday import Birthday

## Dictionary of error messages
error_message = {
    "INVALID_PHONENUMBER": "Phone number should contain only digits",
    "INVALID_COMMAND": "Error: Invalid command.",
    "INVALID_ARGUMENTS": "Error: invalid arguments.",
    "UNKNOWN_COMMAND": "Error: Unknown command",
    "CONTACT_EXIST": "Contact already exist.",
    "PHONE_EXIST": "Phone number already exist.",
    "CONTACT_NOT_FOUND": "Contact does not exist.",
    "CONTACT_ADDED": "Contact added.",
    "CONTACT_UPDATED": "Contact updated."
    }

def input_error(func: Callable):
    '''
    Generic input decorator for validation user input
    '''
    @wraps(func)
    def inner(*args, **kwargs):
        action = func.__name__.split('_')

        ## Additional message hint to error message
        usage_message = ""
        match func.__name__:
            case 'show_phone':
                usage_message = "Usage: phone NAME"
            case 'add_contact':
                usage_message = f"Usage: {action[0]} NAME PHONE"
            case 'change_contact':
                usage_message = f"Usage: {action[0]} NAME OLD_PHONE NEW_PHONE"
            case 'add_birthday':
                usage_message = f"Usage: add-birthday NAME {Birthday.format()}"
            case 'show_birthday':
                usage_message = "Usage: show-birthday NAME"

        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return error_message["INVALID_ARGUMENTS"] + f"\n  {e}\n  {usage_message}"
        except KeyError:
            return error_message["CONTACT_NOT_FOUND"]
        except IndexError:
            return error_message["INVALID_COMMAND"] + ' ' + usage_message

    return inner

def custom_error(func: Callable):
    '''
    Custom error decorator for validation
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"

    return inner


@custom_error
@input_error
def add_contact(args, book: AddressBook):
    '''
    Function add contacts
    '''
    name, phone, *_ = args
    record = book.find(name)
    message = error_message["CONTACT_UPDATED"]
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = error_message["CONTACT_ADDED"]
    if phone:
        if not record.find_phone(phone):
            record.add_phone(phone)
        else:
            message = error_message["PHONE_EXIST"]
    return message

@input_error
def change_contact(args, book: AddressBook):
    '''
    Function change existing contacts
    '''
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)
    return error_message["CONTACT_UPDATED"]

@input_error
def add_birthday(args, book: AddressBook):
    '''
    Function adds birthday to existing contact
    '''
    name, birthday = args

    record = book.find(name)
    message = error_message["CONTACT_UPDATED"]

    if record is None:
        return error_message["CONTACT_NOT_FOUND"]

    record.add_birthday(birthday)

    return message

@input_error
def show_birthday(args, book: AddressBook):
    '''
    Function show birthday in existing contact
    '''
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError

    return f"{record.birthday}"

def list_contacts(book: AddressBook):
    '''
    Function return all existing contacts
    '''
    if not book:
        return "Contacts are empty"
    output = '\n'.join([f"{record}" for item, record in book.items()])
    return output

@input_error
def show_phone(args, book: AddressBook):
    '''
    Function show phone of added contact
    '''
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError

    return f"phones: {'; '.join(p.value for p in record.phones)}"
