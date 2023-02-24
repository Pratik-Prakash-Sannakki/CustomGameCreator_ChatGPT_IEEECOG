# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:38:49 2023

@author: sweta
"""

import time

# Define a function for printing text with a delay between characters
def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Define the starting location and available actions
location = "You find yourself in a dark room with a door to your left and a door to your right."
actions = ["left", "right"]

# Define the possible outcomes for each action
outcomes = {
    "left": {
        "text": "You open the door to your left and step through...",
        "location": "You emerge into a beautiful garden with a shimmering pond in the center.",
        "actions": ["jump in the pond", "explore the garden"]
    },
    "right": {
        "text": "You open the door to your right and step through...",
        "location": "You find yourself in a musty old library, filled with dusty books and ancient artifacts.",
        "actions": ["read a book", "examine an artifact"]
    },
    "jump in the pond": {
        "text": "You dive into the pond and find yourself surrounded by shimmering fish.",
        "location": "You're back in the garden.",
        "actions": ["explore the garden"]
    },
    "explore the garden": {
        "text": "You wander around the garden, admiring the colorful flowers and sculptures.",
        "location": "You're back in the garden.",
        "actions": ["jump in the pond", "explore the garden"]
    },
    "read a book": {
        "text": "You pick up a dusty old tome and start reading...",
        "location": "You're back in the library.",
        "actions": ["read another book", "examine an artifact"]
    },
    "examine an artifact": {
        "text": "You find a strange artifact that emits a faint glow.",
        "location": "You're back in the library.",
        "actions": ["read a book", "examine another artifact"]
    },
    "examine another artifact": {
        "text": "You discover an ancient sword that seems to pulse with power.",
        "location": "You're back in the library.",
        "actions": ["read a book", "examine an artifact"]
    }
}

# Start the game loop
while True:
    # Print the current location and available actions
    print_with_delay(location)
    print_with_delay("You can go " + " or ".join(actions) + ".")

    # Ask the player for their choice of action
    choice = input("> ").lower()

    # Check if the player's choice is valid
    if choice not in actions:
        print_with_delay("Sorry, I don't understand.")
        continue

    # Print the outcome for the player's choice of action
    print_with_delay(outcomes[choice]["text"])
    location = outcomes[choice]["location"]
    actions = outcomes[choice]["actions"]
