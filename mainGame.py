"""
Below is our medieval life game simulation.
This simulation focuses on a farming simulation and city building simulation.
The goal in this program is to efficiently manage data in terms of inventory.
As well as incorporate a smooth user interaction to the game. 
More insight into the program, its structure, legality, and related content
located in the README.md file.

Initial development on 10/3/2024 3:19 pm By RausellStudios.
"""

#Initializing pygame related modules
import sys, pygame
pygame.init()

#Importing modules to run game program
from item import Item
from inventory import Inventory

#Setting screen size (currently on adjusted to MacBook Air 2020 version)
size = width, height = 900, 710
speed = [2, 2]
black = 0, 0, 0

#Creating graphical window
screen = pygame.display.set_mode(size)

#Creating items
#Can be made into a callable function
sword = Item("Iron sword", 5)
wheat = Item("Wheat", 1)

#Creating initial inventory with capacity of 10
player_inventory = Inventory(capacity = 50)

#Adding items to inventory
#Can be made into a callable function
player_inventory.add_item(sword)

#Displaying inventory
#Can be made into a callable function based on user given command
player_inventory.display_items()

#Removing an item
#Can be made into a callable action
player_inventory.remove_item("sword")

#Showing the updated inventory
player_inventory.display_items()

#Shows the graphical display until user exits from page
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()