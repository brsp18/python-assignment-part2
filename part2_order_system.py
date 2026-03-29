import copy

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 20, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
    "2025-01-05": [
        {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
        {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
    ]
}


# Task 1 — Explore the Menu 
#1.Print the full menu grouped by category, formatted like
print("\n")
print("============= Starters ============")
for key,value in menu.items():
    if value["category"] == "Starters":
      if value["available"] == True:
        print(key,"  ","₹",value["price"]," Available")
      else:
        print(key,"  ","₹",value["price"]," Unavailable")

print("============= Mains ============")
for key,value in menu.items():
    if value["category"] == "Mains":
        if value["available"] == True:
         print(key,"  ","₹",value["price"]," Available")
        else:
          print(key,"  ","₹",value["price"]," Unavailable") 

print("========== Desserts =========")
for key, value in menu.items():
    if value["category"] == "Desserts":
      if value["available"] == True:
       print(key,"  ","₹",value["price"]," Available")
      else:
       print(key,"  ","₹",value["price"]," Unavailable")


#2. Using dictionary methods, compute and print:

print("\n")
total_count = len(menu) 
print("Total number of menu items:", total_count)

available_items =0
unavailable_items = 0
for key, value in menu.items():
    if value["available"] == True:
     available_items = available_items +1 
    else:
      unavailable_items = unavailable_items +1
print("\n")      
print("Number of available items:", available_items)
print("Number of unavailable items:", unavailable_items)

expensive = []
for key, value in menu.items():
       expensive.append(value["price"])
most_expensive = max(expensive)

for key, value in menu.items():
 if value["price"] == most_expensive:
  print("\n")
  print("Most expensive item:", key, "₹", most_expensive)
  print("\n")

print("=====Items priced under 150:=====")
for key, value in menu.items():
    if value["price"] <= 150:
       print(key,":", "₹",value["price"])




#Task 2 —  Cart Operations:

cart = [] # calling the function 
print("\n")

def add_to_cart(item_name):
    if item_name in menu and menu[item_name]["available"]:
        for entry in cart:   # Check if already in cart
            if entry["item"] == item_name:
                entry["quantity"] += 1
                print(f"{item_name} quantity updated to {entry['quantity']}")
                return
        
        # Not in cart yet — add fresh
        cart.append({
            "item":     item_name,
            "quantity": 1,
            "price":    menu[item_name]["price"]
        })
        print(f"{item_name} added to cart.")
    
    else:
        print("Item not available")

item_name = input("Enter item name: ") # inputing item name from user 
add_to_cart(item_name)



def add_another_item(item_name):
        while True:
            add_another_item = input("Do you want to add another item? (yes/no): ")
            if add_another_item == "yes":
                item_name = input("Enter item name: ")
                add_to_cart(item_name)
            elif add_another_item == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


add_another_item(item_name)


def remove_an_item(item_name):
   for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] -= 1
            if entry["quantity"] <= 0:
                cart.remove(entry)
                print(f"{item_name} removed from cart.")
            else:
                print(f"{item_name} quantity updated to {entry['quantity']}")
            return
print(f"{item_name} not found in cart.")

item_name = input("Do you want to remove an item? (yes/no): ")
if item_name == "yes":
    item_name = input("Enter item name to remove: ")
    remove_an_item(item_name)

print(cart)
print("\n")
# Printing order Summary

def print_order_summary():
    print("Order Summary:")
    total_amount = 0
    for entry in cart:
        item_total = entry["quantity"] * entry["price"]
        GST =  0.05 * item_total
        total_amount = total_amount + item_total + GST # Adding 5% tax
        print(f"{entry['item']} x {entry['quantity']} = ₹{item_total}")
    print("GST (5%): ₹{:.2f}".format(0.05 * total_amount))
    print(f"Total Payable: ₹{total_amount}")
   
print_order_summary()



#Task 3 - Inventory Tracker with Deep Copy

shallow_inventory = inventory.copy() # outer dict copied; inner dicts still shared
inventory_backup =copy.deepcopy(inventory) # completely independent copy
print("\n")
inventory["Paneer Tikka"]["stock"] = 999 # modifying inventory here
print("Original Inventory:", inventory)
print("Deep Inventory copy:", inventory_backup) 

inventory = copy.deepcopy(inventory_backup) # Restoring original inventory with deep copy
print("Restored Original Inventory:", inventory)


#Task 4 — Daily Sales Log Analysis

daily_total = 0
daily_total_list = []
for date, orders in sales_log.items():
    for order in orders:
        daily_total = daily_total + order["total"]
    daily_total_list.append(daily_total)
    print(f"{date} | Total Revenue: ₹{daily_total}")

print(f"\nDaily Sales Totals: {daily_total_list}")
print(f"\nBest Selling Day is {date}: {max(daily_total_list)}")

#Find the most ordered item 

item_count = {}

for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

print("\n","===== Item Order Count =====")
for item, count in item_count.items():
    print(f"{item:20} | {count} orders")

most_ordered = max(item_count, key=lambda x: item_count[x])
print(f"\nMost Ordered Item: {most_ordered} | {item_count[most_ordered]} orders")



print("===== Revenue Per Day =====")
best_day = None
best_revenue = 0

for date, orders in sales_log.items():
    daily_total = sum(order["total"] for order in orders)
    print(f"{date} | ₹{daily_total}")

    if daily_total > best_revenue:
        best_revenue = daily_total
        best_day = date

print(f"\nBest Selling Day: {best_day} | ₹{best_revenue}")



print("===== All Orders =====")

all_orders = []
for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))  # building into one list

for number, (date, order) in enumerate(all_orders, start=1):
    print(f"{number}. {date} | Order ID: {order['order_id']} | Items: {order['items']} | ₹{order['total']}")