#This file contains the item class and logic related to item usage (general)
class Item:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} (Size: {self.size})"