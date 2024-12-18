class Player():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.health = 100
        self.inventory_max_weight = 15000
        self.inventory_weight = []
        self.inventory = []

    def calculate_inventory_size(self):
        sum = 0
        for i in self.inventory_weight:
            sum += i
        return sum

    def pick_up_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
            self.inventory_weight.append(item_instance.weight)
        else:
            print("Your inventory is full. You can't pick this item up.")

    def use_medicine(self, item_instance):
        if item_instance.type.lower() == "medicine":
            self.health += item_instance.heal
        
    def fight(self, enemy_instance):
        pass

    def npc_speak(self, person_instance):
        while True:
            choice = input("Would you like to speak to this person?")
            if choice.lower == "yes":
                
            if choice.lower == "no":
                print(f"You walked away from {person_instance.name}")
            else: 
                print("That is not an option.")