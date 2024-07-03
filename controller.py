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
            
    def _nextHand(self) -> None:
        if self.currentHandNo == len(self.players[self.currentPlayerNo].hands) - 1:
            self.currentHandNo = 0
            self.nextPlayer()
        else:
            self.currentHandNo += 1
        
    def newGame(self) -> None:
        self.shoe.regenerateShoe()
        self.shoe.customShoe(CUSTOM_SHOE)
        for player in self.players:
            player.resetHands()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            
    def _dealCard(self, player:Player) -> None:
        player.hands[self.currentHandNo].cards.append(self.shoe.drawCard())
        
    def actionNumber(self, number:int) -> None:
        #raise NotImplementedError
        match number:
            case 1: return self._actionHit()
            case 2: return self._actionStand()
            case 3: return self._actionDouble()
            case 4: return self._actionSplit()
            case 5: return self._nextHand()
            
    def _actionHit(self) -> None:
        #raise NotImplementedError
        self._dealCard(self.players[self.currentPlayerNo])
        self.players[self.currentPlayerNo].hands[self.currentHandNo].update()
        
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
        self.players[self.currentPlayerNo].split(self.currentHandNo)
        self.players[self.currentPlayerNo].hands[self.currentHandNo].cards.append(self.shoe.drawCard())
        self.players[self.currentPlayerNo].hands[self.currentHandNo+1].cards.append(self.shoe.drawCard())

    def _drawPlayers(self, WINDOW) -> None:
        for pN in range(len(self.players)):
            
            if len(self.players[pN].hands) == 1:  
                
                if self.currentPlayerNo == pN:
                    pygame.draw.circle(WINDOW, RED, (WIDTH- ( ((self.currentPlayerNo+1)/(len(self.players)+1)) *WIDTH)-33, HEIGHT*0.335), 20)
                     
                for cN in range(len(self.players[pN].hands[0].cards)):
                    drawCard(WINDOW,
                            self.players[pN].hands[0].cards[cN],
                            (
                            WIDTH - (WIDTH/(len(self.players)+1))*(pN+1),
                            HEIGHT*(0.4+cN*0.03)
                            )
                    )

            else:
                #draw split hands
                for hN in range(len(self.players[pN].hands)):
                    if self.currentPlayerNo == pN and self.currentHandNo == hN:
                        pygame.draw.circle(WINDOW, RED, (WIDTH - (((WIDTH/(len(self.players)+1))*2)/(len(self.players[pN].hands)+1)*(hN+1)+((WIDTH/(len(self.players)+1))*(pN)))-33, HEIGHT*0.335), 20)
                    for cN in range(len(self.players[pN].hands[hN].cards)):
                        drawCard(WINDOW,
                                self.players[pN].hands[hN].cards[cN],
                                (
                                WIDTH - (((WIDTH/(len(self.players)+1))*2)/(len(self.players[pN].hands)+1)*(hN+1)+((WIDTH/(len(self.players)+1))*(pN))),
                                HEIGHT*(0.4+cN*0.03)
                                )
                        )
                
     
    def update(self, WINDOW) -> None:
        self._drawPlayers(WINDOW)