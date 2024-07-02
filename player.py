from settings import *
from hand import Hand

class Player():
    def __init__(self, num:int) -> None:
        self.num = num
        self.hands = [Hand()] #list of hands
        self.purse = STARTING_MONEY
        
    def init_split(self) -> None:
        self.hands = [Hand(self.hands.cards[0]), Hand(self.hands.cards[1])]
        
    def resetHands(self) -> None:
        self.hands = [Hand()]