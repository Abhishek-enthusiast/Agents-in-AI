def is_valid_map_coloring(assignment, state, color, neighbors):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring_csp(states, colors, neighbors, assignment={}):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment][0]

    for color in colors:
        if is_valid_map_coloring(assignment, unassigned, color, neighbors):
            assignment[unassigned] = color
            result = map_coloring_csp(states, colors, neighbors, assignment)
            if result:
                return result
            del assignment[unassigned]

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
    
    solution = map_coloring_csp(states, colors, neighbors)
    print("Map Coloring Solution:", solution)
