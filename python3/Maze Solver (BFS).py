from collections import deque

maze = [
    "##########",
    "#S#      #",
    "# # #### #",
    "# #    # #",
    "# #### # #",
    "#      #E#",
    "##########"
]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def find_point(symbol):
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == symbol:
                return r, c


start = find_point("S")
end = find_point("E")


def bfs():
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            break

        r, c = current

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != "#"
            ):
                neighbor = (nr, nc)

                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

    if end not in parent:
        return []

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    return path[::-1]


path = bfs()

grid = [list(row) for row in maze]

for r, c in path:
    if grid[r][c] not in ("S", "E"):
        grid[r][c] = "*"

for row in grid:
    print("".join(row))

print("\nPath length:", len(path))