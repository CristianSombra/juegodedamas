def move_chip(board, turn, start, end):
    # Mueve una ficha de una posición a otra en el tablero.
    sx, sy = start
    ex, ey = end

    # Verifica que la casilla de destino esté vacía
    if board[ey][ex] != '.':
        raise ValueError("La casilla de destino no está vacía.")

    # Mueve la ficha
    board[ey][ex] = board[sy][sx]
    board[sy][sx] = '.'

    # Si es un movimiento de captura, elimina la ficha capturada
    if abs(sx - ex) == 2:
        mx, my = (sx + ex) // 2, (sy + ey) // 2
        board[my][mx] = '.'

    # Promociona una ficha roja a dama
    if turn == 'r' and ey == 7:
        board[ey][ex] = 'R'

    # Promociona una ficha negra a dama
    elif turn == 'b' and ey == 0:
        board[ey][ex] = 'B'
