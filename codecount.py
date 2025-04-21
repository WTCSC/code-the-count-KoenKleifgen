class cardcounter:
    def __init__(self):
        self.running_count = 0
        self.dealt = 0

    def add_card(self, card):
        if card in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        elif card in ['10', 'J', 'Q', 'K', 'A']:
            self.running_count -= 1
        self.dealt += 1

    def true_count(self):
        if self.dealt == 0:
            return 0
        return self.running_count / (self.dealt / 52)
    
    def hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                aces += 1
                value += 11
            else:
                value += int(card)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def recommend_action(self, player_hand, dealer_card):
        player_value = self.hand_value(player_hand)
        dealer_value = self.hand_value([dealer_card])
        if player_value >= 21:
            return "stand"
        elif player_value < 12:
            return "hit"
        elif player_value >= 17:
            return "stand"
        elif player_value >= 13 and dealer_value < 7:
            return "stand"
        else:
            return "hit"