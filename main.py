import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import json
import os

def select(selection: tk.StringVar):
    print(selection.get())
    

def main() -> None:
    root = tk.Tk()
    root.title = "Rock, Paper, Scissors!"
    root.geometry("400x400")
    
    # Create a frame to hold to choice buttons.
    frame_choice: ttk.Frame = ttk.Frame(root)
    frame_choice.pack()
    
    # String variable to hold selection.
    selection = tk.StringVar()
    
    # Create option buttons.
    rad_rock = ttk.Radiobutton(frame_choice, text="Rock", variable=selection, value="rock", command=lambda: select(selection))
    rad_paper = ttk.Radiobutton(frame_choice, text="Paper", variable=selection, value="paper", command=lambda: select(selection))
    rad_scissors = ttk.Radiobutton(frame_choice, text="Scissors", variable=selection, value="scissors", command=lambda: select(selection))
    
    # Place options in choice frame.
    rad_rock.grid(row=0, column=0)
    rad_paper.grid(row=0, column=1)
    rad_scissors.grid(row=0, column=2)
    
    # Create a frame to hold choice pictures.
    frame_choice_pictures = ttk.Frame(root)
    frame_choice_pictures.pack()
    
    # Create frame for the picture boxes.
    frame_choice_pictures = ttk.Frame(root)
    frame_choice_pictures.pack()
    
    # Create picture boxses
    
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main()