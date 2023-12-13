def hello():
    return "How can I help you?"

def add_contact(contacts, username, phone):
    contacts[username] = phone
    return f"Contact {username} with phone number {phone} added."

def change_contact(contacts, username, new_phone):
    if username in contacts:
        contacts[username] = new_phone
        return f"Phone number for {username} updated to {new_phone}."
    else:
        return f"Contact with name {username} not found."

def show_phone(contacts, username):
    if username in contacts:
        return f"Phone number for {username}: {contacts[username]}"
    else:
        return f"Contact with name {username} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add" and len(args) == 2:
            username, phone = args
            print(add_contact(contacts, username, phone))
        elif command == "change" and len(args) == 2:
            username, new_phone = args
            print(change_contact(contacts, username, new_phone))
        elif command == "phone" and len(args) == 1:
            username = args[0]
            print(show_phone(contacts, username))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()