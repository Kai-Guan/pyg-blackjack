from settings import *
from player import Player
from shoe import Shoe

#controller for dealing cards, managing bets, and resolving hands

class Dealer():
    def __init__(self, players:int) -> None:
        self.players = [Player(i) for i in range(players)]
        self.shoe = Shoe()
        
    def newGame(self) -> None:
        self.shoe.regenerateShoe()
        for player in self.players:
            player.hand.resetHand()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            
    def _dealCard(self, player:Player) -> None:
        player.hand.cards.append(self.shoe.drawCard())