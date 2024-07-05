from settings import *

#used in player.py

class Hand():
    def __init__(self, customStartCard = None, isSplitHand = False, bet = 10) -> None:
        self.cards = []
        self.value = [0, True]
        self.bet = bet
        self.insurance = 0
        self.doubled = False
        self.busted = False
        self.blackjack = False
        self.stood = False
        self.isSplitHand = isSplitHand
        if customStartCard:
            self.cards = [customStartCard]
            self.value = self.calcValue()
        
    def resetHand(self) -> None:
        self.cards = []
        self.value = [0, True]
        self.bet = 0
        self.insurance = 0
        self.doubled = False
        self.busted = False
        self.blackjack = False
        self.stood = False
        self.isSplitHand = False
        
    def calcValue(self) -> list:
        value = 0
        hard = True
        anyAce = False
        for card in self.cards:
            value += CARD_VALUES[card[0]]
            if card[0] == 1: anyAce = True
        if anyAce and value <= 11: value += 10; hard = False
        return [value, hard]
    
    def getActions(self) -> list:
        self.update()
        actions = []
        if self.value[0] == 21:
            actions.append('next')
            return actions
        if self.busted:
            actions.append('next')
            return actions
        if not self.stood:
            actions.append('hit')
            actions.append('stand')
            if len(self.cards) == 2:
                if self.isSplitHand == False:
                    actions.append('double')
                if CARD_VALUES[self.cards[0][0]] == CARD_VALUES[self.cards[1][0]]:
                    actions.append('split')
        return actions

    def update(self)->None:
        self.value = self.calcValue()
        if self.value[0] > 21:
            self.busted = True
        if len(self.cards) == 2 and self.value[0] == 21:
            self.blackjack = True
        if self.busted or self.stood:
            self.stood = True
        if self.doubled:
            self.stood = True
        if self.blackjack:
            self.stood = True
            
    def getReward(self, dealerValue, dealerBlackjack, insurance):
        self.update()
        reward = 0
        if self.busted:
            reward -= self.bet
            reward -= insurance
            return reward
        if insurance:
            if dealerBlackjack:
                reward += 2*insurance
            else:
                reward -= insurance
        if self.blackjack:
            if dealerBlackjack:
                reward += self.bet
            else:
                reward += int(round(2.5*self.bet, 0))
        elif dealerValue > 21:
            reward += 2*self.bet
        elif dealerValue < self.value[0]:
            reward += 2*self.bet
        elif dealerValue == self.value[0]:
            reward += self.bet
        return reward