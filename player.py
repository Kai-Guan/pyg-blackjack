from settings import *
from hand import Hand

class Player():
    def __init__(self, num:int) -> None:
        self.num = num
        self.hand = Hand(num)
        self.purse = STARTING_MONEY