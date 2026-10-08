import heapq


graph = {
    "A": {
        "B": 4,
        "C": 2
    },

    "B": {
        "A": 4,
        "C": 1,
        "D": 5
    },

    "C": {
        "A": 2,
        "B": 1,
        "D": 8,
        "E": 10
    },

    "D": {
        "B": 5,
        "C": 8,
        "E": 2
    },

    "E": {
        "C": 10,
        "D": 2
    }
}


def dijkstra(start):

    distances = {
        node: float("inf")
        for node in graph
    }

    distances[start] = 0

    queue = [
        (0, start)
    ]

    while queue:

        distance, node = heapq.heappop(
            queue
        )

        if distance > distances[node]:
            continue

        print(
            f"Visiting {node}: "
            f"{distance}"
        )

        for neighbor, weight in graph[node].items():

            new_distance = (
                distance + weight
            )

            if new_distance < distances[neighbor]:

                distances[neighbor] = (
                    new_distance
                )

                heapq.heappush(
                    queue,
                    (
                        new_distance,
                        neighbor
                    )
                )

    return distances


result = dijkstra("A")

print("\nShortest distances:")

for node, distance in result.items():
    print(node, "=", distance)