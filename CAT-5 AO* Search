graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('E', 1)]],
    'C': [[('F', 1)]],
    'D': [[('G', 1)]],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 0,
    'G': 0
}

solution = []

def ao_star(node):
    if not graph[node]:
        return heuristic[node]

    best_cost = float('inf')
    best_option = None

    for option in graph[node]:
        cost = 0

        for child, edge_cost in option:
            cost += edge_cost + ao_star(child)

        if cost < best_cost:
            best_cost = cost
            best_option = option

    solution.append((node, best_option))

    return best_cost

cost = ao_star('A')

print("Optimal Cost:", cost)
print("Solution:")

for node, option in solution:
    children = [child for child, edge in option]
    print(node, "->", children)
