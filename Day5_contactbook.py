print("----Contact Book----")
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
        for c in contacts:
            print(f"Name: {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")   
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid choice")

