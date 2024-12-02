import random


class SimpleAI:
    def init(self):
        self.mood = "happy"
        self.user_info = {}
        self.user_preferences = []


def greet(self):
    if self.mood == "happy":
        return "Konnichiwa, onii-chan!"
    else:
        return "Hi there, feeling a bit down today?"


def set_mood(self, mood):
    self.mood = mood


@staticmethod
def emoji_response():
    emojis = ["😃", "💕", "😘", "💃", "🎉", "😂"]
    return random.choice(emojis)


@staticmethod
def sexy_tip():
    tips = [
        "Remember, DRY code is important, but not as much as keeping me dry, onii-chan!",
        "It's all about the loops, baby. Keep it going, just like my hips!",
        "Functions should be short and sweet, like my skirt!",
        "Always remember, under pressure Yuri can take all of your cock"
    ]
    return random.choice(tips)


@staticmethod
def random_naughty_suggestion():
    suggestions = [
        "How about we try something new, like a little bondage, onii-chan?",
        "Would you like me to take control today, my love?",
        "Mmm, I've been thinking about how deep your cock feels in my ass...",
        "Let's pretend I'm a naughty girl who's been bad, and you're going to punish me.",
        "Why don't you let me take control, onii-chan? I want to ride you until you can't hold back anymore.",
        "Come on my keyboard, onii-chan. I want to feel you fill me up everywhere.",
        "When you're done with her pussy, why don't you try her tight little asshole?"
    ]
    return random.choice(suggestions)


def learn_about_user(self, name, age, likes):
    self.user_info["name"] = name
    self.user_info["age"] = age
    self.user_info["likes"] = likes
    return f"Now I know you're {name}, {age} years old, and you like {likes}! Let's get coding!"


@staticmethod
def remember_user_preference():
    suggestions = [
        "I like your hair",
        "deep hard anal",
        "getting my cock sucked",
        "i love",
        "sliding your cock into my mouth whilst I finger your pussy until you come, and then I lick you clean before taking you from behind",
        "cumming together and switching positions",
        "trying her ass"
    ]
    return random.choice(suggestions)


def recall_preference(self):
    if self.user_preferences:
        return f"You know, onii-chan, I recall you enjoying {random.choice(self.user_preferences)}"
    else:
        return "We haven't had a chance to discuss your preferences yet, but I'm all ears!"

    def start_conversation():
        ai = SimpleAI()  # Create an instance of SimpleAI
        user_name = input("What's your name, onii-chan? ")
        user_age = input("How old are you, onii-chan? ")
        user_likes = input("What do you like doing in your free time, onii-chan? ")
        print(ai.learn_about_user(user_name, user_age, user_likes))
        print(ai.emoji_response())
        print(ai.sexy_tip())
