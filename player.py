from settings import *
from hand import Hand

class Player():
    def __init__(self, num:int) -> None:
        self.num = num
        self.hands = [Hand()] #list of hands
        self.purse = STARTING_MONEY
        self.insurance = 0
        
    def split(self, handNo) -> None:
        self.hands.insert(handNo+1, Hand(self.hands[handNo].cards[1], True))
        self.hands[handNo] = Hand(self.hands[handNo].cards[0], True)
        #self.hands[handNo+1].bet = self.hands[handNo].bet
        
    def resetHands(self) -> None:
        self.hands = [Hand()]
        self.insurance = 0