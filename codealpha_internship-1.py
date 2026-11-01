"""CodeAlpha Python Internship Project: three beginner-friendly tasks.
Run with: python codealpha_internship.py
"""
import random

# TASK 1: HANGMAN GAME
WORDS = ["PYTHON", "COMPUTER", "GITHUB", "PROGRAM", "KEYBOARD"]
MAX_WRONG_GUESSES = 6

def play_hangman():
    secret = random.choice(WORDS)
    guessed = set()
    wrong = 0
    print("\n--- HANGMAN GAME ---")
    while wrong < MAX_WRONG_GUESSES:
        print("\nWord:", " ".join(ch if ch in guessed else "_" for ch in secret))
        print("Incorrect guesses left:", MAX_WRONG_GUESSES - wrong)
        guess = input("Enter one letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter exactly one alphabet letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        guessed.add(guess)
        if guess in secret:
            print("Correct!")
        else:
            wrong += 1
            print("Not in the word.")
        if all(ch in guessed for ch in secret):
            print("Congratulations! You guessed", secret)
            return
    print("Game over! The word was", secret)

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

# TASK 4: BASIC RULE-BASED CHATBOT
def get_bot_reply(message):
    text = message.lower().strip()
    if not text:
        return "Please type something so I can respond."
    if any(word in text for word in ("bye", "goodbye", "exit", "quit")):
        return "Goodbye! Have a productive day."
    if any(word in text for word in ("hello", "hi", "hey")):
        return "Hello! Welcome. How can I help you today?"
    if "your name" in text or "who are you" in text:
        return "I'm AlphaBot, a simple Python rule-based chatbot."
    if "how are you" in text:
        return "I'm doing well, thank you! How can I help?"
    if "help" in text:
        return "Try hello, ask my name, ask how I am, or say goodbye."
    if "python" in text:
        return "Python is a beginner-friendly programming language."
    return "I'm still learning. Type help to see what I understand."

def run_chatbot():
    print("\n--- ALPHABOT --- Type 'help' for examples or 'bye' to exit.")
    while True:
        message = input("You: ")
        reply = get_bot_reply(message)
        print("AlphaBot:", reply)
        if any(word in message.lower().strip() for word in ("bye", "goodbye", "exit", "quit")):
            break

# MAIN MENU
def main():
    print("Welcome to the CodeAlpha Python Internship Project!")
    while True:
        print("\n" + "=" * 46)
        print("       CODEALPHA PYTHON PROJECT MENU")
        print("=" * 46)
        print("1. Hangman Game\n2. Stock Portfolio Tracker\n3. Basic Chatbot\n4. Exit")
        choice = input("Choose 1-4: ").strip()
        if choice == "1":
            play_hangman()
        elif choice == "2":
            run_portfolio_tracker()
        elif choice == "3":
            run_chatbot()
        elif choice == "4":
            print("Thank you for using the project. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
