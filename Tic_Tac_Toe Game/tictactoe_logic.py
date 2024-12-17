class TicTacToeLogic:
    def __init__(self):
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    def is_moves_left(self):
        return any('_' in row for row in self.board)

    def evaluate(self, player, opponent):
        lines = self.board + list(zip(*self.board))  # Rows and columns
        diagonals = [[self.board[i][i] for i in range(3)], [self.board[i][2-i] for i in range(3)]]
        lines += diagonals

        for line in lines:
            if line[0] == line[1] == line[2]:
                if line[0] == player:
                    return 10
                elif line[0] == opponent:
                    return -10
        return 0

    def minimax(self, depth, is_maximizing_player, player, opponent, alpha=-1000, beta=1000):
        score = self.evaluate(player, opponent)

        if score == 10 or score == -10:
            return score
        if not self.is_moves_left():
            return 0

        if is_maximizing_player:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        self.board[i][j] = player
                        best = max(best, self.minimax(depth + 1, False, player, opponent, alpha, beta))
                        self.board[i][j] = '_'
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        self.board[i][j] = opponent
                        best = min(best, self.minimax(depth + 1, True, player, opponent, alpha, beta))
                        self.board[i][j] = '_'
                        beta = min(beta, best)
                        if beta <= alpha:
                            break
            return best

    def find_best_move(self, player, opponent):
        best_val = -1000
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    self.board[i][j] = player
                    move_val = self.minimax(0, False, player, opponent)
                    self.board[i][j] = '_'
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move

    def reset_board(self):
        self.board = [['_' for _ in range(3)] for _ in range(3)]
