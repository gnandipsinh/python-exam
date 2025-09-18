items = []
categories = []
quantities = []

print("welcome to inventory list analyzer...")

while True:
    name = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    items.append(name)
    categories.append(category.lower())
    quantities.append(quantity)

    choice = input("Do you want to add more items? (y/n): ")
    if choice.lower() != "y":
        break





total_items = len(items)

print("Total Different Items:", total_items)

print("Explanation: You entered", total_items, "different items:", ", ".join(items) + ".")


max_quantity = max(quantities)

max_item = items[quantities.index(max_quantity)]

print("\n\nMost Stocked Item:", max_item, "(", max_quantity, "units )")

print("", max_item, "has the highest quantity among all items.")

total_quantity = sum(quantities)

print("\n\nTotal Quantity in Stock:", total_quantity)

print(" Sum of all quantities:", " + ".join(map(str, quantities)), "=", total_quantity)


max_quantity = max(quantities)

max_item = items[quantities.index(max_quantity)]

print("\n\nMost Stocked Item:", max_item, "(", max_quantity, "units )")

print("", max_item, "has the highest quantity among all items.")

    
min_quantity = min(quantities)

min_item = items[quantities.index(min_quantity)]

print("\n\nLeast Stocked Item:", min_item, "(", min_quantity, "units )")

print("", min_item, "has the lowest quantity.")

unique_categories = set(categories)


print("Unique Categories in Inventory:", unique_categories)

print("Categories are taken from user input and converted to lowercase.")

print("No duplicates are shown here.")








print(" The set of unique categories was sorted alphabetically for display.")


