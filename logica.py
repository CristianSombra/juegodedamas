# Ficha seleccionada
selection = None

# Turno inicial
turn = 'r'

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


def valid_move(start, end):
    #Valida si un movimiento de una ficha es válido.
    sx, sy = start
    ex, ey = end
    print(f"Validando movimiento de {start} a {end}")

    # Verificar que el destino está dentro del tablero
    if not (0 <= ex < 8 and 0 <= ey < 8):
        print("El destino está fuera del tablero.")
        return False

    # Verificar que el destino está vacío
    if board[ey][ex] != '.':
        print("El destino no está vacío.")
        return False

    dx, dy = abs(sx - ex), abs(sy - ey)
    print(f"dx: {dx}, dy: {dy}")

    # Movimiento simple en diagonal
    if dx == 1 and dy == 1:
        if (turn == 'r' and ey > sy) or (turn == 'b' and ey < sy):
            print("Movimiento simple válido.")
            return True
        else:
            print("Movimiento simple en la dirección incorrecta.")

    # Movimiento de captura en diagonal
    if dx == 2 and dy == 2:
        mx, my = (sx + ex) // 2, (sy + ey) // 2
        if board[my][mx] != '.' and board[my][mx] != turn[0]:
            if (turn == 'r' and ey > sy) or (turn == 'b' and ey < sy):
                print("Movimiento de captura válido.")
                return True
            else:
                print("Movimiento de captura en la dirección incorrecta.")
        else:
            print("No hay ficha oponente para capturar.")

    print("Movimiento inválido.")
    return False


def move_chip(start, end):
    #Mueve una ficha de una posición a otra en el tablero.
    sx, sy = start
    ex, ey = end
    board[ey][ex] = board[sy][sx]
    board[sy][sx] = '.'
    #Si es un movimiento de captura, elimina la ficha capturada
    if abs(sx - ex) == 2:
        mx, my = (sx + ex) // 2, (sy + ey) // 2
        board[my][mx] = '.'
    #Promociona una ficha roja a dama
    if turn == 'r' and ey == 7:
        board[ey][ex] = 'R'
    #Promociona una ficha negra a dama
    elif turn == 'b' and ey == 0:
        board[ey][ex] = 'B'


def click_event(event, canvas):
    #Maneja el evento de clic del usuario.
    global selection, turn
    x, y = event.x // 50, event.y // 50
    if selection is None:
        #Seleccionar una ficha
        if board[y][x] in [turn[0], turn.upper()]:
            selection = (x, y)
            print(f"Ficha seleccionada en: {selection}")
    else:
        #Mover una ficha seleccionada
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
    #Dibuja el tablero de juego en el canvas.
    canvas.delete("all")
    for i in range(8):
        for j in range(8):
            x1, y1 = i * 50, j * 50
            x2, y2 = x1 + 50, y1 + 50
            color = 'white' if (i + j) % 2 == 0 else 'black'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')


def draw_chip(canvas):
    for i in range(8):
        for j in range(8):
            if board[j][i] in ['r', 'R']:
                color = 'red'
            elif board[j][i] in ['b', 'B']:
                color = 'gray'
            else:
                continue
            canvas.create_oval(i * 50 + 10, j * 50 + 10, i * 50 + 40, j * 50 + 40, fill=color)
