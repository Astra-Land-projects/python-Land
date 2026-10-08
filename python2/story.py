import random

def generate_story():
    """Generates a random short story."""

    characters = ["a brave knight", "a mischievous wizard", "a cunning rogue", "a wise old woman"]
    settings = ["a dark forest", "a towering castle", "a bustling marketplace", "a hidden cave"]
    actions = ["discovered a secret", "fought a dragon", "solved a riddle", "found a treasure"]
    outcomes = ["lived happily ever after", "learned a valuable lesson", "became a legend", "returned home safely"]

    character = random.choice(characters)
    setting = random.choice(settings)
    action = random.choice(actions)
    outcome = random.choice(outcomes)

    story = f"Once upon a time, there was {character} in {setting}. They {action} and ultimately {outcome}."
    return story

if __name__ == "__main__":
    story = generate_story()
    print(story)