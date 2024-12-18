import random
class Place():
    def __init__(self, name, size, locked=False):
        self.name = name
        self.size = size
        self.locked = locked
        self.next_places = []
        self.items = []
        self.enemies = []

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.items.append(item_instance)
    
    def add_enemies(self, enemy_instance):
        self.enemies.apped(enemy_instance)

    def show_next_places(self):
        print("From here you can go to thse places: ")
        for place in self.next_places:
            print(place.name)
    
    def explore(self):
        chance = random.randint(1,5)