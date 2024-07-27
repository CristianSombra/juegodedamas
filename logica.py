#Ficha seleccionada
selection = None
turn = 'red' #Turno inicial

board = [
    ['.', 'r', '.', 'r', '.', 'r', '.', 'r'],
    ['r', '.', 'r', '.', 'r', '.', 'r', '.'],
    ['.', 'r', '.', 'r', '.', 'r', '.', 'r'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
    ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
    ['b', '.', 'b', '.', 'b', '.', 'b', '.']
]

#Verificación del movimiento
def valid_move(start, end):
    sx, sy = start
    ex, ey = end
    if not (0 <= ex < 8 and 0 <= ey < 8):
        return False
    if board[ey][ex] != '.':
        return False
    #Solo movimientos diagonales simples por ahora
    if abs(sx - ex) == 1 and abs(sy - ey) == 1:
        return  True
    return False

def move_chip(start, end):
    sx, sy = start
    ex, ey = end
    board[ey][ex] = board[sy][sx]
    board[sy][sx] = '.'


#Manejo del evento click
def click_event(event, canvas):
    global selection, turn
    x, y = event.x // 50, event.y // 50

    if selection is None:
        #Seleccionar una ficha
        if board[y][x] in ['r', 'b'] and board[y][x] == turn[0]:
            selection = (x, y)
            print(f"Ficha seleccionada en: {selection}")
    else:
        #Mover la ficha seleccionada
        if valid_move(selection, (x, y)):
            move_chip(selection, (x, y))
            draw_board(canvas)
            draw_chip(canvas)
            selection = None
            turn = 'r' if turn == 'b' else 'b'
            print(f"Turno de: {'rojas' if turn == 'r' else 'negras'}")
        else:
            print("Movimiento no válido")
            selection = None

def draw_board(canvas):
    canvas.delete("all")
    for i in range(8):
        for j in range(8):
            #Coordenadas superiores izquierdas del rectángulo
            x1, y1 = i * 50, j * 50
            #Coordenadas inferiores derechas del rectángulo
            x2, y2 = x1 + 50, y1 + 50
            #Color del cuadrado basado en la suma de i + j para alternar entre blanco y negro
            color = 'white' if (i + j) % 2 == 0 else 'black'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

def draw_chip(canvas):
    for i in range(8):
        for j in range(8):
            if board[j][i] == 'r':
                color = 'red'
            elif board[j][i] == 'b':
                color = 'gray'
            else:
                continue
            canvas.create_oval(i * 50 + 10, j * 50 + 10, i * 50 + 40, j * 50 + 40, fill=color)