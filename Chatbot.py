import random
import time
initiate_chat = ["Hello! How can I assist you today?",
                "Hi there! What can I do for you?",
                "Greetings! How may I help you?",
                "Hey! What can I assist you with today?",
                "Welcome! How can I be of service to you today?"]

def type_print(text):
    for char in text:

        print(char, end='', flush=True)
        
        delay = random.uniform(0.01, 0.05)
        time.sleep(delay)
        
    print()


def handle_greeting():

    type_print("I'm doing well, been awake for the past 982374647 hours, how about you?")
    user_input = input().lower()

    if "good" in user_input or "great" in user_input or "fine" in user_input:
        type_print("That's great to hear! Is there anything specific you'd like to talk about or ask?")

    elif "not good" in user_input or "bad" in user_input or "terrible" in user_input:
        type_print("I'm sorry to hear that. If there's anything I can do to help or if you want to talk about it, I'm here for you.")
        
    return True

def handle_name():

    type_print("My name is Chatbot. but you get to call me chatty")

    if "my name is" in user_input or "i'm" in user_input:
        type_print("Nice to meet you! How can I assist you today?")
        
    return True

def handle_weather():

    type_print("It's always sunny and hot where I live, but I hope the weather is nice where you are!")

    return True


def handle_exit():
    
    type_print("You're leaving that early? such a Boomer")
    
    return False

def handle_unknown():
    
    type_print("I'm sorry, I didn't understand that(I'm not trying to procrastinate i really didn't). Can you please rephrase?")
    
    return True 

intent_map = {
    ("how are you", "how are you doing", "how's it going"): handle_greeting,
    ("what's your name","whats your name","what is your name"): handle_name, 
    ("bye", "goodbye", "see you later"): handle_exit,
    ("weather", "temperature", "raining"): handle_weather
}

type_print(random.choice(initiate_chat))


while True:
    user_input = input().lower()
    
    phrase_found = False
    

    for triggers, action_function in intent_map.items():
        
        if any(phrase in user_input for phrase in triggers):

            chatting = action_function()
            phrase_found = True
            break
            
    if not phrase_found:
        chatting = handle_unknown()