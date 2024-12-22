class TicTacToeLogic:
    def __init__(self, player_symbol, opponent_symbol):
        self.board = [['_' for _ in range(3)] for _ in range(3)]
        self.player = player_symbol
        self.opponent = opponent_symbol

    def is_moves_left(self):
        return any('_' in row for row in self.board)

    def evaluate(self):
        lines = self.board + list(zip(*self.board))
        diagonals = [[self.board[i][i] for i in range(3)], [self.board[i][2 - i] for i in range(3)]]
        lines += diagonals

        for line in lines:
            if line.count(line[0]) == 3 and line[0] != '_':
                return 10 if line[0] == self.player else -10
        return 0

    def minimax(self, depth, is_maximizing_player):
        score = self.evaluate()

        if score == 10 or score == -10:
            return score
        if not self.is_moves_left():
            return 0

        if is_maximizing_player:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        self.board[i][j] = self.player
                        best = max(best, self.minimax(depth + 1, False))
                        self.board[i][j] = '_'
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        self.board[i][j] = self.opponent
                        best = min(best, self.minimax(depth + 1, True))
                        self.board[i][j] = '_'
            return best

    def find_best_move(self):
        best_val = -1000
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    self.board[i][j] = self.player
                    move_val = self.minimax(0, False)
                    self.board[i][j] = '_'
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move