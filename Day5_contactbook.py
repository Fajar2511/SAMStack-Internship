print("---- Contact Book ----")
contacts = []  

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    if not phone.isdigit():
        print("Error: Phone must contain only digits")
        return
    
    contacts.append({"Name": name, "Phone": phone, "Email": email})
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. Name: {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")

def search_contact():
    name = input("Enter name to search: ")
    name = name.lower()  
    found = False
    for c in contacts:
        if c['Name'].lower() == name:
            print(f"Found! Name: {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")
            found = True
            break
    if not found:
        print("Contact not found")

def delete_contact():
    name = input("Enter the name of contact to be deleted: ")
    name = name.lower()  
    for c in contacts:
        if c['Name'].lower() == name:
            contacts.remove(c)
            print(f"Contact {c['Name']} deleted successfully.")
            return
    print("Cannot delete: Contact not found")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")   
    print("3. Search Contacts")
    print("4. Delete Contacts")
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
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5")

