class Nodo:
    def __init__(self, nombre, latitud, longitud, altura, tiene_bus=False):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altura = altura
        self.tiene_bus = tiene_bus

    def __str__(self):
        return f'Ciudad: {self.nombre}  (longitud:{self.longitud}, latitud:{self.latitud}, altura:{self.altura})'
