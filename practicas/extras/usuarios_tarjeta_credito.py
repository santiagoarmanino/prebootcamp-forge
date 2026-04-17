class TarjetaCredito:
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = saldo_pagar

    def compra(self, monto):
        if (self.saldo_pagar + monto) <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

# actualizacion de la clase usuario _:
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        # para el bonus, usamos un diccionario
        self.tarjetas = {
            "visa": TarjetaCredito(limite_credito=5000, intereses=0.02),
            "mastercard": TarjetaCredito(limite_credito=10000, intereses=0.05)
        }

    def hacer_compra(self, monto, nombre_tarjeta="visa"):
        self.tarjetas[nombre_tarjeta].compra(monto)
        return self

    def pagar_tarjeta(self, monto, nombre_tarjeta="visa"):
        self.tarjetas[nombre_tarjeta].pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}")
        for nombre, tarjeta in self.tarjetas.items():
            print(f"Tarjeta: {nombre.upper()}")
            tarjeta.mostrar_info_tarjeta()
        return self

santi = Usuario("Santi", "santi@mail.com")
santi.hacer_compra(1500, "visa").hacer_compra(2000, "mastercard")
santi.pagar_tarjeta(500, "visa")
santi.mostrar_saldo_usuario()