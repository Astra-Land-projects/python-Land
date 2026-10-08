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
    print("\n🎴 Welcome to Four-Player Card Battle! 🎴")
    print("Rules: Highest card wins. Ace (14) is strongest.")
    print("-" * 50)
   
    player1 = input("Enter name for Human Player 1: ").strip()
    player2 = input("Enter name for Human Player 2: ").strip()
   
    if not player1:
        player1 = "Human 1"
    if not player2:
        player2 = "Human 2"
   
    return player1, player2

def play_round(deck, player1_name, player2_name):
    """Play one round of the four-player game"""
    print("\n🎯 Dealing cards...")
    time.sleep(1)
   
    # Deal cards to all four players
    player1_card = deck.deal_one()
    player2_card = deck.deal_one()
    computer1_card = deck.deal_one()
    computer2_card = deck.deal_one()
   
    # Display cards in a 2x2 grid layout
    print("\n" + "="*50)
    print("CARDS ON TABLE:")
    print("="*50)
   
    # First row: Human players
    print(f"\n👥 HUMAN PLAYERS:")
    print_card(player1_card, player1_name)
    print_card(player2_card, player2_name)
   
    # Second row: Computer players
    print(f"\n🤖 COMPUTER PLAYERS:")
    print_card(computer1_card, "Computer Alpha")
    print_card(computer2_card, "Computer Beta")
   
    # Compare values
    print("\n🔍 Comparing values...")
    time.sleep(1.5)
   
    # Find highest card
    players = [
        (player1_name, player1_card),
        (player2_name, player2_card),
        ("Computer Alpha", computer1_card),
        ("Computer Beta", computer2_card)
    ]
   
    # Sort by card value descending
    sorted_players = sorted(players, key=lambda x: x[1].value, reverse=True)
   
    winner_name = sorted_players[0][0]
    winner_card = sorted_players[0][1]
   
    # Check for ties
    tie_players = []
    for i in range(1, len(sorted_players)):
        if sorted_players[i][1].value == sorted_players[0][1].value:
            tie_players.append(sorted_players[i][0])
   
    if tie_players:
        tie_players.append(winner_name)
        winner_name = "Tie between " + ", ".join(sorted(tie_players))
   
    # Display results
    print("\n🏆 Results:")
    for name, card in players:
        print(f"{name}: {card} (Value: {card.value})")
    print(f"\n🎉 Winner: {winner_name} with {winner_card}!")
   
    return winner_name, players

def main_game():
    """Main game loop for four players"""
    player1_name, player2_name = get_player_names()
   
    deck = Deck()
    deck.shuffle()
   
    round_count = 0
    scores = {
        player1_name: 0,
        player2_name: 0,
        "Computer Alpha": 0,
        "Computer Beta": 0
    }
   
    while True:
        round_count += 1
        print(f"\n{'='*60}")
        print(f"ROUND {round_count}")
        print(f"{'='*60}")
       
        winner, players = play_round(deck, player1_name, player2_name)
       
        # Update scores
        if "Tie between" in winner:
            # Extract player names from tie string
            tie_names = winner.replace("Tie between ", "").split(", ")
            for name in tie_names:
                if name in scores:
                    scores[name] += 0.5  # Half point for tie
        elif winner in scores:
            scores[winner] += 1
       
        # Display current scores
        print("\n📊 CURRENT SCORES:")
        print("-" * 30)
        for player, score in scores.items():
            print(f"{player:<20}: {score:>3} points")
       
        # Check if deck has enough cards for next round
        if len(deck.cards) < 4:
            print("\n⚠️ Deck is empty! Game over.")
            break
       
        # Ask to continue
        choice = input("\nPlay another round? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
   
    # Final results
    print(f"\n{'='*60}")
    print("FINAL RESULTS")
    print(f"{'='*60}")
   
    # Sort players by score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
   
    print("\n🏅 FINAL STANDINGS:")
    for rank, (player, score) in enumerate(sorted_scores, 1):
        medal = ""
        if rank == 1:
            medal = "🥇 "
        elif rank == 2:
            medal = "🥈 "
        elif rank == 3:
            medal = "🥉 "
        print(f"{medal}{rank}. {player:<20}: {score:>3} points")
   
    # Determine overall winner(s)
    max_score = sorted_scores[0][1]
    winners = [player for player, score in scores.items() if score == max_score]
   
    if len(winners) == 1:
        print(f"\n🏆 OVERALL CHAMPION: {winners[0]}! 🏆")
    else:
        print(f"\n🏆 OVERALL CHAMPIONS: Tie between {', '.join(winners)}! 🏆")
   
    print("\nThanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    main_game()