from Punto2.Arista import Arista
from Punto2.Bus import Bus
import random


class GrafoDirigido:
    def __init__(self):
        self.nodos = {}  # diccionario "HashTable"
        self.aristas = []  # lista

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

            else:
                usados.append(arista.nodo_destino.nombre)
                probabilidad = random.random()  # Generar un número aleatorio para la probabilidad
                if probabilidad > 0.5:  # Solo agregar pasajeros si la probabilidad es mayor al 30%
                    nuevas = random.randint(1, 10)
                    for ari in self.aristas:
                        if ari.nodo_destino.nombre == arista.nodo_destino.nombre:
                            ari.personas += nuevas
                    print(f"{nuevas} personas nuevas añadidas en {arista.nodo_destino.nombre}\n")

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

    def terminar(self):
        aristas_con_personas = []
        for arista in self.aristas:
            if arista.personas > 0:
                aristas_con_personas.append(arista)

        if len(aristas_con_personas) == 0:
            print("El sistema ha terminado exitosamente")
            quit()

    def a_guadalajara(self):

        for arista in self.aristas:
            if arista.nodo_inicio.nombre == "Toledo" and arista.nodo_inicio.tiene_bus:
                self.avanzar_bus(arista, False)
                for ari in self.aristas:
                    if ari.nodo_inicio.tiene_bus and ari.nodo_destino.nombre == "Guadalajara":
                        self.avanzar_bus(ari, False)
                        print("El bus ha llegado a Guadalajara\n")
                        self.terminar()
                        self.sortear_personas()
                        self.ejecutar()

        for arista in self.aristas:
            if arista.nodo_inicio.tiene_bus and arista.nodo_destino.nombre == "Guadalajara":
                self.avanzar_bus(arista, False)
                print("El bus ha llegado a Guadalajara\n")
                self.terminar()
                self.sortear_personas()
                self.ejecutar()

    def ejecutar(self):
        ejecutando = True
        bus = self.agregar_bus()
        print("-" * 175)
        print(f"Enviando bus número {bus.buses_enviados}\n")
        while ejecutando:

            aristas_ordenadas = sorted(filter(lambda x: x.personas != 0, self.aristas), key=lambda x: x.personas)

            if len(aristas_ordenadas) == 0:
                self.terminar()

            if aristas_ordenadas[0].nodo_destino.nombre == "Toledo":
                for ari in self.aristas:
                    if ari.nodo_inicio.tiene_bus and ari.nodo_destino.nombre == "Toledo":
                        arista_seleccionada = ari
                        self.recoger(arista_seleccionada, bus)

            elif aristas_ordenadas[0].nodo_destino.nombre == "Segovia":
                for ari in self.aristas:
                    if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Toledo"
                            and ari.nodo_destino.nombre == "Segovia"
                            or ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Madrid"
                            and ari.nodo_destino.nombre == "Segovia"):
                        arista_seleccionada = ari
                        self.recoger(arista_seleccionada, bus)

                    if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Ávila"
                            and ari.nodo_destino.nombre == "Madrid"):
                        self.avanzar_bus(ari, False)

            elif aristas_ordenadas[0].nodo_destino.nombre == "Ávila":
                for ari in self.aristas:
                    if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Segovia"
                            and ari.nodo_destino.nombre == "Ávila"):
                        arista_seleccionada = ari
                        self.recoger(arista_seleccionada, bus)

                    if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Madrid"
                            and ari.nodo_destino.nombre == "Segovia"):
                        self.avanzar_bus(ari, False)

                    if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Toledo"
                            and ari.nodo_destino.nombre == "Segovia"):
                        self.avanzar_bus(ari, False)

            elif aristas_ordenadas[0].nodo_destino.nombre == "Madrid":
                if bus.pasajeros == 0:
                    for ari in self.aristas:
                        if ari.nodo_destino.nombre == "Madrid":
                            arista_seleccionada = ari
                            self.recoger(arista_seleccionada, bus)

                else:
                    for ari in self.aristas:
                        if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Ávila"
                                and ari.nodo_destino.nombre == "Madrid"):
                            arista_seleccionada = ari
                            self.recoger(arista_seleccionada, bus)

                        if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Segovia"
                                and ari.nodo_destino.nombre == "Ávila"):
                            self.avanzar_bus(ari, False)

                        if (ari.nodo_inicio.tiene_bus and ari.nodo_inicio.nombre == "Toledo"
                                and ari.nodo_destino.nombre == "Segovia"):
                            self.avanzar_bus(ari, False)

    def recoger(self, arista_seleccionada, bus):
        parada = arista_seleccionada.personas

        if (parada + bus.pasajeros) < 15:
            self.avanzar_bus(arista_seleccionada, True)
            bus.pasajeros += parada
            print(f"Se recogieron {parada} pasajeros en {arista_seleccionada.nodo_destino.nombre}\n"
                  f"{bus.pasajeros} pasajeros actualmente en el bus\n")

        elif (parada + bus.pasajeros) == 15:
            self.avanzar_bus(arista_seleccionada, True)
            bus.pasajeros += parada
            print(f"Se recogieron {parada} pasajeros en {arista_seleccionada.nodo_destino.nombre}\n"
                  f"{bus.pasajeros} pasajeros actualmente en el bus\n")
            self.a_guadalajara()

        elif (parada + bus.pasajeros) > 15:
            exceso = (parada + bus.pasajeros) - 15
            total = parada - exceso
            self.avanzar_bus(arista_seleccionada, False)
            arista_seleccionada.personas = exceso
            bus.pasajeros += total
            print(f"Se recogieron {total} y se dejaron {exceso} pasajeros en "
                  f"{arista_seleccionada.nodo_destino.nombre}\n"
                  f"{bus.pasajeros} pasajeros actualmente en el bus\n")
            self.a_guadalajara()
