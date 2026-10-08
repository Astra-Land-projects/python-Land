"""
بازی UNO کنسولی - پایتون
یک نفره در برابر کامپیوتر (AI ساده)
"""

import random

COLORS = ["قرمز", "آبی", "سبز", "زرد"]
NUMBERS = list(range(0, 10))
ACTIONS = ["رد شو", "برعکس", "بکش+۲"]
WILDS = ["رنگ آزاد", "رنگ آزاد+۴"]


class Card:
    def __init__(self, color, value):
        self.color = color   # یکی از COLORS یا None برای وایلد
        self.value = value   # عدد، اکشن یا وایلد

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
    print("رنگ جدید رو انتخاب کن:")
    for i, c in enumerate(COLORS):
        print(f"{i + 1}. {c}")
    while True:
        choice = input("شماره رنگ: ").strip()
        if choice in ["1", "2", "3", "4"]:
            return COLORS[int(choice) - 1]
        print("عدد نامعتبره، دوباره امتحان کن.")


def print_hand(player):
    print(f"\nکارت‌های {player.name}:")
    for i, c in enumerate(player.hand):
        print(f"  {i + 1}. {c}")


def human_turn(player, deck, discard, top_card, direction):
    print_hand(player)
    print(f"\nکارت روی میز: {top_card}")

    valid_moves = [i for i, c in enumerate(player.hand) if c.matches(top_card)]

    if not valid_moves:
        print(f"{player.name} کارت قابل بازی نداره، یه کارت می‌کشه...")
        player.draw(deck, discard)
        new_card = player.hand[-1]
        if new_card.matches(top_card):
            print(f"کارت کشیدی: {new_card} - قابل بازیه!")
            play = input("می‌خوای بازیش کنی؟ (بله/نه): ").strip()
            if play == "بله":
                return play_card(player, len(player.hand) - 1, discard, direction)
        else:
            print(f"کارت کشیدی: {new_card} - قابل بازی نیست، نوبت رد شد.")
        return top_card, direction

    while True:
        choice = input("\nشماره کارتی که می‌خوای بازی کنی (یا 'بکش' برای کشیدن کارت): ").strip()
        if choice == "بکش":
            player.draw(deck, discard)
            print("یه کارت کشیدی، نوبتت تموم شد.")
            return top_card, direction
        if choice.isdigit() and 1 <= int(choice) <= len(player.hand):
            idx = int(choice) - 1
            if player.hand[idx].matches(top_card):
                return play_card(player, idx, discard, direction)
            else:
                print("این کارت با کارت روی میز نمی‌خونه!")
        else:
            print("ورودی نامعتبره.")


def play_card(player, idx, discard, direction):
    card = player.hand.pop(idx)
    if card.value == "رنگ آزاد":
        card.color = choose_wild_color()
    elif card.value == "رنگ آزاد+۴":
        card.color = choose_wild_color()
    discard.append(card)
    print(f"{player.name} بازی کرد: {card}")

    if card.value == "برعکس":
        direction *= -1
        print("جهت بازی برعکس شد!")

    return card, direction


def computer_turn(player, deck, discard, top_card, direction):
    print(f"\n{player.name} داره فکر می‌کنه...")
    valid_moves = [i for i, c in enumerate(player.hand) if c.matches(top_card)]

    if not valid_moves:
        player.draw(deck, discard)
        new_card = player.hand[-1]
        if new_card.matches(top_card):
            return play_card(player, len(player.hand) - 1, discard, direction)
        print(f"{player.name} کارت قابل بازی نداشت و یه کارت کشید.")
        return top_card, direction

    # ساده: اول کارت‌های عددی رو بازی کن، رنگ‌ها رو برای آخر نگه دار
    idx = valid_moves[0]
    return play_card(player, idx, discard, direction)


def apply_action_effects(card, current_idx, players, deck, discard):
    """اثر کارت‌های اکشن رو روی نفر بعدی اعمال می‌کنه، ایندکس نفر بعدی رو برمی‌گردونه"""
    n = len(players)
    next_idx = current_idx

    if card.value == "رد شو":
        next_idx = (next_idx + 1) % n
        print(f"{players[next_idx].name} نوبتش رد شد!")
    elif card.value == "بکش+۲":
        next_idx = (next_idx + 1) % n
        players[next_idx].draw(deck, discard, 2)
        print(f"{players[next_idx].name} دو تا کارت کشید و نوبتش رد شد!")
    elif card.value == "رنگ آزاد+۴":
        next_idx = (next_idx + 1) % n
        players[next_idx].draw(deck, discard, 4)
        print(f"{players[next_idx].name} چهار تا کارت کشید و نوبتش رد شد!")

    return next_idx


def main():
    print("=" * 40)
    print("به بازی UNO خوش اومدی!")
    print("=" * 40)

    name = input("اسمت چیه؟ ").strip() or "بازیکن"
    players = [Player(name, is_human=True), Player("کامپیوتر", is_human=False)]

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
            print(f"\n🎉 {player.name} برنده شد! تبریک می‌گم! 🎉")
            break

        if len(player.hand) == 1:
            print(f"⚠️  {player.name} فقط یه کارت داره! UNO!")

        current_idx = apply_action_effects(top_card, current_idx, players, deck, discard)
        current_idx = (current_idx + direction) % len(players)


if __name__ == "__main__":
    main()