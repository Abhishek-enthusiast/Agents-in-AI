from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": []
}


def bidirectional_search(start, goal):

    if start == goal:
        return [start]

    forward_queue = deque([[start]])
    backward_queue = deque([[goal]])

    forward_visited = {start: [start]}
    backward_visited = {goal: [goal]}

    reverse_graph = {node: [] for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            reverse_graph[neighbor].append(node)

    while forward_queue and backward_queue:

        path = forward_queue.popleft()
        node = path[-1]

        for neighbor in graph[node]:

            if neighbor not in forward_visited:
                new_path = path + [neighbor]
                forward_visited[neighbor] = new_path
                forward_queue.append(new_path)

                if neighbor in backward_visited:
                    return (
                        forward_visited[neighbor]
                        + backward_visited[neighbor][-2::-1]
                    )

        path = backward_queue.popleft()
        node = path[-1]

        for neighbor in reverse_graph[node]:

            if neighbor not in backward_visited:
                new_path = path + [neighbor]
                backward_visited[neighbor] = new_path
                backward_queue.append(new_path)

                if neighbor in forward_visited:
                    return (
                        forward_visited[neighbor]
                        + backward_visited[neighbor][-2::-1]
                    )

    return None


path = bidirectional_search("A", "G")

print("Bidirectional Path:", path)