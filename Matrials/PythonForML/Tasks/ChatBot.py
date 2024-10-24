import random

class ChatBot:
    def __init__(self):
        self.responses = {
            "hello": ["welcome", "hello how are you", "hi there!"],
            "how are you": ["I'm fine", "I'm good, what about you?", "I am fine, what about you?"],
            "goodbye": ["goodbye", "thanks", "see you later"],
            "default": ["I'm sorry, I did not understand"]
        }

    def get_response(self, user_input):
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def start(self):
        print("chatbot: Hello! How can I help you?")
        while True:
            user_input = input("User: ").lower()
            response = self.get_response(user_input)
            print("chatbot:", response)

            if user_input == "goodbye":
                break


chatbot = ChatBot()
chatbot.start()
