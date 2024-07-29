import tkinter as tk
from damas.logic import click_event, draw_board, draw_chip

#Creo la ventana principal
root = tk.Tk()
root.title("Juego de damas")
root.geometry("400x400")

#Creo el canvas para dibujar el tablero
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

#Se dibuja el tablero y las fichas
draw_board(canvas)
draw_chip(canvas)

#Se vincula el evento de click
canvas.bind("<Button-1>", lambda event: click_event(event, canvas))

#Ejecución de bucle principal
root.mainloop()

