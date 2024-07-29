from damas.components.valid_move import valid_move
from damas.components.move_chip import move_chip

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
        if valid_move(board, turn, selection, (x, y)):
            move_chip(board, turn, selection, (x, y))
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
