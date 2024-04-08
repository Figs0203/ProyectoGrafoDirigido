from Punto1.GrafoDirigido import GrafoDirigido
from Punto1.Nodo import Nodo

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

grafo.agregar_arista(Madrid, Guadalajara, 66.6)
grafo.agregar_arista(Madrid, Segovia, 91.6)
grafo.agregar_arista(Segovia, Avila, 64.3)
grafo.agregar_arista(Madrid, Toledo, 72.5)
grafo.agregar_arista(Toledo, Segovia, 159)
grafo.agregar_arista(Segovia, Guadalajara, 153)
grafo.agregar_arista(Avila, Guadalajara, 171)


aristas = grafo.aristas

sego_gua = False
sego_gua2 = False

for arista in aristas:

    if arista.nodo_inicio == Madrid and arista.nodo_destino == Guadalajara:
        print(f"{arista}\nRecorrido total: {arista.peso}km\n")

    if arista.nodo_inicio == Madrid and arista.nodo_destino == Segovia and sego_gua == False:
        for j in aristas:
            if j.nodo_inicio == arista.nodo_destino and j.nodo_destino == Guadalajara:
                print(f"{arista} --> {j.nodo_destino}\nRecorrido total: {arista.peso + j.peso} km\n")
                sego_gua = True

    if arista.nodo_inicio == Madrid and arista.nodo_destino == Segovia and sego_gua == True:
        for j in aristas:
            if j.nodo_inicio == arista.nodo_destino and j.nodo_destino == Avila:
                for z in aristas:
                    if z.nodo_inicio == j.nodo_destino and z.nodo_destino == Guadalajara:
                        print(f"{arista} --> {j.nodo_destino} --> {z.nodo_destino}\n"
                              f"Recorrido total: {arista.peso + j.peso + z.peso} km\n")

    if arista.nodo_inicio == Madrid and arista.nodo_destino == Toledo and sego_gua2 == False:
        for j in aristas:
            if j.nodo_inicio == arista.nodo_destino and j.nodo_destino == Segovia:
                for z in aristas:
                    if z.nodo_inicio == j.nodo_destino and z.nodo_destino == Guadalajara:
                        print(f"{arista} --> {j.nodo_destino} --> {z.nodo_destino}\n"
                              f"Recorrido total: {arista.peso + j.peso+ z.peso} km\n")
                        sego_gua2 = True

    if arista.nodo_inicio == Madrid and arista.nodo_destino == Toledo and sego_gua2 == True:
        for j in aristas:
            if j.nodo_inicio == arista.nodo_destino and j.nodo_destino == Segovia:
                for z in aristas:
                    if z.nodo_inicio == j.nodo_destino and z.nodo_destino == Avila:
                        for h in aristas:
                            if h.nodo_inicio == z.nodo_destino and h.nodo_destino == Guadalajara:
                                print(f"{arista} --> {j.nodo_destino} --> {z.nodo_destino} --> {h.nodo_destino}\n"
                                      f"Recorrido total: {arista.peso + j.peso + z.peso + h.peso} km\n")
