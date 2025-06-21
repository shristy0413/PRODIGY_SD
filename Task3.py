#3
import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"✅ Contact '{name}' added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("⚠️ No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"👤 {name}: 📞 {info['phone']}, 📧 {info['email']}")

# Edit a contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone = input("New phone number: ")
        email = input("New email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"✏️ Contact '{name}' updated.")
    else:
        print("❌ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

# Menu
def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("📁 Contacts saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
