def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "❌ Please provide both name and phone."
    name, phone = args
    contacts[name] = phone
    return "✅ Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "❌ Please provide both name and new phone."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "🔁 Contact updated."
    else:
        return "⚠️ Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "❌ Please provide the contact name."
    name = args[0]
    if name in contacts:
        return f"📞 {name}'s phone number: {contacts[name]}"
    else:
        return "⚠️ Contact not found."


def show_all(contacts):
    if not contacts:
        return "📭 No contacts found."
    result = "📒 Contact list:\n"
    for name, phone in contacts.items():
        result += f"- {name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("👋 Welcome to the assistant bot!")

    while True:
        user_input = input("📝 Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("👋 Good bye!")
            break

        elif command == "hello":
            print("🤖 How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("❗ Invalid command.")


if __name__ == "__main__":
    main()
