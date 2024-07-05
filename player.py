from settings import *
from hand import Hand

class Player():
    def __init__(self, num:int) -> None:
        self.num = num
        self.hands = [Hand()] #list of hands
        self.purse = STARTING_MONEY
        self.bet = 0
        self.provisionalBet = 0
        self.insurance = 0
        
    def split(self, handNo) -> None:
        self.hands.insert(handNo+1, Hand(self.hands[handNo].cards[1], True, bet=self.bet))
        self.hands[handNo] = Hand(self.hands[handNo].cards[0], True, bet=self.bet)
        self.purse -= self.bet
        
    def resetHands(self) -> None:
        self.hands = [Hand(bet = self.bet)]
        self.provisionalBet = 0
        self.insurance = 0
        
    def getReward(self, dealerValue, dealerBlackjack) -> int:
        reward = 0
        for hand in self.hands:
            reward += hand.getReward(dealerValue, dealerBlackjack, insurance = self.insurance)
        return reward