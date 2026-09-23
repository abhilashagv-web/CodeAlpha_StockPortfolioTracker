# CodeAlpha - Stock Portfolio Tracker

print("====================================")
print("     STOCK PORTFOLIO TRACKER")
print("====================================")

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "=", "$", price)

print("\nEnter your stock details.")
print("Type 'done' when you have finished.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    print("Stock:", stock_name)
    print("Price per share: $", price)
    print("Quantity:", quantity)
    print("Investment: $", investment)
    print()

print("====================================")
print("Total Investment: $", total_investment)
print("====================================")

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("=======================\n")
    file.write("Total Investment: $" + str(total_investment))

print("\nPortfolio result saved to portfolio_result.txt")