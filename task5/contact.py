class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, keyword):
        matching_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        if matching_contacts:
            for contact in matching_contacts:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        print("Contact deleted successfully.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
