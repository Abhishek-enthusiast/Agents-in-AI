import random

N = 8

def calculate_conflicts(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def generate_neighbors(state):
    neighbors = []

    for row in range(N):
        for column in range(N):
            if column != state[row]:
                neighbor = state.copy()
                neighbor[row] = column
                neighbors.append(neighbor)

    return neighbors


def hill_climbing():
    current_state = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    while True:
        current_conflicts = calculate_conflicts(current_state)

        if current_conflicts == 0:
            return current_state, "GLOBAL OPTIMUM"

        neighbors = generate_neighbors(current_state)

        best_state = min(
            neighbors,
            key=calculate_conflicts
        )

        best_conflicts = calculate_conflicts(best_state)

        if best_conflicts >= current_conflicts:
            return current_state, "LOCAL OPTIMUM"

        current_state = best_state


solution, result = hill_climbing()

print("================================")
print("      8-QUEENS HILL CLIMBING")
print("================================")

print("Result :", result)
print("State  :", solution)
print("Conflicts :", calculate_conflicts(solution))

print("\nChessboard:")

for row in range(N):
    for column in range(N):
        if solution[row] == column:
            print(" Q ", end="")
        else:
            print(" . ", end="")
    print()