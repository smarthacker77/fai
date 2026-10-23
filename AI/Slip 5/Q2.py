while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "how are you":
        print("Bot: I am fine.")
    elif user == "your name":
        print("Bot: I am a simple chatbot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")