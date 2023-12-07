def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
        except KeyboardInterrupt:
            return "Good bye!"

    return wrapper


class Assistant:
    def __init__(self):
        self.contacts = {}

    @input_error
    def hello(self):
        return "How can I help you?"

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Contact {name} added successfully."

    @input_error
    def change_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Phone number for {name} changed successfully."
        else:
            raise IndexError

    @input_error
    def get_phone(self, name):
        if name in self.contacts:
            return f"The phone number for {name} is {self.contacts[name]}."
        else:
            raise IndexError

    @input_error
    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts found."
        else:
            result = "All contacts:\n"
            for name, phone in self.contacts.items():
                result += f"{name}: {phone}\n"
            return result.strip()

    def exit(self):
        return "Good bye!"


@input_error
def main():
    assistant = Assistant()

    while True:
        command = input("Enter command: ").lower()

        if command in ["good bye", "close", "exit"]:
            print(assistant.exit())
            break

        if command == "hello":
            print(assistant.hello())
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(assistant.add_contact(name, phone))
        elif command.startswith("change"):
            _, name, phone = command.split()
            print(assistant.change_contact(name, phone))
        elif command.startswith("phone"):
            _, name = command.split()
            print(assistant.get_phone(name))
        elif command == "show all":
            print(assistant.show_all_contacts())
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
