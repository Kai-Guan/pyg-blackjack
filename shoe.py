from settings import *
import random

class Shoe():
    def __init__(self) -> None:
        self.shoe = []
        
    def regenerateShoe(self) -> None:
        for _ in range(DECKS):
            for suit in range(4):
                for number in range(1, 14):
                    self.shoe.append([number, suit])
        random.shuffle(self.shoe)
        
    def customShoe(self, shoe:list) -> None: #testing purposes only
        self.shoe = shoe
        
    def drawCard(self) -> list:
        return self.shoe.pop(0)