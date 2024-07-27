from address_book import AddressBook

import handler

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except KeyboardInterrupt:
            print("Good bye!")
            break

        if not user_input:
            continue
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(handler.add_contact(args, book))
            case "change":
                print(handler.change_contact(args, book))
            case "phone":
                print(handler.show_phone(args, book))
            case "all":
                print(handler.list_contacts(book))
            case "add-birthday":
                print(handler.add_birthday(args, book))
            case "show-birthday":
                print(handler.show_birthday(args, book))
            case "birthdays":
                upcoming_birthdays = book.get_upcoming_birthdays()
                print("Список привітань на цьому тижні:", upcoming_birthdays)

            case _:
                print(handler.error_message["UNKNOWN_COMMAND"])

if __name__ == "__main__":
    main()
