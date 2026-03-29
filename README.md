# python-assignment-part2
Part 2 - Data Structures Out put


@brsp18 ➜ /workspaces/python-assignment-part2 (main) $ /usr/bin/python3 /workspaces/python-assignment-part2/part2_order_system.py


============= Starters ============
Paneer Tikka    ₹ 180.0  Available
Chicken Wings    ₹ 220.0  Unavailable
Veg Soup    ₹ 120.0  Available
============= Mains ============
Butter Chicken    ₹ 320.0  Available
Dal Tadka    ₹ 180.0  Available
Veg Biryani    ₹ 250.0  Available
Garlic Naan    ₹ 40.0  Available
========== Desserts =========
Gulab Jamun    ₹ 90.0  Available
Rasgulla    ₹ 80.0  Available
Ice Cream    ₹ 110.0  Unavailable


Total number of menu items: 10


Number of available items: 8
Number of unavailable items: 2


Most expensive item: Butter Chicken ₹ 320.0


=====Items priced under 150:=====
Veg Soup : ₹ 120.0
Garlic Naan : ₹ 40.0
Gulab Jamun : ₹ 90.0
Rasgulla : ₹ 80.0
Ice Cream : ₹ 110.0


Enter item name: Veg Biryani
Veg Biryani added to cart.
Do you want to add another item? (yes/no): no
Veg Biryani not found in cart.
Do you want to remove an item? (yes/no): no
[{'item': 'Veg Biryani', 'quantity': 1, 'price': 250.0}]


Order Summary:
Veg Biryani x 1 = ₹250.0
GST (5%): ₹13.12
Total Payable: ₹262.5


Original Inventory: {'Paneer Tikka': {'stock': 999, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}
Deep Inventory copy: {'Paneer Tikka': {'stock': 20, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}
Restored Original Inventory: {'Paneer Tikka': {'stock': 20, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}
2025-01-01 | Total Revenue: ₹790.0
2025-01-02 | Total Revenue: ₹1350.0
2025-01-03 | Total Revenue: ₹2310.0
2025-01-04 | Total Revenue: ₹2880.0

Daily Sales Totals: [790.0, 1350.0, 2310.0, 2880.0]

Best Selling Day is 2025-01-04: 2880.0

 ===== Item Order Count =====
Paneer Tikka         | 3 orders
Garlic Naan          | 5 orders
Gulab Jamun          | 4 orders
Veg Soup             | 1 orders
Butter Chicken       | 2 orders
Dal Tadka            | 2 orders
Veg Biryani          | 2 orders
Rasgulla             | 2 orders


Most Ordered Item: Garlic Naan | 6 orders
===== Revenue Per Day =====
2025-01-01 | ₹790.0
2025-01-02 | ₹560.0
2025-01-03 | ₹960.0
2025-01-04 | ₹570.0
2025-01-05 | ₹750.0

Best Selling Day: 2025-01-03 | ₹960.0