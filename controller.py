from settings import *
from player import Player
from shoe import Shoe
from card import *

#controller for dealing cards, managing bets, and resolving hands

class Dealer():
    def __init__(self, players:int) -> None:
        self.players = [Player(i) for i in range(players)]
        self.currentPlayerNo = 0
        self.currentHandNo = 0
        self.shoe = Shoe()
        
    def nextPlayer(self) -> None:
        if self.currentPlayerNo == len(self.players) - 1:
            self.currentPlayerNo = -1
            self.currentHandNo = 0
        else:
            self.currentPlayerNo += 1
            self.currentHandNo = 0
        
    def newGame(self) -> None:
        self.shoe.regenerateShoe()
        for player in self.players:
            player.resetHands()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            
    def _dealCard(self, player:Player, handNo = None) -> None:
        if handNo:
            player.hands[handNo].cards.append(self.shoe.drawCard())
        else:
            player.hands[0].cards.append(self.shoe.drawCard())
        
    def actionNumber(self, number:int) -> None:
        #raise NotImplementedError
        match number:
            case 1: return self._actionHit()
            case 2: return self._actionStand()
            case 3: return self._actionDouble()
            case 4: return self._actionSplit()
            
    def _actionHit(self) -> None:
        raise NotImplementedError
        self._dealCard(self.players[self.currentPlayerNo])
        self.players[self.currentPlayerNo].hand.update()
        
    def _actionStand(self) -> None:
        #special case for split hands
        if len(self.players[self.currentPlayerNo].hands) > 1:
            if self.currentHandNo != len(self.players[self.currentPlayerNo].hands)-1:
                self.players[self.currentPlayerNo].hands[self.currentHandNo].stood = True    
             
                self.currentHandNo += 1
                return
        self.players[self.currentPlayerNo].hands[0].stood = True
        self.nextPlayer()
        
    def _actionDouble(self) -> None:
        raise NotImplementedError
        self._dealCard(self.players[self.currentPlayerNo])
        self.players[self.currentPlayerNo].hand.doubled = True
        self.players[self.currentPlayerNo].hand.stood = True
        self.players[self.currentPlayerNo].hand.update()
        self.nextPlayer()
        
    def _actionSplit(self) -> None:
        self.players[self.currentPlayerNo].init_split()
        for hand in self.players[self.currentPlayerNo].hands:
            hand.cards.append(self.shoe.drawCard())

            

    '''def _draw(self, WINDOW) -> None:
        #draw cards for every player
        if self.currentPlayerNo != -1: pygame.draw.circle(WINDOW, RED, (WIDTH- ( ((self.currentPlayerNo+1)/(len(self.players)+1)) *WIDTH)-33, HEIGHT*0.335), 30)
        for pN, player in enumerate(self.players): #playerNumber
            for cN,card in enumerate(player.hand.cards): #cardNumber
                drawCard(WINDOW, card, ( (WIDTH- ( ((pN+1)/(len(self.players)+1)) *WIDTH)+ (cN*0.01*WIDTH)),  HEIGHT*(0.4+cN*0.03)  ))'''
                
    #new _draw function to draw split hands aswell, but a split hand uses the same space as the original hand, e.g. 2 hands in the space of one
    #don't draw original hands if split hands is drawn
    def _draw(self, WINDOW) -> None:
        #draw a red dot on the current hand if the current hand is not -1
        if self.currentPlayerNo != -1: pygame.draw.circle(WINDOW, RED, (WIDTH- ( ((self.currentPlayerNo+1)/(len(self.players)+1)) *WIDTH)-33, HEIGHT*0.335), 30)
        for pN, player in enumerate(self.players):
            for hN, hand in enumerate(player.hands):
                for cN,card in enumerate(hand.cards):
                    #drawCard(WINDOW, card, ( (WIDTH- ( ((pN+1)/(len(self.players)+1)) *WIDTH)+ (cN*0.01*WIDTH)),  HEIGHT*(0.4+cN*0.03)  ))
                    #belove is above line modified so that split hands are drawn aswell, in the same space as the original hand
                    drawCard(WINDOW, card, ( (WIDTH- ( ((pN+1)/(len(self.players)+1)) *WIDTH)+ (cN*0.01*WIDTH)),  HEIGHT*(0.4+cN*0.03 + hN*0.03)  ))
        
                
    def update(self, WINDOW) -> None:
        self._draw(WINDOW)