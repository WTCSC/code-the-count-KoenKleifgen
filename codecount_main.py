import random
from codecount import cardcounter

def main():
    print("Welcome to a totally normal Blackjack game!")
    counter = cardcounter()
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    player_hand = [random.choice(cards), random.choice(cards)]
    print(f"Your starting hand: {player_hand}")
    for card in player_hand:
        counter.add_card(card)
    dealer_card = random.choice(cards)
    print(f"Dealer's visible card: {dealer_card}")
    print(f"Current Running Count: {counter.running_count}")
    print(f"Current True Count: {counter.true_count()}")
    print(f"Total Hand Value: {counter.hand_value(player_hand)}")
    if counter.hand_value(player_hand) > 21:
        print("Bust! You lose!")
        return
    recommendation = counter.recommend_action(player_hand, dealer_card)
    print(f"Recommendation: {recommendation}")

    while True:
        action = input("Enter 'hit' to draw a card, 'stand' to hold, or 'quit' to exit: ").strip().lower()
        if action == 'quit':
            print("Thanks for playing!")
            break
        elif action not in ['hit', 'stand']:
            print("Invalid action. Please enter 'hit', 'stand', or 'quit'.")
            continue
        if action == 'hit':
            new_card = random.choice(cards)
            print(f"You drew: {new_card}")
            player_hand.append(new_card)
            counter.add_card(new_card)
        print(f"Your hand now: {player_hand}")
        print(f"Current Running Count: {counter.running_count}")
        print(f"Current True Count: {counter.true_count()}")
        print(f"Total Hand Value: {counter.hand_value(player_hand)}")
        if counter.hand_value(player_hand) > 21:
            print("Bust! You lose!")
            break
        recommendation = counter.recommend_action(player_hand, dealer_card)
        print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()