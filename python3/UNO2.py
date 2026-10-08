"""
UNO Console Game (English version)
Play against a simple computer AI.
"""

import random

COLORS = ["Red", "Blue", "Green", "Yellow"]
NUMBERS = list(range(0, 10))
ACTIONS = ["Skip", "Reverse", "Draw Two"]
WILDS = ["Wild", "Wild Draw Four"]


class Card:
    def __init__(self, color, value):
        self.color = color   # one of COLORS, or None for wild cards
        self.value = value   # number, action, or wild

    def __str__(self):
        if self.color:
            return f"{self.color} {self.value}"
        return f"{self.value}"

    def matches(self, other):
        if self.color is None or other.color is None:
            return True
        return self.color == other.color or self.value == other.value


def build_deck():
    deck = []
    for color in COLORS:
        deck.append(Card(color, 0))
        for n in list(range(1, 10)) * 2:
            deck.append(Card(color, n))
        for action in ACTIONS * 2:
            deck.append(Card(color, action))
    for wild in WILDS:
        for _ in range(4):
            deck.append(Card(None, wild))
    random.shuffle(deck)
    return deck


class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.hand = []

    def draw(self, deck, discard, n=1):
        for _ in range(n):
            if not deck:
                deck.extend(discard[:-1])
                discard[:] = discard[-1:]
                random.shuffle(deck)
            if deck:
                self.hand.append(deck.pop())

    def has_valid_move(self, top_card):
        return any(c.matches(top_card) for c in self.hand)


def choose_wild_color():
    print("Choose a new color:")
    for i, c in enumerate(COLORS):
        print(f"{i + 1}. {c}")
    while True:
        choice = input("Color number: ").strip()
        if choice in ["1", "2", "3", "4"]:
            return COLORS[int(choice) - 1]
        print("Invalid choice, try again.")


def print_hand(player):
    print(f"\n{player.name}'s cards:")
    for i, c in enumerate(player.hand):
        print(f"  {i + 1}. {c}")


def human_turn(player, deck, discard, top_card, direction):
    print_hand(player)
    print(f"\nTop card: {top_card}")

    valid_moves = [i for i, c in enumerate(player.hand) if c.matches(top_card)]

    if not valid_moves:
        print(f"{player.name} has no valid card, drawing one...")
        player.draw(deck, discard)
        new_card = player.hand[-1]
        if new_card.matches(top_card):
            print(f"Drew: {new_card} - it's playable!")
            play = input("Do you want to play it? (yes/no): ").strip().lower()
            if play == "yes":
                return play_card(player, len(player.hand) - 1, discard, direction)
        else:
            print(f"Drew: {new_card} - not playable, turn passes.")
        return top_card, direction

    while True:
        choice = input("\nCard number to play (or 'draw' to draw a card): ").strip().lower()
        if choice == "draw":
            player.draw(deck, discard)
            print("You drew a card, your turn ends.")
            return top_card, direction
        if choice.isdigit() and 1 <= int(choice) <= len(player.hand):
            idx = int(choice) - 1
            if player.hand[idx].matches(top_card):
                return play_card(player, idx, discard, direction)
            else:
                print("This card doesn't match the top card!")
        else:
            print("Invalid input.")


def play_card(player, idx, discard, direction):
    card = player.hand.pop(idx)
    if card.value in ("Wild", "Wild Draw Four"):
        card.color = choose_wild_color()
    discard.append(card)
    print(f"{player.name} played: {card}")

    if card.value == "Reverse":
        direction *= -1
        print("Direction reversed!")

    return card, direction


def computer_turn(player, deck, discard, top_card, direction):
    print(f"\n{player.name} is thinking...")
    valid_moves = [i for i, c in enumerate(player.hand) if c.matches(top_card)]

    if not valid_moves:
        player.draw(deck, discard)
        new_card = player.hand[-1]
        if new_card.matches(top_card):
            return play_card(player, len(player.hand) - 1, discard, direction)
        print(f"{player.name} had no valid card and drew one.")
        return top_card, direction

    # Simple strategy: play the first valid card found
    idx = valid_moves[0]
    return play_card(player, idx, discard, direction)


def apply_action_effects(card, current_idx, players, deck, discard):
    """Applies action card effects to the next player, returns the next player's index"""
    n = len(players)
    next_idx = current_idx

    if card.value == "Skip":
        next_idx = (next_idx + 1) % n
        print(f"{players[next_idx].name}'s turn was skipped!")
    elif card.value == "Draw Two":
        next_idx = (next_idx + 1) % n
        players[next_idx].draw(deck, discard, 2)
        print(f"{players[next_idx].name} drew 2 cards and was skipped!")
    elif card.value == "Wild Draw Four":
        next_idx = (next_idx + 1) % n
        players[next_idx].draw(deck, discard, 4)
        print(f"{players[next_idx].name} drew 4 cards and was skipped!")

    return next_idx


def main():
    print("=" * 40)
    print("Welcome to UNO!")
    print("=" * 40)

    name = input("What's your name? ").strip() or "Player"
    players = [Player(name, is_human=True), Player("Computer", is_human=False)]

    deck = build_deck()
    discard = []

    for p in players:
        p.draw(deck, discard, 7)

    first_card = deck.pop()
    while first_card.color is None:
        deck.insert(0, first_card)
        first_card = deck.pop()
    discard.append(first_card)
    top_card = first_card

    current_idx = 0
    direction = 1

    while True:
        player = players[current_idx]

        if player.is_human:
            top_card, direction = human_turn(player, deck, discard, top_card, direction)
        else:
            top_card, direction = computer_turn(player, deck, discard, top_card, direction)

        if len(player.hand) == 0:
            print(f"\n🎉 {player.name} wins! Congratulations! 🎉")
            break

        if len(player.hand) == 1:
            print(f"⚠️  {player.name} has only one card left! UNO!")

        current_idx = apply_action_effects(top_card, current_idx, players, deck, discard)
        current_idx = (current_idx + direction) % len(players)


if __name__ == "__main__":
    main()