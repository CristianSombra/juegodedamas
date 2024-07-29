def valid_move(board, turn, start, end):
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
