import json

inventory = {}

product_id = input("Enter Product ID : ")
product_name = input("Enter Product Name : ")
price = input("Enter Price : ")

inventory[product_id] = {
    "product_name": product_name,
    "price": price
}

with open("inventory.json", "w") as file:

    json.dump(inventory, file, indent=4)

print("Inventory Stored")