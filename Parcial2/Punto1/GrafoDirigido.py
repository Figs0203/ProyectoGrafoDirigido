from Punto1.Arista import Arista


class GrafoDirigido:
    def __init__(self):
        self.nodos = {}     # diccionario "HashTable"
        self.aristas = []   # lista

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
            print('-'*20)

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
