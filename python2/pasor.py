import random
import time

# --- تعریف کلاس‌ها و متغیرها ---

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {rank: idx + 2 for idx, rank in enumerate(RANKS)}  # 2=2, ..., Ace=14

# نمادهای گرافیکی برای هر خال
SUITS_SYMBOLS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
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

def print_card(card):
    """نمایش کارت با رنگ و نماد زیبا"""
    symbol = SUITS_SYMBOLS[card.suit]
    # رنگ‌بندی: قرمز برای Hearts و Diamonds، سیاه برای بقیه
    color = "red" if card.suit in ['Hearts', 'Diamonds'] else "black"
   
    # استفاده از ANSI codes برای رنگ (در ترمینال‌های مدرن کار می‌کند)
    if color == "red":
        print(f"\033[91m  ┌─────────┐  \033[0m")
        print(f"\033[91m  │ {card.rank:<2}        │  \033[0m")
        print(f"\033[91m  │         │  \033[0m")
        print(f"\033[91m  │    {symbol}     │  \033[0m")
        print(f"\033[91m  │         │  \033[0m")
        print(f"\033[91m  │        {card.rank:>2} │  \033[0m")
        print(f"\033[91m  └─────────┘  \033[0m")
    else:
        print(f"\033[97m  ┌─────────┐  \033[0m")
        print(f"\033[97m  │ {card.rank:<2}        │  \033[0m")
        print(f"\033[97m  │         │  \033[0m")
        print(f"\033[97m  │    {symbol}     │  \033[0m")
        print(f"\033[97m  │         │  \033[0m")
        print(f"\033[97m  │        {card.rank:>2} │  \033[0m")
        print(f"\033[97m  └─────────┘  \033[0m")

def play_game():
    print("\n🎴 Welcome to Python Card Battle! 🎴")
    print("Rules: Higher card value wins. Ace is highest (14).")
    print("-" * 40)
   
    deck = Deck()
    deck.shuffle()
   
    # بر زدن کارت‌ها
    print("\nShuffling the deck...")
    time.sleep(1)
   
    player_card = deck.deal_one()
    computer_card = deck.deal_one()
   
    # نمایش کارت‌ها
    print("\n👤 Your Card:")
    print_card(player_card)
   
    print("\n🤖 Computer's Card:")
    # کارت کامپیوتر رو برمی‌گردونیم تا پشتش معلوم باشه (شبیه‌سازی)
    # اما اینجا برای سادگی بازی، کارت رو می‌ذاریم رو میز
    print_card(computer_card)
   
    # محاسبه برنده
    print("\n🔍 Comparing values...")
    time.sleep(1.5)
   
    if player_card.value > computer_card.value:
        winner = "Player"
        result_msg = "🎉 You Win! Your card is stronger!"
    elif computer_card.value > player_card.value:
        winner = "Computer"
        result_msg = "🤖 Computer Wins! Better luck next time."
    else:
        winner = "Tie"
        result_msg = "🤝 It's a Tie! Both cards are equal."
   
    print(f"\n{result_msg}")
    print(f"Your Card: {player_card} (Value: {player_card.value})")
    print(f"Computer Card: {computer_card} (Value: {computer_card.value})")
   
    # سوال برای ادامه بازی
    play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")

# اجرای بازی
if __name__ == "__main__":
    play_game()