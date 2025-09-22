def greet_user():
    """
    Greet the user when they start the chatbot.
    """
    print("👋 Hello! I’m your Language Learning Chatbot.")
    print("Type 'bye' anytime to exit.")
    print("Let’s practice some basic phrases!\n")


def get_response(user_input):
    """
    Return a simple chatbot response based on user input.
    Rule-based: matches keywords to responses.
    """
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hola! (That means 'Hello' in Spanish 🌎)."

    # Asking how are you
    elif "how are you" in user_input:
        return "Estoy bien, gracias! (That means 'I am fine, thank you')."

    # Asking name
    elif "your name" in user_input:
        return "Me llamo ChatBot! (That means 'My name is ChatBot')."

    # Numbers
    elif "one" in user_input:
        return "'Uno' is one in Spanish."
    elif "two" in user_input:
        return "'Dos' is two in Spanish."
    elif "three" in user_input:
        return "'Tres' is three in Spanish."

    # Goodbye
    elif "bye" in user_input:
        return "Adiós! (Goodbye 👋)"
    
    # Default fallback
    else:
        return "Hmm 🤔 I don’t know that yet. Try asking something simple!"


def run_chatbot():
    """
    Run the chatbot loop until the user types 'bye'.
    """
    greet_user()
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    run_chatbot()