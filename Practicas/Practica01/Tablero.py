matriz = [[5, 4, 2], [3, 1, 7], ["e", 6, 8]]
fila_vacia, col_vacia = [(fila, columna) for fila in range(3) for columna in range(3) if matriz[fila][columna] == "e"][0]

def mover_arriba():
    global fila_vacia, col_vacia
    if fila_vacia > 0:
        matriz[fila_vacia][col_vacia], matriz[fila_vacia-1][col_vacia] = matriz[fila_vacia-1][col_vacia], matriz[fila_vacia][col_vacia]
        fila_vacia -= 1
        print("\n MOVEMOS HACIA ARRIBA\n")
        for fila in matriz:
            print(fila)

def mover_abajo():
    global fila_vacia, col_vacia
    if fila_vacia < 2:
        matriz[fila_vacia][col_vacia], matriz[fila_vacia+1][col_vacia] = matriz[fila_vacia+1][col_vacia], matriz[fila_vacia][col_vacia]
        fila_vacia += 1
        print("\n MOVEMOS HACIA ABAJO")
        for fila in matriz:
            print(fila)

def mover_izquierda():
    global fila_vacia, col_vacia
    if col_vacia > 0:
        matriz[fila_vacia][col_vacia], matriz[fila_vacia][col_vacia-1] = matriz[fila_vacia][col_vacia-1], matriz[fila_vacia][col_vacia]
        col_vacia -= 1
        print("\n MOVEMOS HACIA LA IZQUIERDA")
        for fila in matriz:
            print(fila)

def mover_derecha():
    global fila_vacia, col_vacia
    if col_vacia < 2:
        matriz[fila_vacia][col_vacia], matriz[fila_vacia][col_vacia+1] = matriz[fila_vacia][col_vacia+1], matriz[fila_vacia][col_vacia]
        col_vacia += 1
        print("\n MOVEMOS HACIA LA DERECHA")
        for fila in matriz:
            print(fila)

print()
print("Tablero inicial:\n")
for fila in matriz:
    print(fila)

mover_arriba()
mover_izquierda()
mover_derecha()

