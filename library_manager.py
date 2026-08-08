class Resource:
    def __init__(self, resource_id, title):
        self.resource_id = resource_id
        self.title = title
        self.__is_issued = False
    def issue_item(self):
        if self.__is_issued:
            print("Resource is already issued!")
        else:
            self.__is_issued = True
            print("Resource issued successfully.")
    def return_item(self):
        if self.__is_issued:
            self.__is_issued = False
            print("Resource returned successfully.")
        else:
            print("Resource was not issued.")
    def get_status(self):
        return self.__is_issued
    def display_details(self):
        print("Resource ID:", self.resource_id)
        print("Title:", self.title)
class Book(Resource):
    def __init__(self, resource_id, title, author, isbn):
        super().__init__(resource_id, title)
        self.author = author
        self.isbn = isbn
    def display_details(self):
        print("\n--- Book Details ---")
        print("ID:", self.resource_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        if self.get_status():
            print("Status: Issued")
        else:
            print("Status: Available")
class HardwareDevice(Resource):
    def __init__(self, resource_id, title, serial_number, specifications):
        super().__init__(resource_id, title)
        self.serial_number = serial_number
        self.specifications = specifications
    def display_details(self):
        print("\n--- Hardware Details ---")
        print("ID:", self.resource_id)
        print("Device:", self.title)
        print("Serial Number:", self.serial_number)
        print("Specifications:", self.specifications)
        if self.get_status():
            print("Status: Issued")
        else:
            print("Status: Available")
class LibraryManager:
    def __init__(self):
        self.resources = []
    def add_resource(self, resource):
        self.resources.append(resource)
    def show_all_resources(self):
        print("\n All Resources ")
        for item in self.resources:
            item.display_details()
    def search_resource(self, value):
        for item in self.resources:
            if item.resource_id == value or item.title.lower() == value.lower():
                item.display_details()
                return item
        print("Resource not found!")
        return None
    def issue_resource(self, value):
        item = self.search_resource(value)
        if item:
            item.issue_item()
    def return_resource(self, value):
        item = self.search_resource(value)
        if item:
            item.return_item()
manager = LibraryManager()
book1 = Book("B101","Python Programming","John Smith","ISBN12345")
book2 = Book("B102","OOP Concepts","Ali Khan","ISBN67890")
device1 = HardwareDevice("H101","Laptop","SN555","Core i5, 8GB RAM")
manager.add_resource(book1)
manager.add_resource(book2)
manager.add_resource(device1)
while True:
    print("\n===== Library Resource Tracker =====")
    print("1. Display All Resources")
    print("2. Search Resource")
    print("3. Issue Resource")
    print("4. Return Resource")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        manager.show_all_resources()
    elif choice == "2":
        value = input("Enter ID or Title: ")
        manager.search_resource(value)
    elif choice == "3":
        value = input("Enter Resource ID or Title to issue: ")
        manager.issue_resource(value)
    elif choice == "4":
        value = input("Enter Resource ID or Title to return: ")
        manager.return_resource(value)
    elif choice == "5":
        print("Program Closed.")
        break
    else:
        print("Invalid Choice!")