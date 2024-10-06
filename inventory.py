#This file deals with inventory logic & the procedures behind a given action
class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.occupied_space = 0
    
    #Incorporating the logic of adding an item into the inventory
    def add_item(self, item):
        if self.occupied_space + item.size <= self.capacity:
            self.items.append(item)
            self.occupied_space += item.size
        else:
            print("Inventory full!!\n")
    
    #Incorporating the logic of removing an item into the inventory
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.occupied_space -= item.size
                break
            else:
                print("You don't have this item\n")
    
    def display_items(self):
        for item in self.items:
            print(f" - {item}")
        print(f"You have: {self.occupied_space}/{self.capacity} of space.\n")
