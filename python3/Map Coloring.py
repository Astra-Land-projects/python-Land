regions = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}


colors = [
    "Red",
    "Green",
    "Blue"
]


assignment = {}


def valid(region, color):

    for neighbor in regions[region]:

        if assignment.get(neighbor) == color:
            return False

    return True


def solve():

    if len(assignment) == len(regions):
        return True

    region = next(
        r
        for r in regions
        if r not in assignment
    )

    for color in colors:

        if valid(region, color):

            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False


if solve():

    for region, color in assignment.items():
        print(
            f"{region}: {color}"
        )

else:

    print("No solution.")