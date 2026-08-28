import heapq

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (1, 1)
]

def valid(state):
    m, c, boat = state

    if m < 0 or m > 3 or c < 0 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    right_m = 3 - m
    right_c = 3 - c

    if right_m > 0 and right_m < right_c:
        return False

    return True

def heuristic(state):
    m, c, boat = state
    return m + c

def a_star():
    queue = [(heuristic(start), 0, start, [start])]
    visited = {}

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state in visited and visited[state] <= g:
            continue

        visited[state] = g

        if state == goal:
            print("Solution:")
            for state in path:
                print(state)
            print("Cost:", g)
            return

        m, c, boat = state

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if valid(new_state):
                new_g = g + 1
                new_f = new_g + heuristic(new_state)

                heapq.heappush(
                    queue,
                    (new_f, new_g, new_state, path + [new_state])
                )

    print("Solution not found")

a_star()
