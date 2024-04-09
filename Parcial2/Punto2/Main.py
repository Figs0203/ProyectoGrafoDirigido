from Punto2.GrafoDirigido import GrafoDirigido
from Punto2.Nodo import Nodo

grafo = GrafoDirigido()

Madrid = Nodo("Madrid", 40.416775, -3.703790, 667)
Toledo = Nodo("Toledo", 39.858938, -4.024472, 529)
Segovia = Nodo("Segovia", 40.942903, -4.123201, 1000)
Avila = Nodo("Ávila", 40.655071, -4.701009, 1132)
Guadalajara = Nodo("Guadalajara", 40.633190, -3.163360, 37596)

grafo.agregar_nodo(Madrid)
grafo.agregar_nodo(Segovia)
grafo.agregar_nodo(Avila)
grafo.agregar_nodo(Toledo)
grafo.agregar_nodo(Guadalajara)
grafo.nodos["Madrid"].tiene_bus = True

grafo.agregar_arista(Avila, Madrid, 102)
grafo.agregar_arista(Madrid, Segovia, 91.6)
grafo.agregar_arista(Segovia, Avila, 64.3)
grafo.agregar_arista(Madrid, Toledo, 72.5)
grafo.agregar_arista(Toledo, Segovia, 159)
grafo.agregar_arista(Madrid, Guadalajara, 66.6)
grafo.agregar_arista(Segovia, Guadalajara, 153)
grafo.agregar_arista(Avila, Guadalajara, 171)
grafo.agregar_arista(Avila, Toledo, 133)
grafo.agregar_arista(Segovia, Toledo, 159)


grafo.asignar_personas()

print(f"Personas en Madrid: {grafo.aristas[0].personas}\nPersonas en Segovia: {grafo.aristas[1].personas}\n"
      f"Personas en Ávila: {grafo.aristas[2].personas}\nPersonas en Toledo: {grafo.aristas[3].personas}\n")


aristas_ordenadas = sorted(grafo.aristas, key=lambda x: x.peso)

#for arista in aristas_ordenadas:
    #print(arista)

grafo.recoger_pasajeros()
