graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": []
}


def depth_limited_search(node, goal, limit, path):

    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph[node]:

        if neighbor not in path:

            result = depth_limited_search(
                neighbor,
                goal,
                limit - 1,
                path + [neighbor]
            )

            if result:
                return result

    return None


path = depth_limited_search(
    "A",
    "G",
    3,
    ["A"]
)

print("DLS Path:", path)