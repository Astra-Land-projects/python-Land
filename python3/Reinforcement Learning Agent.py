import random


STATES = 6

ACTIONS = [
    -1,  # left
    1    # right
]

GOAL = 5


q_table = [
    [0.0, 0.0]
    for _ in range(STATES)
]


LEARNING_RATE = 0.1
DISCOUNT = 0.9
EPSILON = 0.2


def choose_action(state):

    if random.random() < EPSILON:

        return random.randint(
            0,
            len(ACTIONS) - 1
        )

    values = q_table[state]

    return values.index(
        max(values)
    )


def step(state, action):

    new_state = (
        state + ACTIONS[action]
    )

    new_state = max(
        0,
        min(
            STATES - 1,
            new_state
        )
    )

    if new_state == GOAL:
        reward = 10
    else:
        reward = -1

    done = (
        new_state == GOAL
    )

    return (
        new_state,
        reward,
        done
    )


EPISODES = 500


for episode in range(EPISODES):

    state = 0

    for _ in range(100):

        action = choose_action(state)

        new_state, reward, done = step(
            state,
            action
        )

        best_next = max(
            q_table[new_state]
        )

        old_value = (
            q_table[state][action]
        )

        new_value = (
            old_value
            + LEARNING_RATE
            * (
                reward
                + DISCOUNT * best_next
                - old_value
            )
        )

        q_table[state][action] = (
            new_value
        )

        state = new_state

        if done:
            break


print("===== Q TABLE =====")

for state, values in enumerate(
    q_table
):

    print(
        f"State {state}: "
        f"Left={values[0]:.2f}, "
        f"Right={values[1]:.2f}"
    )


print("\n===== TEST =====")

state = 0

path = [state]

for _ in range(20):

    action = q_table[state].index(
        max(q_table[state])
    )

    state, reward, done = step(
        state,
        action
    )

    path.append(state)

    if done:
        break


print("Path:", path)
print("Goal reached:", state == GOAL)