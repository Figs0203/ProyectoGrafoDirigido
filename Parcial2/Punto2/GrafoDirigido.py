from Punto2.Arista import Arista
from Punto2.Bus import Bus
import random


class GrafoDirigido:
    def __init__(self):
        self.nodos = {}  # diccionario "HashTable"
        self.aristas = []  # lista
        self.buses = []  # lista
        self.lista = []  # lista

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

    def agregar_bus(self):
        bus = Bus()
        self.buses.append(bus)
        for arista in self.aristas:
            if arista.nodo_inicio.nombre == "Madrid":
                arista.nodo_inicio.tiene_bus = True
        return bus

    def asignar_personas(self):
        mad = int(input("¿Cuantas personas se encuentran en Madrid? "))
        seg = int(input("¿Cuantas personas se encuentran en Segovia? "))
        avi = int(input("¿Cuantas personas se encuentran en Ávila? "))
        tol = int(input("¿Cuantas personas se encuentran en Toledo? "))

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

            elif arista.personas == 0:
                continue

            else:
                usados.append(arista.nodo_destino.nombre)
                probabilidad = random.randint(0, 100)  # Generar un número aleatorio para la probabilidad
                if probabilidad > 30:  # Solo agregar pasajeros si la probabilidad es mayor al 30%
                    nuevas = random.randint(0, 15)
                    for ari in self.aristas:
                        if ari.nodo_destino.nombre == arista.nodo_destino.nombre:
                            ari.personas += nuevas
                    print(f"{nuevas} personas nuevas añadidas en {arista.nodo_destino.nombre}\n")

    def final(self):
        aristas_gente = []
        for ari in self.aristas:
            if ari.personas > 0:
                aristas_gente.append(ari)

        if len(aristas_gente) == 0:
            return True
        else:
            return False

    def a_guadalajara(self, bus):
        for arista in self.aristas:
            if (arista.nodo_inicio.nombre == "Toledo" and arista.nodo_destino.nombre == "Segovia"
                    and arista.nodo_inicio.tiene_bus == True):
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
                        bus.pasajeros = 0
                        print("El bus ha llegado a Guadalajara\n")
                        if self.final():
                            quit()
                        else:
                            self.sortear_personas()

            elif arista.nodo_inicio.tiene_bus and arista.nodo_destino.nombre == "Guadalajara":
                for ari in self.aristas:
                    if ari.nodo_inicio == arista.nodo_inicio:
                        ari.nodo_inicio.tiene_bus = False
                for ari in self.aristas:
                    if ari.nodo_destino == arista.nodo_destino:
                        ari.nodo_destino.tiene_bus = True
                bus.pasajeros = 0
                print("El bus ha llegado a Guadalajara\n")
                if self.final():
                    quit()
                else:
                    self.sortear_personas()

        return False

    def avanzar_bus(self, arista, boole):
        if boole:
            for ari in self.aristas:
                if ari.nodo_inicio == arista.nodo_inicio:
                    ari.nodo_inicio.tiene_bus = False
            for ari in self.aristas:
                if ari.nodo_destino == arista.nodo_destino:
                    ari.nodo_destino.tiene_bus = True
                    ari.personas = 0

        else:
            for ari in self.aristas:
                if ari.nodo_inicio == arista.nodo_inicio:
                    ari.nodo_inicio.tiene_bus = False
            for ari in self.aristas:
                if ari.nodo_destino == arista.nodo_destino:
                    ari.nodo_destino.tiene_bus = True

    def recoger_avila(self, bus):
        for arista in self.aristas:
            if arista.nodo_inicio.tiene_bus == True and arista.nodo_destino.nombre == "Segovia":
                self.avanzar_bus(arista, False)
                for i in self.aristas:
                    if i.nodo_destino.nombre == "Ávila":
                        parada = i.personas
                        if bus.pasajeros + parada < 15:
                            self.avanzar_bus(i, True)
                            bus.pasajeros += parada
                            print(
                                f"{parada} personas recogidas en {i.nodo_destino.nombre}\n"
                                f"{bus.pasajeros} personas actualmente en el bus\n")
                            return bus.pasajeros

                        elif bus.pasajeros + parada == 15:
                            self.avanzar_bus(i, True)
                            bus.pasajeros += parada
                            print(
                                f"{parada} personas recogidas en {i.nodo_destino.nombre}\n"
                                f"{bus.pasajeros} personas actualmente en el bus\n")
                            self.a_guadalajara(bus)

                        else:
                            exceso = bus.pasajeros + i.personas - bus.maximo
                            parada = i.personas - exceso
                            bus.pasajeros += parada
                            for ari in self.aristas:
                                if ari.nodo_inicio == i.nodo_inicio:
                                    ari.nodo_inicio.tiene_bus = False
                            for ari in self.aristas:
                                if ari.nodo_destino == i.nodo_destino:
                                    ari.nodo_destino.tiene_bus = True
                                    ari.personas = exceso

                            print(f"Se recogieron {parada} y se dejaron {exceso} personas en"
                                  f" {i.nodo_destino.nombre}\n")
                            self.a_guadalajara(bus)

    def recoger_pasajeros(self):
        a = True
        while a:
            b = True
            bus = self.agregar_bus()  # Se crea un nuevo objeto Bus en cada iteración del bucle
            print(f"Enviando bus número {bus.buses_enviados}\n")

            while b:
                aristas_disponibles = []
                aristas_sin_gua = []
                for i in self.aristas:
                    if i.nodo_destino.nombre == "Guadalajara":
                        continue
                    else:
                        aristas_sin_gua.append(i)
                menor_abs = min(aristas_sin_gua, key=lambda x: x.personas)
                mayor_abs = max(aristas_sin_gua, key=lambda x: x.personas)
                cont = 0
                for arista in self.aristas:

                    if arista.nodo_destino.nombre == "Madrid" and arista.personas > 0:
                        aristas_disponibles.append(arista)
                    cont += 1

                    if (arista.nodo_inicio.tiene_bus and arista.nodo_destino.nombre != "Guadalajara" and
                            arista.personas > 0):
                        aristas_disponibles.append(arista)

                cont = 0
                if len(aristas_disponibles) == 0 and mayor_abs.personas == 0:
                    self.a_guadalajara(bus)

                else:
                    if len(aristas_disponibles) > 0:
                        arista_seleccionada = min(aristas_disponibles, key=lambda x: x.personas)
                    else:
                        if mayor_abs.personas == 0:
                            self.a_guadalajara(bus)
                        else:
                            self.recoger_avila(bus)

                if menor_abs.personas != 0 and menor_abs.personas < arista_seleccionada.personas and arista:
                    a = self.recoger_avila(bus)
                    bus.pasajeros = a

                elif bus.pasajeros + arista_seleccionada.personas == bus.maximo:
                    parada = arista_seleccionada.personas
                    bus.pasajeros += parada
                    self.avanzar_bus(arista_seleccionada, True)

                    print(
                        f"{parada} personas recogidas en {arista_seleccionada.nodo_destino.nombre}\n"
                        f"{bus.pasajeros} personas actualmente en el bus\n")
                    arista_seleccionada.personas = 0
                    self.a_guadalajara(bus)

                elif bus.pasajeros + arista_seleccionada.personas < bus.maximo:
                    parada = arista_seleccionada.personas
                    self.avanzar_bus(arista_seleccionada, True)
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
                    bus.pasajeros = 0
                    self.a_guadalajara(bus)

        print("El sistema ha terminado exitosamente.")