import random
import time


WIDTH = 20
HEIGHT = 10

snake = [(5, 5)]
direction = (1, 0)

food = (
    random.randint(0, WIDTH - 1),
    random.randint(0, HEIGHT - 1)
)


def draw():

    print("\033[H\033[J")

    for y in range(HEIGHT):

        row = ""

        for x in range(WIDTH):

            if (x, y) == food:
                row += "●"

            elif (x, y) == snake[0]:
                row += "O"

            elif (x, y) in snake:
                row += "o"

            else:
                row += "."

        print(row)


def choose_direction():

    head = snake[0]

    dx = food[0] - head[0]
    dy = food[1] - head[1]

    if abs(dx) > abs(dy):

        return (
            1 if dx > 0 else -1,
            0
        )

    return (
        0,
        1 if dy > 0 else -1
    )


while True:

    direction = choose_direction()

    head_x, head_y = snake[0]

    dx, dy = direction

    new_head = (
        head_x + dx,
        head_y + dy
    )

    if not (
        0 <= new_head[0] < WIDTH
        and 0 <= new_head[1] < HEIGHT
    ):
        print("AI hit the wall.")
        break

    if new_head in snake:
        print("AI hit itself.")
        break

    snake.insert(0, new_head)

    if new_head == food:

        while True:

            food = (
                random.randint(
                    0,
                    WIDTH - 1
                ),
                random.randint(
                    0,
                    HEIGHT - 1
                )
            )

            if food not in snake:
                break

    else:

        snake.pop()

    draw()

    time.sleep(0.3)