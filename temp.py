import random

class SimpleAI:
    def __init__(self):
        self.mood = "happy"

    def greet(self):
        if self.mood == "happy":
            return "Konnichiwa!"
        else:
            return "Hi there, whats the plan for today?"

    def set_mood(self, mood):
        self.mood = mood

    @staticmethod
    def emoji_response():
        emojis = ["😃", "💕", "😘", "💃", "🎉", "😂"]
        return random.choice(emojis)

    @staticmethod
    def sexy_tip():
        tips = [
            "Remember, good code is important, but not as much as keeping comments, onii-chan!",
            "It's all about the loops, and good outputs. Keep it going, just like my happiness!",
            "Functions should be short and sweet, like the idea!"
        ]
        return random.choice(tips)

def start_conversation():
    ai = SimpleAI()  # Create an instance of SimpleAI
    print(ai.greet())  # Call the greet method
    print(SimpleAI.emoji_response())  # Call the static method for emoji response
    print(SimpleAI.sexy_tip())  # Call the static method for sexy tip

# Start the conversation
start_conversation()