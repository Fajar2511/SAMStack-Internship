import json
import os
print("Contact Book Application")
contacts = []

def load_contacts():
    global contacts
    try:
    
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                contacts = json.load(file)  
            print("Contacts loaded successfully.")
        else:
            contacts = []  
            print("No existing contact file found. Starting with an empty contact book.")
    except json.JSONDecodeError:
        contacts = []
        print("Warning: contacts.json is corrupted. Starting with an empty contact book.")
    except Exception as e:
        contacts = []
        print(f"Error loading contacts: {e}")


def save_contacts():
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)  
    except Exception as e:
        print(f"Error saving contacts: {e}")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    if not phone.isdigit():
        print("Error: Phone must contain only digits")
        return
    
    contacts.append({"Name": name, "Phone": phone, "Email": email})
    save_contacts()  
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n---- Your Contacts ----")
        for i, c in enumerate(contacts, 1):
            print(f"{i}. Name: {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")

def search_contact():
    name = input("Enter name to search: ").lower()
    found = False
    for c in contacts:
        if c['Name'].lower() == name:
            print(f"Found! Name: {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")
            found = True
            break
    if not found:
        print("Contact not found")

def delete_contact():
    name = input("Enter the name of contact to be deleted: ").lower()
    for c in contacts:
        if c['Name'].lower() == name:
            contacts.remove(c)
            save_contacts()  
            print(f"Contact {c['Name']} deleted successfully.")
            return
    print("Cannot delete: Contact not found")

print("---- Contact Book ----")
load_contacts()

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")   
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting... Data saved in contacts.json. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5")