import random

def count_conflicts(assignment, state, color, neighbors):
    conflicts = 0
    for neighbor in neighbors[state]:
        if assignment.get(neighbor) == color:
            conflicts += 1
    return conflicts

def min_conflicts_csp(states, colors, neighbors, max_steps=1000):
    assignment = {s: random.choice(colors) for s in states}

    for _ in range(max_steps):
        conflicted_states = [
            s for s in states 
            if count_conflicts(assignment, s, assignment[s], neighbors) > 0
        ]

        if not conflicted_states:
            return assignment

        var = random.choice(conflicted_states)
        
        min_color = min(
            colors, 
            key=lambda color: count_conflicts(assignment, var, color, neighbors)
        )
        assignment[var] = min_color

    return None


if __name__ == "__main__":
    states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    colors = ['Red', 'Green', 'Blue']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    solution = min_conflicts_csp(states, colors, neighbors)
    print("Min-Conflicts Solution:", solution)
