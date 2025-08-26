

# AI CHAT BOT

import random

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.responses = [
           "AIzaSyAvsp6-tZMYNb9Cd_uJ-tQWllBxJqnHW64"
        ]

    def greet(self):
        return f"{self.name}: {random.choice(self.responses)}"

    def chat(self, user_input):
        return f"{self.name}: You said '{user_input}'. That's interesting!"

if __name__ == "__main__":
    bot = ChatBot("AI Assistant")
    print(bot.greet())
    user_input = input("You: ")
    print(bot.chat(user_input))
