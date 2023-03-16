import heapq

class Puzzle8:
    #Inicializamos el tablero 
    def __init__(self, estado_inicial, padre=None, movimiento=None, profundidad=0):
        self.estado_inicial = estado_inicial
        self.estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 'e']]
        self.heuristica_peso = 0.8
        self.padre = padre
        self.movimiento = movimiento
        self.profundidad = profundidad

    #Iteramos sobre el tablero para encontrar a nuestro agente e.
    def encontrar_vacio(self):
        for i in range(3):
            for j in range(3):
                if self.estado_inicial[i][j] == 'e':
                    return i, j

    #Verificamos que se puedan realizar movimientos validos dentro del tablero
    def movimientos_validos(self):
        #Primero encontramos la posicion actual de "e"
        i, j = self.encontrar_vacio()
        #Aqui almacenaremos los movimientos posibles a realizar
        movimientos = []
        #verificamos si es posible moverse
        if i > 0:
            movimientos.append((-1, 0))
        if i < 2:
            movimientos.append((1, 0))
        if j > 0:
            movimientos.append((0, -1))
        if j < 2:
            movimientos.append((0, 1))
        #Regresamos el arreglo con los movimientos posibles 
        return movimientos
    """ Movemos a "e" dentro del tablero, primero encontramos en que posicion está,
    calculamos la nueva posicion y guardamos el nuevo estado"""
    def mover(self, movimiento):
        #Encontramos el agente vacio
        i, j = self.encontrar_vacio()
        #Almacenamos el numero por el cual se intercambiara la posicion con el agente 
        di, dj = movimiento
        #modificamos las coordenadas para realizar el cambio de numeros con el agente
        nuevo_i, nuevo_j = i + di, j + dj
        nuevo_estado = [fila[:] for fila in self.estado_inicial]
        #Reañizamos el intercambio
        nuevo_estado[i][j], nuevo_estado[nuevo_i][nuevo_j] = nuevo_estado[nuevo_i][nuevo_j], nuevo_estado[i][j]
        #Creamos el nuevo estado, incrementamos la produnfidad y regresamos el nuevo estado.
        return Puzzle8(nuevo_estado, self, movimiento, self.profundidad + 1)

    #Verificamos si ya llegamos al estado meta
    def es_estado_final(self):
        return self.estado_inicial == self.estado_final

    """Utilizamos la distancia manhattan para estimar la cantidad de movimientos 
    para poder resolver el problema"""
    def heuristica_manhattan(self):
        distancia = 0
        for i in range(3):
            for j in range(3):
                # verifica si la casilla actual no es la casilla vacía
                if self.estado_inicial[i][j] != 'e': 
                    #guardamos la casilla en la variable valor 
                    valor = self.estado_inicial[i][j]
                    #calculamos las coordenadas donde estaria el valor actual en el estado meta del problema
                    fila_final, columna_final = (valor-1) // 3, (valor-1) % 3
                    #Actualizamos la distancia
                    distancia += abs(i - fila_final) + abs(j - columna_final)
        return distancia * self.heuristica_peso

    def costo(self):
        return self.profundidad

    """Comparamos dos estados utilizando la heuristica de manhattan y el costo de cada estado respectivamente"""
    def __lt__(self, other):
        return self.heuristica_manhattan() * self.heuristica_peso + self.costo() < other.heuristica_manhattan() * other.heuristica_peso + other.costo()

    """Implementamos A* con nuestra frontera, utilizamos una colda de prioridad"""
    def resolver(self):
        frontera = [self]
        heapq.heapify(frontera) # convierte la lista de frontera en una cola de prioridad
        visitados = set()
        while frontera:
            #obtenemos el nodo con la menor prioridad
            actual = heapq.heappop(frontera) 
            visitados.add(str(actual.estado_inicial))
            #Verificamos si el estado actual es la meta devolvemos el camino de reversa de la meta al estado inicial
            if actual.es_estado_final():
                camino = []
                while actual.padre:
                    camino.append(actual.movimiento)
                    actual = actual.padre
                camino.reverse()
                return camino
            #Generamos un nodo hijo  e insertamos en la cola de prioridad si dicho nodo no ha sido visitado
            for movimiento in actual.movimientos_validos():
                hijo = actual.mover(movimiento)
                if str(hijo.estado_inicial) not in visitados:
                    heapq.heappush(frontera, hijo) # inserta el nodo hijo en la cola de prioridad
        return None
    
"""Representamos hacia que sentido se mueve "e" """
def obtener_cadena_movimiento(movimiento):
    if movimiento == (-1, 0):
        return 'arriba'
    elif movimiento == (1, 0):
        return 'abajo'
    elif movimiento == (0, -1):
        return 'la izquierda'
    elif movimiento == (0, 1):
        return 'la derecha'
    else:
        return 'Movimiento no válido'


puzzle = Puzzle8([[5, 4, 2], [3, 1, 7], ['e', 6, 8]])
print("Estado inicial:\n")
for fila in puzzle.estado_inicial:
    print(fila)
print()
solucion = puzzle.resolver()
if solucion is None:
    print("No se encontró solución")
else:
    print("Solución encontrada:")
    actual = puzzle
    for movimiento in solucion:
        print(f'Movemos e hacia {obtener_cadena_movimiento(movimiento)}:')
        actual = actual.mover(movimiento)
        for fila in actual.estado_inicial:
            print(fila)
        print()
