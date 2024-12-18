class Person:
    def __init__(self, name, behaviour):
        self.name = name
        self.behaviour = behaviour

    def speak(self, speech):
        print(f"{self.name}: {speech}")

class Enemy(Person):
    def __init__(self, name, behaviour, hp, damage):
        super.__init__(name, behaviour)
        self.hp = hp
        self.damage = damage
