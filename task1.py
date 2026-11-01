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