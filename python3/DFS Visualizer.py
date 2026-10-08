graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


def dfs(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        print("Visited:", node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)


dfs("A")