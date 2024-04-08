class Bus:

    buses_enviados = 0

    def __init__(self):
        self.pasajeros = int(0)
        Bus.buses_enviados += 1
        self.maximo = 15

    def __str__(self):
        return f"Bus número {Bus.buses_enviados}\n{self.pasajeros} a bordo"

