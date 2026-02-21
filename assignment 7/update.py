import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'inventory.json')

new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}

with open(file_path, 'r') as file:
    inventory = json.load(file)

print(f"Initial book count: {len(inventory)}")

already_exists = False
for book in inventory:
    if book['title'].lower() == new_book['title'].lower():
        already_exists = True
        break

if not already_exists:
    inventory.append(new_book)
    with open(file_path, 'w') as file:
        json.dump(inventory, file, indent=4)
    print(f"Added: {new_book['title']}")
else:
    print(f"Skipped: {new_book['title']} already exists")

print("\n--- Current Bookstore Inventory ---")
for book in inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")