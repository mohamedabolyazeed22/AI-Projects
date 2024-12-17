import tkinter as tk
import random
import time

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Create an initial Sudoku board (0 represents empty cells)
        self.board = [
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
        
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        """ Create the grid for Sudoku UI """
        self.grid = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(self.root, width=4, font=('Arial', 18), 
                                 justify='center', bd=2, relief='solid')
                entry.grid(row=i, column=j, padx=5, pady=5)
                # Add number to the grid if not zero (pre-filled cells)
                if self.board[i][j] != 0:
                    entry.insert(tk.END, str(self.board[i][j]))
                    entry.config(state='disabled')
                row.append(entry)
            self.grid.append(row)

    def create_buttons(self):
        """ Create Solve and Clear buttons """
        solve_btn = tk.Button(self.root, text="Solve", width=10, height=2, command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=2, pady=5)
        
        ai_btn = tk.Button(self.root, text="AI Move", width=10, height=2, command=self.ai_move)
        ai_btn.grid(row=9, column=2, columnspan=2, pady=5)
        
        clear_btn = tk.Button(self.root, text="Clear", width=10, height=2, command=self.clear_grid)
        clear_btn.grid(row=9, column=4, columnspan=2, pady=5)

    def solve(self):
        """ Function to solve the Sudoku puzzle using backtracking """
        if self.solve_sudoku(self.board):
            self.update_grid()
        else:
            print("No solution exists!")

    def solve_sudoku(self, board):
        """ Backtracking solver for Sudoku """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_safe(board, i, j, num):
                            board[i][j] = num
                            if self.solve_sudoku(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    def is_safe(self, board, row, col, num):
        """ Check if placing a number is safe """
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def update_grid(self):
        """ Update the grid with the solved numbers """
        for i in range(9):
            for j in range(9):
                self.grid[i][j].delete(0, tk.END)
                self.grid[i][j].insert(tk.END, str(self.board[i][j]))
                self.grid[i][j].config(state='disabled')

    def ai_move(self):
        """ Simulate an AI Move (makes a random legal move) """
        empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        if not empty_cells:
            print("Game Over! No more moves can be made.")
            return

        i, j = random.choice(empty_cells)  # Choose random empty cell
        num = random.randint(1, 9)  # Random number from 1 to 9

        if self.is_safe(self.board, i, j, num):
            self.board[i][j] = num
            self.grid[i][j].delete(0, tk.END)
            self.grid[i][j].insert(tk.END, str(num))
            print(f"AI placed {num} in cell ({i},{j})")
        else:
            self.ai_move()  # Retry if the move was not valid

    def clear_grid(self):
        """ Clear the board for a new game """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.grid[i][j].delete(0, tk.END)
                    self.grid[i][j].config(state='normal')

        print("Grid cleared!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
