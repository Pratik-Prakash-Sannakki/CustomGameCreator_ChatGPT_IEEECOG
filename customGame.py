# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:51 2023

@author: sweta
"""

import pygame
import requests
import json
import openai
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Your OpenAI API key
#with open("C:\Users\Pratik's Predator\Documents\CustomGameCreator_ChatGPT_IEEECOG/apikey.txt") as f:
    #openai_api_key = f.read().strip()
openai_api_key ="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"

# Ask the user for the type of game they want to create
game_type = input("Enter the type of game you want to create (e.g. platformer, shooter, puzzle): ")

# Generate a game description using OpenAI's GPT-3
response = requests.post(
    "https://api.openai.com/v1/engines/text-davinci-002/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    },
    json={
        "prompt": f"genearte python code for {game_type}",
        "max_tokens": 100,
        "n": 1,
        "temperature": 0.5,
    },
)

# Extract the game description from the API response
#game_description = response.json()["choices"][0]["text"].strip()
print(response.json())
game_description = response.json()["choices"][0]["text"]

# Print the generated game description
print("Game description:")
print(game_description)

# Display the game description on the screen
font = pygame.font.Font(None, 36)
text = font.render(game_description, True, (255, 255, 255))
screen.blit(text, (100, 100))
pygame.display.update()

# Wait for a keypress
pygame.event.wait()

# Quit Pygame
pygame.quit()
