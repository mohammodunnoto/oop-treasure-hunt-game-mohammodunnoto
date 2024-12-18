import termcolor
from termcolor import colored, cprint
import pyfiglet
class Item():
    def __init__(self, name, description, rarity, rarity_colour, weight):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.rarity_colour = rarity_colour
        self.weight = weight

    def get_details(self):
        cprint(f"{self.name}", "self.rarity_colour", attrs=["bold"])
        print(f"""
{self.description}
{self.weight}
""")
        cprint(f"{self.rarity}", "self.rarity_colour")
    
class Melee(Item):
    def __init__(self, name, description, rarity, rarity_colour, weight, damage, item_type):
        super.__init__(name, description, rarity, rarity_colour, weight)
        self.damage = damage
        self.item_type = item_type
    
    def get_details(self):
        cprint(f"{self.name}", "self.rarity_colour", attrs=["bold"])
        print(f"""
{self.description}
{self.weight}
""")
        print("Deals ") + cprint(f"{self.damage}", "red", attrs=["bold"]) + print(" damage.")
        cprint(f"{self.rarity} {self.item_type}", "self.rarity_colour")

class Medicine(Item):
    def __init__(self, name, description, rarity, rarity_colour, weight, item_type, heal):
        super.__init__(name, description, rarity, rarity_colour, weight)
        self.item_type = item_type
        self.heal = heal
    
    def get_details(self):
        cprint(f"{self.name}", "self.rarity_colour", attrs=["bold"])
        print(f"""
{self.description}
{self.weight}
""")
        print("Heals ") + cprint(f"{self.heal}", "magenta", attrs=["bold"]) + print(" health.")
        cprint(f"{self.rarity} {self.item_type}", "self.rarity_colour")

