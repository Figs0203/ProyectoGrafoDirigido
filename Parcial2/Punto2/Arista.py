class Arista:
    def __init__(self, nodo_inicio, nodo_destino, peso, personas=0):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.peso = peso
        self.personas = personas

    def __str__(self):
        return f'{self.nodo_inicio} --> {self.nodo_destino}\nEl trayecto tiene una distancia de: {self.peso} km\n'
