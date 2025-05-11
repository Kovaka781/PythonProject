class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
        self.happiness = 50

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.happiness += 10
            print(f"{self.name} грається і стає щасливішим.")
        else:
            print(f"{self.name} занадто втомлений(а).")

    def feed(self):
        self.energy += 20
        print(f"{self.name} поїв(ла) і має більше енергії.")

    def status(self):
        return f"{self.name} ({self.species}): Енергія = {self.energy}, Щастя = {self.happiness}"


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def adopt_pet(self, pet):
        self.pets.append(pet)
        print(f"{self.name} взяв(ла) {pet.name} ({pet.species}) під опіку.")

    def play_with_pets(self):
        for pet in self.pets:
            pet.play()

    def feed_pets(self):
        for pet in self.pets:
            pet.feed()

    def show_all_statuses(self):
        for pet in self.pets:
            print(pet.status())


owner = Owner("Олена")
cat = Pet("Мурчик", "Кіт")
dog = Pet("Барбос", "Пес")

owner.adopt_pet(cat)
owner.adopt_pet(dog)

owner.feed_pets()
owner.play_with_pets()
owner.show_all_statuses()
