from settings import *

class Hand():
    def __init__(self, num:int) -> None:
        self.num = num
        self.cards = []
        self.value = [0, True]
        self.bet = 0
        self.insurance = 0
        self.splitHand = False
        self.doubled = False
        self.stood = False
        self.busted = False
        self.blackjack = False
        self.surrendered = False
        
    def calcValue(self) -> list:
        value = 0
        hard = True
        anyAce = False
        for card in self.hand:
            value += CARD_VALUES[card.number]
            if card.number == 1: anyAce = True
        if anyAce and value <= 11: value += 10; hard = False
        self.value = [value, hard]
        return self.value