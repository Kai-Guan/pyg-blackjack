from settings import *
from hand import Hand

class Player():
    def __init__(self, num:int) -> None:
        self.num = num
        self.hands = [Hand()] #list of hands
        self.purse = STARTING_MONEY
        
    def init_split(self) -> None:
        self.hands = [Hand(self.hands[0].cards[0], True), Hand(self.hands[0].cards[1], True)]
        
    def resetHands(self) -> None:
        self.hands = [Hand()]