import math

class TicTacToe:
    def __init__(self, board=None, turn='X'):
        self.board = board if board is not None else [' '] * 9
        self.turn = turn

    def is_terminal(self):
        return self.check_winner() is not None or ' ' not in self.board

    def check_winner(self):
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
        return None

    def evaluate(self):
        winner = self.check_winner()
        if winner == 'X':
            return 10
        elif winner == 'O':
            return -10
        return 0

    def get_moves(self):
        moves = []
        next_turn = 'O' if self.turn == 'X' else 'X'
        for i in range(9):
            if self.board[i] == ' ':
                new_board = list(self.board)
                new_board[i] = self.turn
                moves.append(TicTacToe(new_board, next_turn))
        return moves


def minimax_ttt(state, is_maximizing):
    if state.is_terminal():
        return state.evaluate(), None

    best_move = None
    if is_maximizing:
        best_val = -math.inf
        for move in state.get_moves():
            val, _ = minimax_ttt(move, False)
            if val > best_val:
                best_val = val
                best_move = move
        return best_val, best_move
    else:
        best_val = math.inf
        for move in state.get_moves():
            val, _ = minimax_ttt(move, True)
            if val < best_val:
                best_val = val
                best_move = move
        return best_val, best_move


if __name__ == "__main__":
    ttt = TicTacToe(['X', 'O', 'X', ' ', 'O', ' ', ' ', ' ', ' '], turn='X')
    val, _ = minimax_ttt(ttt, True)
    print("Tic-Tac-Toe Minimax Evaluation:", val)
