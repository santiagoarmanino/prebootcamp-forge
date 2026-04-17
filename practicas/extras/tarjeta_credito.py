class TarjetaCredito:
    todas_las_tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = saldo_pagar
        #
        TarjetaCredito.todas_las_tarjetas.append(self)

    def compra(self, monto):
        if (self.saldo_pagar + monto) <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self # Retornamos self para permitir encadenamiento

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += (self.saldo_pagar * self.intereses)
        return self

    @classmethod
    def imprimir_todas_las_tarjetas(cls):
        print("--- Listado General de Tarjetas ---")
        for tarjeta in cls.todas_las_tarjetas:
            tarjeta.mostrar_info_tarjeta()

visa_santi = TarjetaCredito(5000, 0.02)
master_david = TarjetaCredito(10000, 0.05, 100)
amex_lucas = TarjetaCredito(1500, 0.01)

visa_santi.compra(1500).compra(500).pago(200).cobrar_interes().mostrar_info_tarjeta()
master_david.compra(1000).compra(2000).compra(500).pago(300).pago(200).cobrar_interes().mostrar_info_tarjeta()
amex_lucas.compra(400).compra(400).compra(400).compra(400).compra(400).mostrar_info_tarjeta()

TarjetaCredito.imprimir_todas_las_tarjetas()