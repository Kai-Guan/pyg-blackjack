from settings import *
from player import Player
from shoe import Shoe
from card import *
from dealer import Dealer
import random

#controller for dealing cards, managing bets, and resolving hands

class Controller():
    def __init__(self, players:int) -> None:
        self.players = [Player(i) for i in range(players)]
        self.currentPlayerNo = 0
        self.currentHandNo = 0
        self.shoe = Shoe()
        self.dealer = Dealer(self.players, self.shoe)
        
        self.start_tick=pygame.time.get_ticks()
        self.seconds = self.start_tick/1000
        
    def nextPlayer(self) -> None:
        if self.currentPlayerNo == len(self.players) - 1:
            self.currentPlayerNo = -1
            self.currentHandNo = 0
            self.start_tick = pygame.time.get_ticks()
        else:
            self.currentPlayerNo += 1
            self.currentHandNo = 0
            
    def _nextHand(self) -> None:
        if self.currentHandNo == len(self.players[self.currentPlayerNo].hands) - 1:
            self.currentHandNo = 0
            self.nextPlayer()
        else:
            self.currentHandNo += 1
        
    def newGame(self, customShoe:bool = False) -> None:
        self.shoe.regenerateShoe()
        if customShoe: self.shoe.customShoe(CUSTOM_SHOE)
        for player in self.players:
            player.resetHands()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            self.dealer.cards.append(self.shoe.drawCard())
            
            
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
        self.players[self.currentPlayerNo].hands[self.currentHandNo].stood = True
        self._nextHand()
        
    def _actionDouble(self) -> None:
        self._actionHit()
        self.players[self.currentPlayerNo].hands[self.currentHandNo].doubled = True
        self.players[self.currentPlayerNo].hands[self.currentHandNo].update()
        self._nextHand()
        
    def _actionSplit(self) -> None:
        self.players[self.currentPlayerNo].split(self.currentHandNo)
        self.players[self.currentPlayerNo].hands[self.currentHandNo].cards.append(self.shoe.drawCard())
        self.players[self.currentPlayerNo].hands[self.currentHandNo+1].cards.append(self.shoe.drawCard())

    def _drawPlayers(self, WINDOW, W, H) -> None:
        for pN in range(len(self.players)):
             
                for hN in range(len(self.players[pN].hands)):
                    if self.currentPlayerNo == pN and self.currentHandNo == hN:
                        pygame.draw.circle(WINDOW, RED, (W - (((W/(len(self.players)+1))*2)/(len(self.players[pN].hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN)))-(W*0.024), H*0.385), 20)
                    for cN in range(len(self.players[pN].hands[hN].cards)):
                        #check if doubled and last card
                        if self.players[pN].hands[hN].doubled and cN == len(self.players[pN].hands[hN].cards)-1:
                            drawCard(WINDOW,
                                self.players[pN].hands[hN].cards[cN],
                                (
                                W - (((W/(len(self.players)+1))*2)/(len(self.players[pN].hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN))) + cN*0.005*W,
                                H*(0.45+cN*0.03),
                                ),
                                rotated=True
                            )
                        else:
                            drawCard(WINDOW,
                                    self.players[pN].hands[hN].cards[cN],
                                    (
                                    W - (((W/(len(self.players)+1))*2)/(len(self.players[pN].hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN))) + cN*0.005*W,
                                    H*(0.45+cN*0.03),
                                    )
                            )
                            
    def _drawDealer(self, WINDOW, W, H) -> None:
        for cN in range(len(self.dealer.cards)):
            if cN == 0 and (self.currentPlayerNo not in [-1, -2]):
                drawCard(WINDOW, self.dealer.cards[cN], (W*0.5, H*0.1), faceDown=True)
            else:
                drawCard(WINDOW, self.dealer.cards[cN], ((W*0.5 + cN*0.005*W), H*(0.1+cN*0.03)))
                
     
    def update(self, WINDOW) -> None:
        self.seconds=(pygame.time.get_ticks()-self.start_tick)/1000
        W, H = WINDOW.get_size()
        self._drawPlayers(WINDOW, W, H)
        self._drawDealer(WINDOW, W, H)
        
        if self.currentPlayerNo == -1:
            if self.sleep(random.uniform(1, 2)):
                self.dealer.getAction()
                if self.dealer.getAction() == "hit":
                    self.dealer.hit()
                    self.start_tick = pygame.time.get_ticks()
                elif self.dealer.getAction() == "stand":
                    print("Dealer Stands")
                    self._endGame()
        
    def sleep(self, seconds:int) -> bool:
        if self.seconds >= seconds:
            return True
        
    def _endGame(self) -> None:
        winners = []
        for player in self.players:
            for hID, hand in enumerate(player.hands):
                if hand.busted:
                    continue
                if self.dealer.calcValue()[0] > hand.calcValue()[0]:
                    continue
                winners.append([player, hand])
        print([f"{player.num} hand {hID}" for player, hand in winners])
        self.currentPlayerNo = -2