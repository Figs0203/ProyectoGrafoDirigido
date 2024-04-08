from Punto2.Arista import Arista
from Punto2.Bus import Bus
import random


class GrafoDirigido:
    def __init__(self):
        self.nodos = {}  # diccionario "HashTable"
        self.aristas = []  # lista
        self.buses = []  # lista
        self.lista = []   # lista

    def agregar_nodo(self, nodo):
        self.nodos[nodo.nombre] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino, peso):
        if nodo_inicio.nombre in self.nodos and nodo_destino.nombre in self.nodos:
            arista = Arista(nodo_inicio, nodo_destino, peso)
            self.aristas.append(arista)

    def mostrar_grafo(self):
        for arista in self.aristas:
            print(f"{arista}")

    def encontrar_camino(self, inicio_nombre, destino_nombre, camino_actual=None):
        inicio_nombre = inicio_nombre.strip().capitalize()
        destino_nombre = destino_nombre.strip().capitalize()
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.nodos.get(inicio_nombre)
        destino = self.nodos.get(destino_nombre)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            self.mostrar_camino(camino_actual)
            return
        for arista in self.aristas:
            if arista.nodo_inicio == inicio and arista.nodo_destino not in camino_actual:
                self.encontrar_camino(arista.nodo_destino.nombre, destino_nombre, camino_actual[:])

    def mostrar_camino(self, camino):
        if camino:
            print("\nCAMINO ENCONTRADO:")
            costo_total = 0
            for i in range(len(camino) - 1):
                arista = self.buscar_arista(camino[i].nombre, camino[i + 1].nombre)
                print(f"{arista.nodo_inicio.nombre} -> {arista.nodo_destino.nombre} (Peso: {arista.peso})")
                costo_total += arista.peso
            print(f"Costo total del camino: [{costo_total} Km]\n")
            print('-' * 20)

    def buscar_arista(self, inicio_nombre, destino_nombre):
        for arista in self.aristas:
            if arista.nodo_inicio.nombre == inicio_nombre and arista.nodo_destino.nombre == destino_nombre:
                return arista

    def eliminar_nodo(self, nodo):
        if nodo in self.nodos.keys():
            self.nodos.pop(nodo)
            print(f"El nodo {nodo} ha sido exterminado.")
            queu = []
            for i in self.aristas:
                if i.nodo_inicio == nodo or i.nodo_destino == nodo:
                    queu.append(i)
                for j in queu:
                    self.aristas.remove(j)

        else:
            return "Esta mondá no existe."

    """def asignar_personas(self):
        mad = int(input("¿Cuantas personas se encuentran en Madrid?"))
        seg = int(input("¿Cuantas personas se encuentran en Segovia?"))
        avi = int(input("¿Cuantas personas se encuentran en Ávila?"))
        tol = int(input("¿Cuantas personas se encuentran en Toledo?"))

        for arist in self.aristas:
            if arist.nodo_destino.nombre == "Madrid":
                arist.personas = mad
            elif arist.nodo_destino.nombre == "Segovia":
                arist.personas = seg
            elif arist.nodo_destino.nombre == "Ávila":
                arist.personas = avi
            elif arist.nodo_destino.nombre == "Toledo":
                arist.personas = tol"""

    def agregar_bus(self):
        bus = Bus()
        self.buses.append(bus)
        for arista in self.aristas:
            if arista.nodo_inicio.nombre == "Madrid":
                arista.nodo_inicio.tiene_bus = True
        return bus

    def asignar_personas(self):
        mad = int(input("¿Cuantas personas se encuentran en Madrid?"))
        seg = int(input("¿Cuantas personas se encuentran en Segovia?"))
        avi = int(input("¿Cuantas personas se encuentran en Ávila?"))
        tol = int(input("¿Cuantas personas se encuentran en Toledo?"))

        for arist in self.aristas:
            if arist.nodo_destino.nombre == "Madrid":
                arist.personas = mad
            elif arist.nodo_destino.nombre == "Segovia":
                arist.personas = seg
            elif arist.nodo_destino.nombre == "Ávila":
                arist.personas = avi
            elif arist.nodo_destino.nombre == "Toledo":
                arist.personas = tol

    def sortear_personas(self):
        usados = ["Guadalajara"]
        for arista in self.aristas:
            if arista.nodo_destino.nombre in usados:
                continue
            else:
                usados.append(arista.nodo_destino.nombre)
                probabilidad = random.randint(0, 100)  # Generar un número aleatorio para la probabilidad
                if probabilidad > 30:  # Solo agregar pasajeros si la probabilidad es mayor al 30%
                    arista.personas = random.randint(0, 15)
                    print(f"{arista.personas} añadidas en {arista.nodo_destino.nombre}")

    def revisar_personas(self):
        personas = False
        for arista in self.aristas:
            if arista.personas > 0:
                personas = True
        return personas

    """def a_guadalajara(self):
        for arista in self.aristas:
            if arista.nodo_inicio.nombre == "Toledo" and arista.nodo_destino.nombre == "Segovia":
                arista.nodo_destino.tiene_bus = True
                arista.nodo_inicio.tiene_bus = False
                for i in self.aristas:
                    if i.nodo_inicio.nombre == "Segovia" and i.nodo_destino.nombre == "Guadalajara":
                        i.nodo_destino.tiene_bus = True
                        i.nodo_inicio.tiene_bus = False
                        return True

            if arista.nodo_inicio.nombre != "Toledo" and arista.nodo_inicio.tiene_bus:
                for j in self.aristas:
                    if j.nodo_inicio.nombre == arista.nodo_inicio.nombre and j.nodo_destino.nombre == "Guadalajara":
                        j.nodo_destino.tiene_bus = True
                        j.nodo_inicio.tiene_bus = False
                        if not self.revisar_personas():
                            return False
                        else:
                            self.sortear_personas()
                            return True"""

    def a_guadalajara(self):
        for arista in self.aristas:
            if arista.nodo_inicio.nombre == "Toledo" and arista.nodo_destino.nombre == "Segovia":
                for ari in self.aristas:
                    if ari.nodo_inicio == arista.nodo_inicio:
                        ari.nodo_inicio.tiene_bus = False
                for ari in self.aristas:
                    if ari.nodo_destino == arista.nodo_destino:
                        ari.nodo_destino.tiene_bus = True

                for i in self.aristas:
                    if i.nodo_inicio.nombre == "Segovia" and i.nodo_destino.nombre == "Guadalajara":
                        for ari in self.aristas:
                            if ari.nodo_inicio == i.nodo_inicio:
                                ari.nodo_inicio.tiene_bus = False
                        for ari in self.aristas:
                            if ari.nodo_destino == i.nodo_destino:
                                ari.nodo_destino.tiene_bus = True
                        print("El bus ha llegado a Guadalajara")
                        return True

            elif arista.nodo_inicio.tiene_bus and arista.nodo_destino.nombre == "Guadalajara":
                for ari in self.aristas:
                    if ari.nodo_inicio == arista.nodo_inicio:
                        ari.nodo_inicio.tiene_bus = False
                for ari in self.aristas:
                    if ari.nodo_destino == arista.nodo_destino:
                        ari.nodo_destino.tiene_bus = True
                return True

        return False


    def recoger_pasajeros(self):
        a = True
        while a:
            b = True
            bus = self.agregar_bus()  # Se crea un nuevo objeto Bus en cada iteración del bucle
            print(f"Enviando bus número {bus.buses_enviados}\n")
            for k in self.aristas:
                if k.nodo_inicio.nombre == "Madrid":
                    k.nodo_inicio.tiene_bus = True

            while b:
                aristas_disponibles = []
                aristas_vacias = []
                for arista in self.aristas:
                    if arista.personas == 0:
                        aristas_vacias.append(arista)
                        if len(aristas_vacias) == 9:
                            a = False

                    if (arista.nodo_inicio.tiene_bus and arista.nodo_destino.nombre != "Guadalajara" and
                            arista.personas > 0 or arista.nodo_destino.nombre == "Madrid" and arista.personas > 0):
                        aristas_disponibles.append(arista)
                if len(aristas_disponibles) == 0:
                    hola = self.a_guadalajara()
                    if hola:
                        b = False
                    else:
                        a = False

                else:
                    arista_seleccionada = min(aristas_disponibles, key=lambda x: x.personas)

                if bus.pasajeros + arista_seleccionada.personas == bus.maximo:
                    parada = arista_seleccionada.personas
                    bus.pasajeros += parada
                    for ari in self.aristas:
                        if ari.nodo_inicio == arista_seleccionada.nodo_inicio:
                            ari.nodo_inicio.tiene_bus = False
                    for ari in self.aristas:
                        if ari.nodo_destino == arista_seleccionada.nodo_destino:
                            ari.nodo_destino.tiene_bus = True
                            ari.personas = 0

                    print(
                        f"{parada} personas recogidas en {arista_seleccionada.nodo_destino.nombre}\n"
                        f"{bus.pasajeros} personas actualmente en el bus\n")
                    arista_seleccionada.personas = 0
                    hola = self.a_guadalajara()
                    if hola:
                        b = False
                    else:
                        a = False

                if bus.pasajeros + arista_seleccionada.personas < bus.maximo:
                    parada = arista_seleccionada.personas
                    for ari in self.aristas:
                        if ari.nodo_inicio == arista_seleccionada.nodo_inicio:
                            ari.nodo_inicio.tiene_bus = False
                    for ari in self.aristas:
                        if ari.nodo_destino == arista_seleccionada.nodo_destino:
                            ari.nodo_destino.tiene_bus = True
                            ari.personas = 0
                    bus.pasajeros += parada
                    print(
                        f"{parada} personas recogidas en {arista_seleccionada.nodo_destino.nombre}\n"
                        f"{bus.pasajeros} personas actualmente en el bus\n")

                else:
                    exceso = bus.pasajeros + arista_seleccionada.personas - bus.maximo
                    parada = arista_seleccionada.personas - exceso
                    bus.pasajeros += parada
                    for ari in self.aristas:
                        if ari.nodo_inicio == arista_seleccionada.nodo_inicio:
                            ari.nodo_inicio.tiene_bus = False
                    for ari in self.aristas:
                        if ari.nodo_destino == arista_seleccionada.nodo_destino:
                            ari.nodo_destino.tiene_bus = True
                            ari.personas = exceso

                    print(f"Se recogieron {parada} y se dejaron {exceso} personas en"
                          f" {arista_seleccionada.nodo_destino.nombre}\n")

                    hola = self.a_guadalajara()
                    if hola:
                        b = False
                    else:
                        a = False

        print("El sistema ha terminado exitosamente.")
