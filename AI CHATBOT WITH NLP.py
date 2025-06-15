import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK. You can call me Chatty!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright", "Don't worry about it"]
    ],
    [
        r"i need (.*)",
        ["Why do you need %1?", "Would it really help you to get %1?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that.", "Can you please rephrase?", "Tell me more."]
    ]
]

def chatbot():
    print("Hi! I'm Chatty. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
