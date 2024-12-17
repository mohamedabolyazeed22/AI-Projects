# gui.py

import tkinter as tk
from tkinter import messagebox
from sudoku import print_board, player_move, ai_move

def on_cell_click(row, col):
    try:
        num = int(grid[row][col].get())
        if num < 1 or num > 9:
            raise ValueError
        if player_move(sudoku_board, row, col, num):
            print_board(sudoku_board)
        else:
            messagebox.showerror("Invalid Move", "This move is not valid.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 1 and 9.")

def ai_turn():
    if ai_move(sudoku_board):
        print_board(sudoku_board)
    else:
        messagebox.showinfo("AI Move", "AI has no valid moves left.")

# Create the main window
root = tk.Tk()
root.title("Sudoku Game")

# Create a 9x9 grid of Entry widgets
grid = [[None for _ in range(9)] for _ in range(9)]
for r in range(9):
    for c in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
        entry.grid(row=r, column=c, padx=5, pady=5)
        entry.bind("<Return>", lambda e, row=r, col=c: on_cell_click(row, col))
        grid[r][c] = entry

# Initialize the Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Fill the grid with initial values
print_board(sudoku_board)

# Create a button for AI move
ai_button = tk.Button(root, text="AI Move", command=ai_turn)
ai_button.grid(row=10, column=0, columnspan=9, pady=10)

# Start the GUI event loop
root.mainloop()