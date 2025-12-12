import random
import datetime
import time
user_name=input("What is your name? ")

present_hour = datetime.datetime.now().hour

if 5 <= present_hour <= 11:
    print(f"Good Morning, {user_name}")
elif 12 <= present_hour <= 17:
    print(f"Good Afternoon, {user_name}")
else:
    print(f"Hello, {user_name}")

print("HELLO WELCOME TO THE RULE BASED PYTHON CHATBOT")
print("DO YOU HAVE ANY QUESTIONS?")

responses = {
    "hi": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! How may I help you?"
    ],

    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Feel free to come back anytime."
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "No problem at all!"
    ],

    "fallback": [
        "I'm not sure I understand. Could you try rephrasing?",
        "Hmm… I didn’t get that. Can you clarify?",
        "Sorry, I don't have info on that."
    ],

    "about_bot": [
        "I'm a rule-based chatbot built to answer basic queries.",
        "I'm here to help with predefined responses!",
        "I'm a simple chatbot using pattern matching to respond."
    ],

    "weather": [
        "I can't check real-time weather, but it's always a good idea to keep an umbrella handy!",
        "Weather data isn't available, but I hope it's nice where you are!"
    ],

    "name": [
        "I'm your friendly chatbot!",
        "You can call me ChatBot!"
    ],

    "help":[
        "Sure! You can ask me about greetings, my name, or general info.",
        "I'm here to support! Try asking something simple like 'hello' or 'who are you'."
    ]
}


def getbotresponse(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
    return "Sorry, I don't know what you mean."


while True:
    userinput = input("Please ask your question: ")

    reply = random.choice(getbotresponse(userinput))
    print("Bot Response: ", reply)

    if "bye" in userinput.lower():
        break
