import random
import time

# --- Constants ---
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {rank: idx + 2 for idx, rank in enumerate(RANKS)}  # 2=2, ..., Ace=14

SUITS_SYMBOLS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

# ANSI colors for terminal display
COLORS = {
    'red': '\033[91m',
    'black': '\033[97m',
    'reset': '\033[0m'
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
   
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
   
    def shuffle(self):
        random.shuffle(self.cards)
   
    def deal_one(self):
        return self.cards.pop()

def print_card(card, player_name=""):
    """Display a card with color and symbol"""
    symbol = SUITS_SYMBOLS[card.suit]
    color = "red" if card.suit in ['Hearts', 'Diamonds'] else "black"
   
    # Display player name above card
    if player_name:
        print(f"\n{player_name}:")
   
    # Card graphic with ANSI colors
    color_code = COLORS[color]
    reset_code = COLORS['reset']
   
    print(f"{color_code}  ┌─────────┐  {reset_code}")
    print(f"{color_code}  │ {card.rank:<2}        │  {reset_code}")
    print(f"{color_code}  │         │  {reset_code}")
    print(f"{color_code}  │    {symbol}     │  {reset_code}")
    print(f"{color_code}  │         │  {reset_code}")
    print(f"{color_code}  │        {card.rank:>2} │  {reset_code}")
    print(f"{color_code}  └─────────┘  {reset_code}")

def get_player_names():
    """Get names for two human players"""
    print("\n🎴 Welcome to Three-Player Card Battle! 🎴")
    print("Rules: Highest card wins. Ace (14) is strongest.")
    print("-" * 40)
   
    player1 = input("Enter name for Player 1: ").strip()
    player2 = input("Enter name for Player 2: ").strip()
   
    if not player1:
        player1 = "Player 1"
    if not player2:
        player2 = "Player 2"
   
    return player1, player2

def play_round(deck, player1_name, player2_name):
    """Play one round of the three-player game"""
    print("\n🎯 Dealing cards...")
    time.sleep(1)
   
    # Deal cards to all three players
    player1_card = deck.deal_one()
    player2_card = deck.deal_one()
    computer_card = deck.deal_one()
   
    # Display cards
    print_card(player1_card, player1_name)
    print_card(player2_card, player2_name)
    print_card(computer_card, "Computer")
   
    # Compare values
    print("\n🔍 Comparing values...")
    time.sleep(1.5)
   
    # Find highest card
    cards = [
        (player1_name, player1_card),
        (player2_name, player2_card),
        ("Computer", computer_card)
    ]
   
    # Sort by card value descending
    sorted_cards = sorted(cards, key=lambda x: x[1].value, reverse=True)
   
    winner_name = sorted_cards[0][0]
    winner_card = sorted_cards[0][1]
   
    # Check for ties (if top two have equal values)
    if sorted_cards[0][1].value == sorted_cards[1][1].value:
        winner_name = "Tie between " + sorted_cards[0][0] + " and " + sorted_cards[1][0]
   
    # Display results
    print("\n🏆 Results:")
    print(f"{player1_name}: {player1_card} (Value: {player1_card.value})")
    print(f"{player2_name}: {player2_card} (Value: {player2_card.value})")
    print(f"Computer: {computer_card} (Value: {computer_card.value})")
    print(f"\n🎉 Winner: {winner_name} with {winner_card}!")
   
    return winner_name

def main_game():
    """Main game loop"""
    player1_name, player2_name = get_player_names()
   
    deck = Deck()
    deck.shuffle()
   
    round_count = 0
    scores = {
        player1_name: 0,
        player2_name: 0,
        "Computer": 0
    }
   
    while True:
        round_count += 1
        print(f"\n════════════════════════════════════════")
        print(f"Round {round_count}")
        print(f"════════════════════════════════════════")
       
        winner = play_round(deck, player1_name, player2_name)
       
        # Update scores (if not a tie)
        if winner != "Computer" and winner not in [player1_name, player2_name]:
            # It's a tie between two players
            tie_players = winner.replace("Tie between ", "").split(" and ")
            for player in tie_players:
                scores[player] += 0.5  # Half point for tie
        elif winner in scores:
            scores[winner] += 1
       
        # Display current scores
        print("\n📊 Current Scores:")
        for player, score in scores.items():
            print(f"{player}: {score} points")
       
        # Check if deck has enough cards for next round
        if len(deck.cards) < 3:
            print("\n⚠️ Deck is empty! Game over.")
            break
       
        # Ask to continue
        choice = input("\nPlay another round? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
   
    # Final results
    print("\n════════════════════════════════════════")
    print("Final Results:")
    print("════════════════════════════════════════")
    for player, score in scores.items():
        print(f"{player}: {score} points")
   
    # Determine overall winner
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]
   
    if len(winners) == 1:
        print(f"\n🏆 Overall Winner: {winners[0]}!")
    else:
        print(f"\n🏆 Overall Winners: Tie between {', '.join(winners)}!")
   
    print("\nThanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    main_game()