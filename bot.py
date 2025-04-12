import random

responses = {
    "hello": ["Hi! How are you?", "Hey, what's up?", "Hello"],
    "how are you": ["I'm good, thanks!", "Doing great, thanks for asking!", "I'm good, thanks."],
    "bye": ["Good bye!", "See you later", "Bye!"],
    "default": ["I am not understanding what you are saying."]
}

def simple_chat_bot(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])
