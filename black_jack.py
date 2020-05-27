import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # using global vars, create a Card class, to append to deck list
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return 'The deck contains: ' + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


'''
# TEST ONE
test_deck = Deck()
test_deck.shuffle()
print(test_deck)
'''


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card - from class: Deck, method: deal, returns: single_card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # ace default value is 11
        # if total value is less than 21 and player holds an ace, change ace value to 1
        # 'and self.aces' - aces is set to zero, which evaluates to false. self.aces evaluates to true if value is 1.
        while self.value > 21 and self.aces:
            self.value -= 10  # 11aceValue -10aceValue = 1 aceValue
            self.aces -= 1  # reduces 2 aces count back to 1 ace


'''
# TEST TWO
test_deck = Deck()
test_deck.shuffle()
# PLAYER
test_player = Hand()
# DEAL 1 CARD FROM THE DECK
pulled_card = test_deck.deal()
print(f'PULLED CARD: {pulled_card}')
test_player.add_card(pulled_card)
print(f'PLAYER ONE CARD VALUE: {test_player.value}')
# alt
# test_player.add_card(test_deck.deal())
'''


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass
