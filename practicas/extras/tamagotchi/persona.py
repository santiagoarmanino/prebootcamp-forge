from tamagotchi import Babytchi, Mametchi, Gozarutchi

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
        return self

    def darle_comida(self):
        self.tamagotchi.comer()
        return self

bebe_proweb = Babytchi("Chiquitín", "Blanco")
santi = Persona("Santi", "Gomez", bebe_proweb)

print("prueba de babytchi")
santi.darle_comida()
santi.jugar_con_tamagotchi()

ninja_david = Gozarutchi("Ninja", "Negro")
david = Persona("David", "Puente", ninja_david)

print("\n-prueba del ninja")
ninja_david.entrenamiento_ninja()