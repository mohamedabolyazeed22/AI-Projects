import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for r in range(9):
        for c in range(9):
            cell = board[r][c]
            if cell == 0:
                grid[r][c].delete(0)
            else:
                grid[r][c].delete(0)
                grid[r][c].insert(0, str(cell))

def is_valid(board, row_sets, col_sets, box_sets, row, col, num):
    box_index = (row // 3) * 3 + (col // 3)
    return (num not in row_sets[row] and
            num not in col_sets[col] and
            num not in box_sets[box_index])

def ai_move(board, row_sets, col_sets, box_sets):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row_sets, col_sets, box_sets, r, c, num):
                        # Place the number
                        board[r][c] = num
                        row_sets[r].add(num)
                        col_sets[c].add(num)
                        box_sets[(r // 3) * 3 + (c // 3)].add(num)
                        return True  # AI made a move
    return False  # No valid moves for AI

def player_move(board, row_sets, col_sets, box_sets, row, col, num):
    if is_valid(board, row_sets, col_sets, box_sets, row, col, num):
        board[row][col] = num
        row_sets[row].add(num)
        col_sets[col].add(num)
        box_sets[(row // 3) * 3 + (col // 3)].add(num)
        return True
    return False

def solve_sudoku(board):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    box_sets = [set() for _ in range(9)]

    # Initialize sets with existing numbers
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0:
                row_sets[r].add(num)
                col_sets[c].add(num)
                box_sets[(r // 3) * 3 + (c // 3)].add(num)

    turn = 'AI'  # Start with AI's turn
    while True:
        if all(all(cell != 0 for cell in row) for row in board):
            messagebox.showinfo("Sudoku", "The Sudoku is solved!")
            break

        if turn == 'AI':
            if not ai_move(board, row_sets, col_sets, box_sets):
                messagebox.showinfo("Sudoku", "AI has no valid moves left.")
                break
            turn = 'Player'  # Switch to player's turn
        else:
            break  # Player's turn is handled by GUI

def on_cell_click(row, col):
    try:
        num = int(grid[row][col].get())
        if num < 1 or num > 9:
            raise ValueError
        if player_move(sudoku_board, row_sets, col_sets, box_sets, row, col, num):
            print_board(sudoku_board)
        else:
            messagebox.showerror("Invalid Move", "This move is not valid.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 1 and 9.")

def ai_turn():
    solve_sudoku(sudoku_board)
    print_board(sudoku_board)

# Create the main window
root = tk.Tk()
root.title("Sudoku Game")

# Create a 9x9 grid of Entry widgets
grid = [[None for _ in range(9)] for _ in range(9)]
for r in range(9):
    for c in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
        entry.grid(row=r, column=c, padx=5, pady=5)
        entry.bind("<FocusOut>", lambda e, row=r, col=c: on_cell_click(row, col))
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

# Initialize sets for the Sudoku board
row_sets = [set() for _ in range(9)]
col_sets = [set() for _ in range(9)]
box_sets = [set() for _ in range(9)]

# Fill the grid with initial values
print_board(sudoku_board)

# Create a button for AI move
ai_button = tk.Button(root, text="AI Move", command=ai_turn)
ai_button.grid(row=10, column=0, columnspan=9, pady=10)

# Start the GUI event loop
root.mainloop()