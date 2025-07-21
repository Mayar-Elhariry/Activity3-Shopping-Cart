store_items = {
    "apple":20,
    "honey":10,
    "milk":15,
    "bread":5,
    "cheese":15
}
cart = []
def view_items():
    print("Available Items are : \n")
    for item, price in store_items.items():
        print(f"{item} : {price}$")

def add_to_cart():
    item = input("Enter the wanted item, please :")
    if item in store_items:
        cart.append(item)
        print(f"{item} was added")
    else: 
        print(f"{item} is not found in store.")
def view_cart():
    if not cart:
        print("Your cart is empty")
        return
    print("Items in your cart are: \n")
    total = 0
    counted_items = {}
    for item in cart:
        counted_items[item] = counted_items.get(item, 0) + 1
        total += store_items[item]
    for item, count in counted_items.items():
        print(f"- {item.capitalize()} x{count} = ${store_items[item] * count:.2f}")
    print(f"Total Price: ${total:.2f}")

while True:
    print("----Options:")
    print("1. View avaliable items.")
    print("2. Add items to your cart.")
    print("3. View your cart and total price.")
    print("4. Exit.")
    option = input("Choose the number of the wanted option, please:")
    if option == "1":
         view_items()
    elif option== "2":
        add_to_cart()
    elif option =="3":
        view_cart()
    elif option == "4":
        print("See you soon, Goodbye.")
        break
    else:
        print("Invalid Option. Choose from 1-4 please.")


