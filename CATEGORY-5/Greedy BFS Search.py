import heapq

board = [
    ['X', 'O', 'X'],
    [' ', 'O', ' '],
    [' ', ' ', 'X']
]

goal = [
    ['X', 'O', 'X'],
    [' ', 'O', ' '],
    [' ', ' ', 'O']
]

def heuristic(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal[i][j]:
                count += 1
    return count

def greedy_search():
    start = tuple(tuple(row) for row in board)
    target = tuple(tuple(row) for row in goal)

    queue = [(heuristic(board), start)]
    visited = set()

    while queue:
        h, state = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)

        if state == target:
            print("Goal State:")
            for row in state:
                print(row)
            return

        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    new_board = [list(row) for row in state]
                    new_board[i][j] = 'O'
                    new_state = tuple(tuple(row) for row in new_board)

                    if new_state not in visited:
                        heapq.heappush(
                            queue,
                            (heuristic(new_board), new_state)
                        )

    print("Goal not found")

greedy_search()
