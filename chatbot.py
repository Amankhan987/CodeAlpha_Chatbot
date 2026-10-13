
def get_reply(message):
    message = message.lower()

    if "hello" in message or message == "hi":
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks!"
    elif "your name" in message:
        return "I am a simple Python chatbot."
    elif "help" in message:
        return "You can say: hello, how are you, your name, bye."
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand. Type 'help' for options."

print("=== SIMPLE CHATBOT === (type 'bye' to exit)")

while True:
    user = input("You: ")
    reply = get_reply(user)
    print("Bot:", reply)

    if "bye" in user.lower():
        break