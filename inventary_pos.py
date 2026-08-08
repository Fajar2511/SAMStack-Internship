import json

FILE = "inventory.json"


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        
        return [
            {"id":"101", "name":"Pen", "price":50, "stock":20},
            {"id":"102", "name":"Notebook", "price":200, "stock":10},
            {"id":"103", "name":"Mouse", "price":1500, "stock":5}
        ]


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def show_inventory(data):
    print("\nID\tName\tPrice\tStock")
    print("-"*30)
    for item in data:
        print(f"{item['id']}\t{item['name']}\t{item['price']}\t{item['stock']}")


def billing(data):
    cart = []
    while True:
        item_id = input("Enter Item ID or 'done': ")
        if item_id == "done": break

       
        item = None
        for i in data:
            if i["id"] == item_id:
                item = i
                break

        if not item:
            print("Item not found")
            continue

        qty = int(input("Enter Quantity: "))

        if qty > item["stock"]:
            print("Not enough stock")
            continue

        item["stock"] -= qty
        total = item["price"] * qty
        cart.append([item["name"], qty, total])
        print(f"{item['name']} added")

    if len(cart) == 0: return

    
    subtotal = 0
    for c in cart: subtotal += c[2]

    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.10
        print("10% Discount Applied")

    tax = (subtotal - discount) * 0.05
    final = subtotal - discount + tax

    
    print("\n--- RECEIPT ---")
    for c in cart:
        print(f"{c[0]} x{c[1]} = {c[2]}")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}")
    print(f"Tax 5%: {tax}")
    print(f"Total: {final}")

    save_data(data) 


def main():
    data = load_data()
    while True:
        print("\n1. View Inventory")
        print("2. Billing")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == "1": show_inventory(data)
        elif choice == "2": billing(data)
        elif choice == "3": break
        else: print("Wrong choice")

main()