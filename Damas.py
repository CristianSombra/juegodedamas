import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Juego de damas")
root.geometry("400x400")

canvas =  tk.Canvas(root, width=400, height=400)
canvas.pack()

def draw_board():
    for i in range(8):
        for j in range(8):
            #Coordenadas superiores izquierdas del rectángulo
            x1, y1 = i * 50, j * 50
            #Coordenadas inferiores derechas del rectángulo
            x2, y2 = x1 + 50, y1 + 50
            #Color del cuadrado basado en la suma de i + j para alternar entre blanco y negro
            color = 'white' if (i + j) % 2 == 0 else 'black'

def draw_chip():
    for i in range(8):
        for j in range(8):
            if(i + j) % 2 != 0:
                if j < 3:
                    color = 'red'
                elif j > 4:
                    color = 'black'
                else:
                    continue
                canvas.create_oval(i * 50 + 10, j * 50 + 10, i * 50 + 40, j * 50 + 40, fill=color)

#Se dibuja el tablero y las fichas
draw_board()
draw_chip()

#Ejecución de bucle principal
root.mainloop()

