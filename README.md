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
Do you want to add another item? (yes/no): yes
Enter item name: Veg Soup
Veg Soup added to cart.
Do you want to add another item? (yes/no): yes
Enter item name: Rasgulla
Rasgulla added to cart.
Do you want to add another item? (yes/no): yes
Enter item name: Ice Cream 
Item not available
Do you want to add another item? (yes/no): yes
Enter item name: Veg Soup
Veg Soup quantity updated to 2
Do you want to add another item? (yes/no): no
Veg Biryani not found in cart.
Do you want to remove an item? (yes/no): yes
Enter item name to remove: Veg Soup
Veg Soup quantity updated to 1
[{'item': 'Veg Biryani', 'quantity': 1, 'price': 250.0}, {'item': 'Veg Soup', 'quantity': 1, 'price': 120.0}, {'item': 'Rasgulla', 'quantity': 1, 'price': 80.0}]


Order Summary:
Veg Biryani x 1 = ₹250.0
Veg Soup x 1 = ₹120.0
Rasgulla x 1 = ₹80.0
GST (5%): ₹23.62
Total Payable: ₹472.5


Original Inventory: {'Paneer Tikka': {'stock': 999, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}
Deep Inventory copy: {'Paneer Tikka': {'stock': 20, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}
Restored Original Inventory: {'Paneer Tikka': {'stock': 20, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}
2025-01-01 | Total Revenue: ₹790.0
2025-01-02 | Total Revenue: ₹1350.0
2025-01-03 | Total Revenue: ₹2310.0
2025-01-04 | Total Revenue: ₹2880.0
2025-01-05 | Total Revenue: ₹3630.0

Daily Sales Totals: [790.0, 1350.0, 2310.0, 2880.0, 3630.0]

Best Selling Day is 2025-01-05: 3630.0

 ===== Item Order Count =====
Paneer Tikka         | 4 orders
Garlic Naan          | 6 orders
Gulab Jamun          | 5 orders
Veg Soup             | 1 orders
Butter Chicken       | 3 orders
Dal Tadka            | 2 orders
Veg Biryani          | 2 orders
Rasgulla             | 3 orders

Most Ordered Item: Garlic Naan | 6 orders
===== Revenue Per Day =====
2025-01-01 | ₹790.0
2025-01-02 | ₹560.0
2025-01-03 | ₹960.0
2025-01-04 | ₹570.0
2025-01-05 | ₹750.0

Best Selling Day: 2025-01-03 | ₹960.0
===== All Orders =====
1. 2025-01-01 | Order ID: 1 | Items: ['Paneer Tikka', 'Garlic Naan'] | ₹220.0
2. 2025-01-01 | Order ID: 2 | Items: ['Gulab Jamun', 'Veg Soup'] | ₹210.0
3. 2025-01-01 | Order ID: 3 | Items: ['Butter Chicken', 'Garlic Naan'] | ₹360.0
4. 2025-01-02 | Order ID: 4 | Items: ['Dal Tadka', 'Garlic Naan'] | ₹220.0
5. 2025-01-02 | Order ID: 5 | Items: ['Veg Biryani', 'Gulab Jamun'] | ₹340.0
6. 2025-01-03 | Order ID: 6 | Items: ['Paneer Tikka', 'Rasgulla'] | ₹260.0
7. 2025-01-03 | Order ID: 7 | Items: ['Butter Chicken', 'Veg Biryani'] | ₹570.0
8. 2025-01-03 | Order ID: 8 | Items: ['Garlic Naan', 'Gulab Jamun'] | ₹130.0
9. 2025-01-04 | Order ID: 9 | Items: ['Dal Tadka', 'Garlic Naan', 'Rasgulla'] | ₹300.0
10. 2025-01-04 | Order ID: 10 | Items: ['Paneer Tikka', 'Gulab Jamun'] | ₹270.0
11. 2025-01-05 | Order ID: 11 | Items: ['Butter Chicken', 'Gulab Jamun', 'Garlic Naan'] | ₹490.0
12. 2025-01-05 | Order ID: 12 | Items: ['Paneer Tikka', 'Rasgulla'] | ₹260.0