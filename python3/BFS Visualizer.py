from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        print("Visited:", node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append(neighbor)


bfs("A")