from settings import *
from player import Player
from shoe import Shoe
from card import *

#controller for dealing cards, managing bets, and resolving hands

class Dealer():
    def __init__(self, players:int) -> None:
        self.players = [Player(i) for i in range(players)]
        self.currentPlayerNo = 0
        self.shoe = Shoe()
        
    def nextPlayer(self) -> None:
        if self.currentPlayerNo == len(self.players) - 1:
            self.currentPlayerNo = 0
        else:
            self.currentPlayerNo += 1  
        
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

    def draw(self, WINDOW) -> None:
        #draw cards for every player
        pygame.draw.circle(WINDOW, RED, (WIDTH- ( ((self.currentPlayerNo+1)/(len(self.players)+1)) *WIDTH)-33, HEIGHT*0.44), 30)
        for pN, player in enumerate(self.players): #playerNumber
            for cN,card in enumerate(player.hand.cards): #cardNumber
                drawCard(WINDOW, card, ( (WIDTH- ( ((pN+1)/(len(self.players)+1)) *WIDTH)+ (cN*0.01*WIDTH)),  HEIGHT*(0.5+cN*0.03)  ))