import heapq


grid = [
    "..........",
    "...###....",
    "...#......",
    "...#...#..",
    "......#...",
    ".........."
]


start = (0, 0)
goal = (5, 9)


directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def heuristic(a, b):

    return (
        abs(a[0] - b[0])
        + abs(a[1] - b[1])
    )


def plan():

    queue = [
        (0, start)
    ]

    parent = {
        start: None
    }

    cost = {
        start: 0
    }

    while queue:

        _, current = heapq.heappop(
            queue
        )

        if current == goal:
            break

        r, c = current

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if not (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
            ):
                continue

            if grid[nr][nc] == "#":
                continue

            neighbor = (
                nr,
                nc
            )

            new_cost = (
                cost[current] + 1
            )

            if (
                neighbor not in cost
                or new_cost < cost[neighbor]
            ):

                cost[neighbor] = new_cost

                priority = (
                    new_cost
                    + heuristic(
                        neighbor,
                        goal
                    )
                )

                heapq.heappush(
                    queue,
                    (
                        priority,
                        neighbor
                    )
                )

                parent[neighbor] = current

    if goal not in parent:
        return []

    path = []

    current = goal

    while current is not None:

        path.append(current)
        current = parent[current]

    return path[::-1]


path = plan()

result = [
    list(row)
    for row in grid
]

for r, c in path:

    if (
        (r, c) != start
        and (r, c) != goal
    ):
        result[r][c] = "*"


for row in result:
    print("".join(row))