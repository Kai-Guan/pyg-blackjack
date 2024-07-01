from settings import *
from player import Player
from shoe import Shoe
from card import *

#controller for dealing cards, managing bets, and resolving hands

class Dealer():
    def __init__(self, players:int) -> None:
        self.players = [Player(i) for i in range(players)]
        self.currentPlayer = 0
        self.shoe = Shoe()
        
    def nextPlayer(self) -> None:
        if self.currentPlayer == len(self.players) - 1:
            self.currentPlayer = 0
        else:
            self.currentPlayer += 1  
        
    def newGame(self) -> None:
        self.shoe.regenerateShoe()
        for player in self.players:
            player.hand.resetHand()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            
    def _dealCard(self, player:Player) -> None:
        player.hand.cards.append(self.shoe.drawCard())
        
    def actionNumber(self, number:int) -> None:
        raise NotImplementedError
        match number:
            case 1: return self._actionHit()
            case 2: return self._actionStand()
            case 3: return self._actionDouble()
            case 4: return self._actionSplit()
            
    def draw(self) -> None:
        raise NotImplementedError