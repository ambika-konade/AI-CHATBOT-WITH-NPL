  import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "thx"],
    "name": ["your name", "who are you", "what's your name"],
    "age": ["how old are you", "what's your age"],
    "help": ["can you help", "i need help", "assist me"],
}

responses = {
    "greeting": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "name": "I'm a simple chatbot created using spaCy.",
    "age": "I don't have an age, but I was created recently!",
    "help": "Sure, I can help. Ask me a question.",
    "unknown": "I'm not sure how to respond to that. Can you rephrase?",
}

# Intent recognition function
def recognize_intent(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)
    
    for intent, patterns in intents.items():
        for pattern in patterns:
            if pattern in user_input:
                return intent
    return "unknown"

# Chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot:", responses["goodbye"])
            break
        intent = recognize_intent(user_input)
        print("Chatbot:", responses[intent])

if __name__ == "__main__":
    chatbot()
