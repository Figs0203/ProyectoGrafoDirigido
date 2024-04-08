class Nodo:
    def __init__(self, nombre, latitud, longitud, altura):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altura = altura


    def __str__(self):
        return f'Ciudad: {self.nombre}'