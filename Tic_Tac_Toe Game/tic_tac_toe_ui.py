import tkinter as tk
from tkinter import messagebox, simpledialog
from tic_tac_toe_logic import TicTacToeLogic

class TicTacToeUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("400x500")

        # Ask player for names and symbols
        self.player_name = simpledialog.askstring("Player Name", "Enter your name:")
        self.opponent_name = "Opponent"
        self.player_symbol = simpledialog.askstring("Choose Symbol", "Choose your symbol (X or O):").upper()
        self.opponent_symbol = 'X' if self.player_symbol == 'O' else 'O'

        self.logic = TicTacToeLogic(self.opponent_symbol, self.player_symbol)

        # Scores
        self.player_score = 0
        self.opponent_score = 0

        # Setup UI
        self.create_scoreboard()
        self.create_buttons()

    def create_scoreboard(self):
        self.scoreboard_frame = tk.Frame(self.master)
        self.scoreboard_frame.pack(pady=10)

        self.player_label = tk.Label(self.scoreboard_frame, text=f"{self.player_name}: 0", font=("Arial", 14))
        self.player_label.pack(side=tk.LEFT, padx=10)

        self.opponent_label = tk.Label(self.scoreboard_frame, text=f"{self.opponent_name}: 0", font=("Arial", 14))
        self.opponent_label.pack(side=tk.RIGHT, padx=10)

    def create_buttons(self):
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.button_frame, text='', font=('Arial', 20), width=5, height=2,
                command=lambda r=i, c=j: self.human_turn(r, c))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game, font=("Arial", 12),
                bg="#F39C12", fg="white")
        self.reset_button.pack(pady=20)

    def human_turn(self, row, col):
        if self.logic.board[row][col] == '_':
            self.make_move(row, col, self.player_symbol)
            if self.check_winner():
                return
            self.opponent_turn()

    def opponent_turn(self):
        best_move = self.logic.find_best_move()
        if best_move != (-1, -1):
            self.make_move(best_move[0], best_move[1], self.opponent_symbol)
            self.check_winner()

    def make_move(self, row, col, symbol):
        self.logic.board[row][col] = symbol
        self.buttons[row][col].config(text=symbol, state=tk.DISABLED)

    def check_game_limit(self):
        # Check if the score reaches 5 and display the final winner
        if self.player_score >= 5:
            final_winner = f"🎉 {self.player_name} is the Grand Winner! 🎉"
        elif self.opponent_score >= 5:
            final_winner = f"🎉 {self.opponent_name} is the Grand Winner! 🎉"
        else:
            return False  

        # Show final winner and ask to play again
        messagebox.showinfo("Game Over", final_winner)
        play_again = messagebox.askyesno("Play Again?", "Do you want to start a new game?")
        
        if play_again:
            self.reset_game()  
        else:
            self.master.quit()  
        return True

    def check_winner(self):
        result = self.logic.evaluate()
        if result == 10:
            self.opponent_score += 1
            self.show_result(f"{self.opponent_name} Wins!")
            self.check_game_limit()  
            return True
        elif result == -10:
            self.player_score += 1
            self.show_result(f"{self.player_name} Wins!")
            self.check_game_limit()  
            return True
        elif not self.logic.is_moves_left():
            self.show_result("It's a Draw!")
            return True
        return False

    def show_result(self, message):
        messagebox.showinfo("Game Over", message)
        self.update_scores()
        self.reset_board()

    def update_scores(self):
        self.player_label.config(text=f"{self.player_name}: {self.player_score}")
        self.opponent_label.config(text=f"{self.opponent_name}: {self.opponent_score}")

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.logic.board[i][j] = '_'
                self.buttons[i][j].config(text='', state=tk.NORMAL)

    def reset_game(self):
        self.player_score = 0
        self.opponent_score = 0
        self.update_scores()
        self.reset_board()



root = tk.Tk()
app = TicTacToeUI(root)
root.mainloop()