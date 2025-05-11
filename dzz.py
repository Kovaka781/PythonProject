import random

class Pet:
    def __init__(self, name, species="cat"):
        self.name = name
        self.species = species
        self.energy = 100
        self.hunger = 0
        self.happiness = 50

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.energy += 10
            print(f"{self.name} поїв. Голод зменшився.")
        else:
            print(f"{self.name} не голодний.")

    def sleep(self):
        self.energy += 20
        self.hunger += 5
        print(f"{self.name} поспав. Енергія поповнена.")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.happiness += 15
            self.hunger += 10
            print(f"{self.name} пограв. Щастя збільшилося!")
        else:
            print(f"{self.name} занадто втомлений, щоб грати.")

    def status(self):
        print(f"Ім'я: {self.name} ({self.species})")
        print(f"Енергія: {self.energy}")
        print(f"Голод: {self.hunger}")
        print(f"Щастя: {self.happiness}")
        mood = self.get_mood()
        print(f"Настрій: {mood}")

    def get_mood(self):
        if self.happiness > 80:
            return "дуже щасливий(а)"
        elif self.happiness > 50:
            return "задоволений(а)"
        elif self.happiness > 30:
            return "сумний(а)"
        else:
            return "дуже сумний(а)"

my_pet = Pet("Мурчик", "cat")
my_pet.status()
my_pet.play()
my_pet.eat()
my_pet.sleep()
my_pet.status()
