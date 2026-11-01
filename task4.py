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