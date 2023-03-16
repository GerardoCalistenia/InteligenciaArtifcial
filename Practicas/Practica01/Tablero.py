import heapq

class Puzzle8:
    def __init__(self, estado_inicial, padre=None, movimiento=None, profundidad=0):
        self.estado_inicial = estado_inicial
        self.estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 'e']]
        self.heuristica_peso = 0.8
        self.padre = padre
        self.movimiento = movimiento
        self.profundidad = profundidad

    def encontrar_vacio(self):
        for i in range(3):
            for j in range(3):
                if self.estado_inicial[i][j] == 'e':
                    return i, j

    def movimientos_validos(self):
        i, j = self.encontrar_vacio()
        movimientos = []
        if i > 0:
            movimientos.append((-1, 0))
        if i < 2:
            movimientos.append((1, 0))
        if j > 0:
            movimientos.append((0, -1))
        if j < 2:
            movimientos.append((0, 1))
        return movimientos

    def mover(self, movimiento):
        i, j = self.encontrar_vacio()
        di, dj = movimiento
        nuevo_i, nuevo_j = i + di, j + dj
        nuevo_estado = [fila[:] for fila in self.estado_inicial]
        nuevo_estado[i][j], nuevo_estado[nuevo_i][nuevo_j] = nuevo_estado[nuevo_i][nuevo_j], nuevo_estado[i][j]
        return Puzzle8(nuevo_estado, self, movimiento, self.profundidad + 1)

    def es_estado_final(self):
        return self.estado_inicial == self.estado_final

    def heuristica_manhattan(self):
        distancia = 0
        for i in range(3):
            for j in range(3):
                if self.estado_inicial[i][j] != 'e': # verifica si la casilla actual no es la casilla vacía
                    valor = self.estado_inicial[i][j]
                    fila_final, columna_final = (valor-1) // 3, (valor-1) % 3
                    distancia += abs(i - fila_final) + abs(j - columna_final)
        return distancia * self.heuristica_peso

    def costo(self):
        return self.profundidad

    def __lt__(self, other):
        return self.heuristica_manhattan() * self.heuristica_peso + self.costo() < other.heuristica_manhattan() * other.heuristica_peso + other.costo()


    def resolver(self):
        frontera = [self]
        heapq.heapify(frontera) # convierte la lista de frontera en una cola de prioridad
        visitados = set()
        while frontera:
            actual = heapq.heappop(frontera) # obtiene el nodo con la menor prioridad
            visitados.add(str(actual.estado_inicial))
            if actual.es_estado_final():
                camino = []
                while actual.padre:
                    camino.append(actual.movimiento)
                    actual = actual.padre
                camino.reverse()
                return camino
            for movimiento in actual.movimientos_validos():
                hijo = actual.mover(movimiento)
                if str(hijo.estado_inicial) not in visitados:
                    heapq.heappush(frontera, hijo) # inserta el nodo hijo en la cola de prioridad
        return None

def obtener_cadena_movimiento(movimiento):
    if movimiento == (-1, 0):
        return 'Arriba'
    elif movimiento == (1, 0):
        return 'Abajo'
    elif movimiento == (0, -1):
        return 'Izquierda'
    elif movimiento == (0, 1):
        return 'Derecha'
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
        print(f'Movimiento {obtener_cadena_movimiento(movimiento)}:')
        actual = actual.mover(movimiento)
        for fila in actual.estado_inicial:
            print(fila)
        print()
