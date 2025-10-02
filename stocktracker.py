stock_prices = {
    "RELIANCE": 2500,
    "TCS": 3700,
    "INFY": 1500,
    "HDFC": 1650,
    "ICICIBANK": 980,
    "HDFCBANK": 1600,
    "SBIN": 650,
    "AXISBANK": 1020,
    "BAJFINANCE": 7400,
    "WIPRO": 420
}

portfolio = {}

while True:
    stock = input("Enter stock symbol (type 'list' to see all, 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    if stock == "LIST":
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue
    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue

    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("❌ Please enter a valid number for quantity.")

total_value = 0
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n Total Investment Value: ₹{total_value}")

save_choice = input("\nDo you want to save the result? (yes/no): ").lower()

if save_choice == "yes":
    file_type = input("Save as (txt/csv)? ").lower()
    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("--- Portfolio Summary ---\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{qty * stock_prices[stock]}\n")
            f.write(f"\nTotal Investment Value: ₹{total_value}\n")
        print(" Portfolio saved as portfolio.txt")
    elif file_type == "csv":
        import csv
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (INR)", "Value (INR)"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow(["Total", "", "", total_value])
        print(" Portfolio saved as portfolio.csv")
    else:
        print(" Invalid file type, not saved.")
