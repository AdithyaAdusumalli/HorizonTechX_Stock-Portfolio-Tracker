import os

portfolio = {}


# Load portfolio from file
def load_portfolio():
    global portfolio

    if os.path.exists("portfolio.txt"):
        with open("portfolio.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    stock = data[0]
                    price = float(data[1])
                    quantity = int(data[2])

                    portfolio[stock] = {
                        "price": price,
                        "quantity": quantity
                    }


# Save portfolio to file
def save_portfolio():
    with open("portfolio.txt", "w") as file:
        for stock, details in portfolio.items():
            file.write(
                f"{stock},{details['price']},{details['quantity']}\n"
            )


# View Portfolio
def view_portfolio():
    if not portfolio:
        print("\nPortfolio is empty.")
        return

    print("\n===== YOUR PORTFOLIO =====")

    for stock, details in portfolio.items():
        print(
            f"{stock} | "
            f"Price: ₹{details['price']} | "
            f"Quantity: {details['quantity']}"
        )


# Add Stock
def add_stock():
    stock = input("Enter stock name: ").upper()

    price = float(input("Enter stock price: ₹"))
    quantity = int(input("Enter quantity: "))

    portfolio[stock] = {
        "price": price,
        "quantity": quantity
    }

    print("✅ Stock added successfully!")


# Update Stock
def update_stock():
    stock = input("Enter stock name to update: ").upper()

    if stock not in portfolio:
        print("❌ Stock not found.")
        return

    print("\n1. Update Price")
    print("2. Update Quantity")

    choice = input("Enter choice: ")

    if choice == "1":
        new_price = float(input("Enter new price: ₹"))

        portfolio[stock]["price"] = new_price

        print("✅ Price updated successfully!")

    elif choice == "2":
        new_quantity = int(input("Enter new quantity: "))

        portfolio[stock]["quantity"] = new_quantity

        print("✅ Quantity updated successfully!")

    else:
        print("❌ Invalid choice.")


# Delete Stock
def delete_stock():
    stock = input("Enter stock name to delete: ").upper()

    if stock in portfolio:
        del portfolio[stock]

        print("✅ Stock deleted successfully!")

    else:
        print("❌ Stock not found.")


# Calculate Investment
def calculate_investment():
    if not portfolio:
        print("\nPortfolio is empty.")
        return

    total = 0

    print("\n===== INVESTMENT SUMMARY =====")

    for stock, details in portfolio.items():
        investment = (
            details["price"] *
            details["quantity"]
        )

        total += investment

        print(
            f"{stock}: "
            f"₹{investment}"
        )

    print("\nTotal Investment Value: ₹", total)


# Main Program
load_portfolio()

while True:
    print("\n===== STOCK PORTFOLIO TRACKER =====")

    print("1. View Portfolio")
    print("2. Add Stock")
    print("3. Update Stock")
    print("4. Delete Stock")
    print("5. Calculate Total Investment")
    print("6. Save Portfolio")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_portfolio()

    elif choice == "2":
        add_stock()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        delete_stock()

    elif choice == "5":
        calculate_investment()

    elif choice == "6":
        save_portfolio()

        print("✅ Portfolio saved successfully!")

    elif choice == "7":
        save_portfolio()

        print("\nThank you for using Stock Portfolio Tracker!")
        print("Portfolio saved automatically.")

        break

    else:
        print("❌ Invalid choice. Please try again.")