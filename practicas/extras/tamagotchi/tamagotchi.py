class Tamagotchi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 100

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        return self

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        return self

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        return self

class Babytchi(Tamagotchi):

    def comer(self):
        super().comer() 
        self.salud += 10
        print(f"{self.nombre} comió")
        return self

    def jugar(self):
        super().jugar()
        self.salud -= 10
        print(f"{self.nombre} jugó de más.")
        return self

class Mametchi(Tamagotchi):
    def hacer_deporte(self):
        self.salud += 15
        self.felicidad += 15
        print(f"{self.nombre} entrenó bien")
        return self

class Kuchipatchi(Tamagotchi):
    def comer(self):
        self.salud += 5
        self.felicidad += 20 
        print(f"{self.nombre} comió.")
        return self

class Gozarutchi(Tamagotchi):
    def entrenamiento_ninja(self):
        self.salud += 25
        self.felicidad += 5
        print(f"{self.nombre} entrenó tecnicas especiales.")
        return self