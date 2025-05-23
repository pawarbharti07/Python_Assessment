# -*- coding: utf-8 -*-
"""Assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IGsqb8lX8ZR3nbA7ble11P-r3bjwNSyR
"""

#1.Write a program to demonstrate the Fruit Store Console application.
def show_menu():
    print("\n------ Fruit Store Menu ------")
    print("1. View available fruits")
    print("2. Buy fruits")
    print("3. View cart")
    print("4. Checkout and exit")

def show_fruits(fruits):
    print("\nAvailable Fruits:")
    for fruit, price in fruits.items():
        print(f"{fruit.title()} - ₹{price}/kg")

def buy_fruits(fruits, cart):
    show_fruits(fruits)
    fruit_name = input("Enter the name of the fruit you want to buy: ").lower()
    if fruit_name in fruits:
        try:
            quantity = float(input(f"Enter quantity of {fruit_name} in kg: "))
            if quantity > 0:
                if fruit_name in cart:
                    cart[fruit_name] += quantity
                else:
                    cart[fruit_name] = quantity
                print(f"{quantity} kg of {fruit_name} added to cart.")
            else:
                print("Please enter a positive quantity.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Sorry, fruit not available.")

def view_cart(cart, fruits):
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for fruit, quantity in cart.items():
        price = fruits[fruit] * quantity
        total += price
        print(f"{fruit.title()} - {quantity} kg - ₹{price:.2f}")
    print(f"Total Amount: ₹{total:.2f}")

def main():
    fruits = {
        'apple': 100,
        'banana': 40,
        'mango': 80,
        'orange': 60,
        'grape': 90
    }
    cart = {}
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_fruits(fruits)
        elif choice == '2':
            buy_fruits(fruits, cart)
        elif choice == '3':
            view_cart(cart, fruits)
        elif choice == '4':
            print("\nFinal Bill:")
            view_cart(cart, fruits)
            print("Thank you for shopping at the Fruit Store!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

# Run the application
main()

#2.Prepare demonstration of Python Fruit Store under software development principles and follow coding protocols.
"""
Fruit Store Console Application
Author: Your Name
Description: A simple console-based fruit store app following software development principles.
"""

# ---------- Data Layer ----------
FRUIT_PRICES = {
    'apple': 100,
    'banana': 40,
    'mango': 80,
    'orange': 60,
    'grape': 90
}

# ---------- Business Logic Layer ----------
def calculate_total(cart):
    total = 0
    for fruit, quantity in cart.items():
        total += FRUIT_PRICES[fruit] * quantity
    return total

def add_to_cart(cart, fruit, quantity):
    if fruit in cart:
        cart[fruit] += quantity
    else:
        cart[fruit] = quantity

# ---------- UI Layer ----------
def display_menu():
    print("\n====== Fruit Store Menu ======")
    print("1. View Available Fruits")
    print("2. Buy Fruits")
    print("3. View Cart")
    print("4. Checkout and Exit")

def display_fruits():
    print("\nAvailable Fruits and Prices:")
    for fruit, price in FRUIT_PRICES.items():
        print(f"- {fruit.title()}: ₹{price}/kg")

def display_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for fruit, quantity in cart.items():
        price = FRUIT_PRICES[fruit] * quantity
        total += price
        print(f"{fruit.title()} - {quantity:.2f} kg - ₹{price:.2f}")
    print(f"Total Amount: ₹{total:.2f}")

def get_user_input():
    return input("Enter your choice (1-4): ").strip()

def handle_buy(cart):
    display_fruits()
    fruit = input("Enter the fruit name to buy: ").strip().lower()
    if fruit not in FRUIT_PRICES:
        print("Fruit not available.")
        return
    try:
        quantity = float(input(f"Enter quantity of {fruit} in kg: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        add_to_cart(cart, fruit, quantity)
        print(f"{quantity} kg of {fruit} added to cart.")
    except ValueError:
        print("Invalid quantity entered.")

# ---------- Main Program ----------
def main():
    cart = {}
    while True:
        display_menu()
        choice = get_user_input()
        if choice == '1':
            display_fruits()
        elif choice == '2':
            handle_buy(cart)
        elif choice == '3':
            display_cart(cart)
        elif choice == '4':
            print("\nFinal Bill:")
            display_cart(cart)
            print("Thank you for shopping at the Fruit Store!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

#3.Prepare code with module controller – which holds your actual code that may be inside root.

#After each operation always display menu:
#• Make sure validation proper given – each option - display appropriate
#message if user enter invalid input and accept values again and - use
#looping concepts and string inbuilt methods concepts in this logic
#implementation
#• Make sure code prevent from unexpected exception return to the previous
#menu and accept all details again.

import logging

logging.basicConfig(filename='transactions.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_transaction(message):
    logging.info(message)

def display_menu():
    print("\n===== MAIN MENU =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Exit")

def add_item():
    try:
        item = input("Enter item name to add: ").strip()
        if item == "":
            print("Item name cannot be empty.")
            return
        print(f"Item '{item}' added successfully.")
        log_transaction(f"Added item: {item}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

def remove_item():
    try:
        item = input("Enter item name to remove: ").strip()
        if item == "":
            print("Item name cannot be empty.")
            return
        print(f"Item '{item}' removed successfully.")
        log_transaction(f"Removed item: {item}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

def view_items():
    try:
        print("Showing all items (This is placeholder text).")
        log_transaction("Viewed items")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

def main():
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-4): ").strip()
            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice = int(choice)
            if choice == 1:
                add_item()
            elif choice == 2:
                remove_item()
            elif choice == 3:
                view_items()
            elif choice == 4:
                print("Exiting the application.")
                log_transaction("User exited the application.")
                break
            else:
                print("Invalid choice. Please select from 1 to 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Returning to the main menu...")

if __name__ == "__main__":
    main()

