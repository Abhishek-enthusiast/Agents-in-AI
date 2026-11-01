import heapq


class TicTacToeProblem:
    def __init__(self, board=None, player='X'):
        self.board = board if board is not None else [' '] * 9
        self.player = player
        self.g = 0
        self.h = self.evaluate()
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def evaluate(self):
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return -10 if self.board[a] == 'O' else 10
        return 0

    def is_goal(self):
        return ' ' not in self.board or self.evaluate() != 0

    def get_neighbors(self):
        neighbors = []
        next_player = 'O' if self.player == 'X' else 'X'
        for i in range(9):
            if self.board[i] == ' ':
                new_board = list(self.board)
                new_board[i] = self.player
                child = TicTacToeProblem(new_board, next_player)
                child.g = self.g + 1
                child.f = child.g + child.h
                neighbors.append(child)
        return neighbors


class MissionariesCannibalsProblem:
    def __init__(self, state=(3, 3, 1)):
        self.state = state
        self.g = 0
        self.h = (state[0] + state[1]) / 2.0
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def is_goal(self):
        return self.state == (0, 0, 0)

    def is_valid(self, m, c):
        if m < 0 or c < 0 or m > 3 or c > 3:
            return False
        if m > 0 and m < c:
            return False
        m_right, c_right = 3 - m, 3 - c
        if m_right > 0 and m_right < c_right:
            return False
        return True

    def get_neighbors(self):
        m, c, b = self.state
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        neighbors = []
        for dm, dc in moves:
            if b == 1:
                nm, nc, nb = m - dm, c - dc, 0
            else:
                nm, nc, nb = m + dm, c + dc, 1
            if self.is_valid(nm, nc):
                child = MissionariesCannibalsProblem((nm, nc, nb))
                child.g = self.g + 1
                child.f = child.g + child.h
                neighbors.append(child)
        return neighbors


class EightPuzzleProblem:
    def __init__(self, state=None):
        self.state = state if state is not None else (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.g = 0
        self.h = self.manhattan_distance()
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def is_goal(self):
        return self.state == (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def manhattan_distance(self):
        dist = 0
        for idx, val in enumerate(self.state):
            if val != 0:
                target_r, target_c = (val - 1) // 3, (val - 1) % 3
                current_r, current_c = idx // 3, idx % 3
                dist += abs(target_r - current_r) + abs(target_c - current_c)
        return dist

    def get_neighbors(self):
        neighbors = []
        idx = self.state.index(0)
        r, c = idx // 3, idx % 3
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_idx = nr * 3 + nc
                new_state = list(self.state)
                new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
                child = EightPuzzleProblem(tuple(new_state))
                child.g = self.g + 1
                child.f = child.g + child.h
                neighbors.append(child)
        return neighbors


def sma_star_search(initial_node, memory_limit=10):
    open_list = [initial_node]
    nodes_map = {}

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return current

        for neighbor in current.get_neighbors():
            if len(open_list) >= memory_limit:
                worst_node = max(open_list, key=lambda x: x.f)
                if neighbor.f < worst_node.f:
                    open_list.remove(worst_node)
                    heapq.heapify(open_list)
                    heapq.heappush(open_list, neighbor)
            else:
                heapq.heappush(open_list, neighbor)

    return None


if __name__ == "__main__":
    ttt = TicTacToeProblem()
    ttt_result = sma_star_search(ttt, memory_limit=15)
    print("Tic-Tac-Toe Final Board:", ttt_result.board if ttt_result else "No Solution")

    mc = MissionariesCannibalsProblem()
    mc_result = sma_star_search(mc, memory_limit=10)
    print("Missionaries & Cannibals Goal State:", mc_result.state if mc_result else "No Solution")

    puzzle = EightPuzzleProblem((1, 2, 3, 4, 0, 6, 7, 5, 8))
    puzzle_result = sma_star_search(puzzle, memory_limit=20)
    print("Eight Puzzle Solved State:", puzzle_result.state if puzzle_result else "No Solution")
