from collections import deque


maze = [
    "###########",
    "#P        #",
    "# ### ### #",
    "#         #",
    "# ### ### #",
    "#       G #",
    "###########"
]


def find(symbol):

    for r, row in enumerate(maze):

        for c, value in enumerate(row):

            if value == symbol:
                return r, c


start = find("P")
goal = find("G")


directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def find_path():

    queue = deque([start])

    parent = {
        start: None
    }

    while queue:

        current = queue.popleft()

        if current == goal:
            break

        r, c = current

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if not (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
            ):
                continue

            if maze[nr][nc] == "#":
                continue

            neighbor = (
                nr,
                nc
            )

            if neighbor not in parent:

                parent[neighbor] = current
                queue.append(neighbor)

    if goal not in parent:
        return []

    path = []

    current = goal

    while current is not None:

        path.append(current)
        current = parent[current]

    return path[::-1]


path = find_path()

grid = [
    list(row)
    for row in maze
]

for r, c in path:

    if grid[r][c] not in ("P", "G"):
        grid[r][c] = "*"


for row in grid:
    print("".join(row))

print(
    "\nAI path length:",
    len(path)
)