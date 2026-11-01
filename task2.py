# TASK 2: STOCK PORTFOLIO TRACKER (sample prices, not live quotes)
STOCK_PRICES = {"AAPL": 180.00, "TSLA": 250.00, "MSFT": 420.00,
                "GOOGL": 165.00, "AMZN": 190.00}

def run_portfolio_tracker():
    print("\n--- STOCK PORTFOLIO TRACKER ---")
    holdings = {}
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: sample price ${price:.2f}")
        while True:
            try:
                quantity = int(input(f"Quantity of {symbol} (0 to skip): "))
                if quantity < 0:
                    print("Enter zero or a positive whole number.")
                    continue
                if quantity:
                    holdings[symbol] = quantity
                break
            except ValueError:
                print("Please enter a whole number.")
    if not holdings:
        print("No stocks selected.")
        return
    lines = ["SAMPLE STOCK PORTFOLIO REPORT", "-" * 38]
    total = 0.0
    for symbol, quantity in holdings.items():
        value = STOCK_PRICES[symbol] * quantity
        total += value
        line = f"{symbol}: {quantity} x ${STOCK_PRICES[symbol]:.2f} = ${value:.2f}"
        print(line)
        lines.append(line)
    print(f"TOTAL SAMPLE VALUE: ${total:.2f}")
    lines.append(f"TOTAL SAMPLE VALUE: ${total:.2f}")
    lines.append("Note: Hardcoded educational prices; not live market data.")
    if input("Save report to portfolio_report.txt? (y/n): ").strip().lower() == "y":
        with open("portfolio_report.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(lines))
        print("Report saved successfully.")