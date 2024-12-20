# Game Documentation: Tic-Tac-Toe and Sudoku

## 🎮 Overview
This project features two timeless games: **Tic-Tac-Toe** and **Sudoku**, crafted using **Python** and the **Tkinter** library for graphical user interfaces (GUIs). Dive into strategic gameplay with Tic-Tac-Toe or challenge your logic with Sudoku!

- **Tic-Tac-Toe**: A 2-player game (Human vs AI), powered by the **minimax algorithm** for AI decision-making.
- **Sudoku**: A classic number puzzle with a backtracking algorithm for automated solving.

### ✨ Features
- Intuitive graphical interfaces with buttons and interactivity.
- Reset, solve, and play functionalities for both games.
- Algorithms tailored for optimal performance and simplicity.

---

## 🧩 Core Components

### 🕹 Tic-Tac-Toe

#### **Logic**
- **Minimax Algorithm**: Ensures the AI plays optimally.
- **Game Evaluation**: Checks for winning or draw conditions.
- **Move Validation**: Determines legal moves on the board.

#### **UI**
- Interactive 3x3 grid for player moves.
- Score tracking for both players.
- Reset option for a fresh start.

### 🔢 Sudoku

#### **Solver**
- **Backtracking Algorithm**: Finds solutions efficiently.
- **Validation Functions**: Ensures number placement follows Sudoku rules.

#### **UI**
- Editable 9x9 grid for user inputs.
- Buttons for solving, clearing, and resetting the puzzle.
- Interactive numpad for number entry.

---

## 🚀 Key Functions

### Tic-Tac-Toe

#### Logic Functions
- **`is_moves_left(board)`**: Checks for available moves.
- **`evaluate(board)`**: Scores the board state.
- **`minimax(board, depth, is_max)`**: AI algorithm for optimal decision-making.
- **`find_best_move(board)`**: Identifies the AI’s best move.

#### UI Functions
- **`create_scoreboard()`**: Displays current scores.
- **`human_turn(x, y)`**: Processes player moves.
- **`opponent_turn()`**: Executes AI moves.
- **`reset_game()`**: Resets scores and board.

### Sudoku

#### Solver Functions
- **`find_next_empty_cell(board)`**: Locates the next empty cell.
- **`valid_board(board, num, pos)`**: Validates number placement.
- **`solve_sudoku(board)`**: Recursively solves the puzzle.

#### UI Functions
- **`create_grid()`**: Draws the Sudoku board.
- **`cell_clicked(row, col)`**: Handles cell selections.
- **`clear_board()`**: Erases user inputs while retaining defaults.
- **`reset_game()`**: Restarts the puzzle.

---

## 🖥 Graphical Interface

### Tic-Tac-Toe
- **Grid**: 3x3 clickable buttons.
- **Player Interaction**: Real-time AI responses to player moves.
- **Victory Notification**: Announces the winner or a draw.
- **Control Options**: Reset and start new games easily.

### Sudoku
- **Grid**: Interactive 9x9 table for number placement.
- **Numpad**: Intuitive number entry system.
- **Solver**: Automatically completes the puzzle with a single click.
- **Customization**: Reset or clear the board for retries.

---

## 📊 Sample Output

### Tic-Tac-Toe
**Before Solving:**
```
X | O | _
---------
_ | X | _
---------
O | _ | _
```
**After Solving (AI Move):**
```
X | O | _
---------
_ | X | O
---------
O | _ | X
```

### Sudoku
**Before Solving:**
```
7 8 _ | _ _ _ | 1 2 _
_ _ _ | 4 _ _ | _ _ _
_ _ _ | _ 7 _ | _ _ _
```
**After Solving:**
```
7 8 9 | 5 4 3 | 1 2 6
6 1 2 | 7 9 8 | 3 4 5
5 3 4 | 2 6 1 | 8 9 7
```

---

## ⚙️ Dependencies

- **Python 3.x**
- **Tkinter** library

Ensure Tkinter is installed before running the games.

---

## 💡 Suggestions & Improvements

### Tic-Tac-Toe
- Add customizable AI difficulty levels.
- Enhance UI with animations or sound effects.
- Support for multiplayer mode over the network.

### Sudoku
- Include difficulty options (easy, medium, hard).
- Add a "Hint" button for user assistance.
- Improve aesthetics with modern UI themes.
