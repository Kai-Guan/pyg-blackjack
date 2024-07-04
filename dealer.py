from settings import *

class Dealer():
    def __init__(self, players:list, shoe) -> None:
        self.players = players
        self.shoe = shoe
        self.cards = []
        
    def calcValue(self) -> list:
        value = 0
        hard = True
        anyAce = False
        for card in self.cards:
            value += CARD_VALUES[card[0]]
            if self.cards[0] == 1: anyAce = True
        if anyAce and value <= 11: value += 10; hard = False
        return [value, hard]
        
    def getAction(self) -> None:
        if self.calcValue()[0] < 17:
            return 'hit'
        else:
            return 'stand'
        
    def hit(self) -> None:
        self.cards.append(self.shoe.drawCard())
        
    def resetHand(self) -> None:
        self.cards = []