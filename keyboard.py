import tkinter as tk
from tkinter import ttk

"""
creating a new window
"""
board = tk.Tk()
board.title('AccessWord')  # window name
# board.iconbitmap("ke.svg")  # icon

# window size
board.geometry('1010x250')             # normal size
board.maxsize(width=1010, height=250)  # maximum size
board.minsize(width=1010, height=250)  # minimum size

# text box
equation = tk.StringVar()
Dis_entry = ttk.Entry(board, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)

board.mainloop()
