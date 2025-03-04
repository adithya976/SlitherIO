import tkinter as tk
from MainCG import MainCG
import pygame

game = MainCG()

root = tk.Tk()


def demo():
    game.init()


def close():
    root.destroy()
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         game.quit = True
    #         root.destroy()


root.title("SERPENTINE SAGA")
label = tk.Label(root, text="WELCOME TO SLITHER IO")
label.pack()

button1 = tk.Button(root, text="Single Player", command=demo)
button2 = tk.Button(root, text="Multi Player")
button3 = tk.Button(root, text="Close", command=close)
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
