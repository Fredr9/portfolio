import random
import re
import datetime

class Person:
    def __init__(self, name):
        self.name = name


class ChatBot:
    ACTIONS = {

    }

    def __init__(self, name):
        self.name = name

    def getThe_ACTIONS(self, message):
        # Make the message uppercase
        message = re.sub("[A-Za-z/]+", " ", message).lower()
        self.add_random()

        return list(filter(lambda w: w in self.ACTIONS, message.split(" ")))

    def add_random(self):
        pass

    def get_help(self):
        self.add_random()
        return list(filter(lambda a: a in self.ACTIONS.keys() and a is not None, self.ACTIONS.keys()))

    def respond(self, message):
        actions = self.getThe_ACTIONS(message)

        if len(actions) < 1:
            return self.ACTIONS[None]
        else:
            response = ""
            for action in actions:
                response += f"{self.ACTIONS[action]} "
            return response

class Hanne(ChatBot):
    Greetings = [
        "Hey there!"
        "Hi you!"
        "How nice to see you!"
        "Halloi!"
    ]

    ACTIONS = {
        None: "I have no response for that =( Try something else please!",

        'sing': "its awesome! I love to sing!",
        'test': "is cool, maybe you can teach me!",
        'box':  "thats scary, i dont want that!",
        'try': "I like to always try my best!",
        'talk': "I am always open to talk!",
        'who': "I am Hanne!"
    }

    def __init__(self):
        super().__init__('Hanne')

    def add_random_actions(self):
        self.ACTIONS.update({'greetings': random.choice(self.Greetings)})


class Jon(ChatBot):
    Greetings = [
        "Helloi"
        "Hi you!"
        "How nice to see you!"
    ]

    ACTIONS = {
        None: "I have no response for that =( Try something else please!",

        'sing': "its awesome! I love to sing!",
        'test': "is cool, maybe you can teach me!",
        'box':  "thats scary, i dont want that!",
        'try': "I like to always try my best!",
        'talk': "I am always open to talk!",
        'who': "I am Jon, the kind giant!"

    }

    def __init__(self):
        super().__init__('Jon')

    def add_random_actions(self):
        self.ACTIONS.update({'greetings': random.choice(self.Greetings)})
