from settings import *

#used in player.py

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
        
    def resetHand(self) -> None:
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
        for card in self.cards:
            value += CARD_VALUES[card[0]]
            if self.cards[0] == 1: anyAce = True
        if anyAce and value <= 11: value += 10; hard = False
        return [value, hard]
    
    def getActions(self) -> list:
        actions = []
        if self.busted:
            raise Exception("Not yet implimented")
        if not self.stood:
            actions.append('hit')
            actions.append('stand')
        if len(self.cards) == 2:
            actions.append('double')
            if self.cards[0][0] == self.cards[1][0]:
                actions.append('split')
        return actions