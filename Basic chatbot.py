import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')  

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well. How about you?']),
    (r'what is your name', ['I am a chatbot. You can call me ChatGPT.', 'I don\'t have a name. You can just call me Chatbot.']),
    (r'your age|how old are you', ['I don\'t have an age. I am a computer program.']),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!', 'See you later.']),
    (r'(.*)', ['That\'s interesting!', 'Tell me more...', 'I am not sure I understand.']),
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

# Begin the chat 
print("Hello! I'm a simple chatbot. You can start a conversation with me or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye! Have a great day.")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
