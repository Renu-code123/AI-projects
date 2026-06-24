#1. Installing Necessary Libraries
pip install nltk

#2. Importing Required Libraries
import nltk
import re
from nltk.chat.util import Chat, reflections

#3. Downloading NLTK Datasets
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

##4. Defining Patterns and Responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?",
                       "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name?", ["I am your friendly chatbot!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    [r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?",
               "Could you please elaborate?"]]
]

##5. Defining the Chatbot Class
class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)

##6. Interacting with the Chatbot
def chat_with_bot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

#7. Initializing the Chatbot
chatbot = RuleBasedChatbot(pairs)
chat_with_bot()

#




