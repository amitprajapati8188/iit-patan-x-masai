import numpy as np
import json
from tabulate import tabulate

ITEMS = {
    1: ("Rice", 50),
    2: ("Milk", 30),
    3: ("Bread", 25),
    4: ("Eggs", 10),
    5: ("Sugar", 45)
}

def display_menu():
    headers = ["Item ID", "Item", "Price"]
    rows = [[item_id, name, price] for item_id, (name, price) in ITEMS.items()]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def get_user_selection():
    count = int(input("\nHow many different items do you want to purchase? "))
    selected_ids, selected_qty = [], []
    for _ in range(count):
        while True:
            try:
                item_id = int(input("Enter Item ID (1–5): "))
                if item_id in ITEMS:
                    qty = int(input(f"Enter quantity for {ITEMS[item_id][0]}: "))
                    selected_ids.append(item_id)
                    selected_qty.append(qty)
                    break
                else:
                    print("Invalid Item ID. Try again.")
            except ValueError:
                print("Please enter valid numbers.")
    return np.array(selected_ids), np.array(selected_qty)

def calculate_totals(item_ids, quantities):
    prices = np.array([ITEMS[i][1] for i in item_ids])
    return prices * quantities

def apply_discount(amount):
    return amount * 0.9 if amount > 500 else amount

def generate_bill_table(item_ids, quantities, totals):
    return [[ITEMS[i][0], quantities[idx], totals[idx]] for idx, i in enumerate(item_ids)]

def export_to_json(item_ids, quantities, subtotal, discount, final_total):
    bill_data = {
        "items": [ITEMS[i][0] for i in item_ids],
        "quantities": quantities.tolist(),
        "subtotal": float(subtotal),
        "discount": float(discount),
        "final_total": float(final_total)
    }
    with open("grocery_bill.json", "w") as f:
        json.dump(bill_data, f, indent=4)

def main():
    display_menu()
    item_ids, quantities = get_user_selection()
    totals = calculate_totals(item_ids, quantities)
    subtotal = np.sum(totals)
    final_total = apply_discount(subtotal)
    discount = subtotal - final_total

    print("\nFinal Bill")
    print(tabulate(generate_bill_table(item_ids, quantities, totals),
                   headers=["Item", "Quantity", "Total"], tablefmt="grid"))
    print(f"\nSubtotal: {subtotal}")
    print(f"Discount: {discount}")
    print(f"Total Payable: {final_total}")

    export_to_json(item_ids, quantities, subtotal, discount, final_total)
    print("\nBill exported to grocery_bill.json")

if __name__ == "__main__":
    main()