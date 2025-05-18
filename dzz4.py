
class Tvaryna:
    def __init__(self, imya, vik):
        self.imya = imya
        self.vik = vik

    def govoryty(self):
        return "Ця тварина видає звуки."

    def informatsiya(self):
        return f"Ім'я: {self.imya}, Вік: {self.vik}"


class Sobaka(Tvaryna):
    def govoryty(self):
        return "Гав-гав!"


class Kit(Tvaryna):
    def govoryty(self):
        return "Мяу!!"


tvaryna1 = Sobaka("Барон", 3)
tvaryna2 = Kit("Мурка", 2)

print(tvaryna1.informatsiya())
print(tvaryna1.govoryty())

print(tvaryna2.informatsiya())
print(tvaryna2.govoryty())
