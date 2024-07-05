from settings import *
from player import Player
from shoe import Shoe
from card import *
from dealer import Dealer
from textRenderer import renderText
from input_text import InputBox

import random

#controller for dealing cards, managing bets, and resolving hands

class Controller():
    def __init__(self, players:int) -> None:
        self.players = [Player(i) for i in range(players)]
        self.players[1].purse = 5
        self.currentPlayerNo = -3
        self.currentHandNo = 0
        self.shoe = Shoe()
        self.dealer = Dealer(self.players, self.shoe)
        
        self.start_tick=pygame.time.get_ticks()
        self.seconds = self.start_tick/1000
        self.events = []
        
        self.input_boxes = [InputBox(p) for p in self.players]
        
    def newGame(self, customShoe:bool = False) -> None:
        self.shoe.regenerateShoe()
        if customShoe: self.shoe.customShoe(CUSTOM_SHOE)
        for player in self.players:
            player.resetHands()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            self.dealer.cards.append(self.shoe.drawCard())
            
    def _newRound(self) -> None:
        for player in self.players:
            player.purse -= player.bet
        self.dealer.resetHand()
        for player in self.players:
            player.resetHands()
        for _ in range(2):
            for player in self.players:
                self._dealCard(player)
            self.dealer.cards.append(self.shoe.drawCard())
        self.currentPlayerNo = 0
        if self.players[self.currentPlayerNo].purse == 0 and self.players[self.currentPlayerNo].bet == 0:
            self.nextPlayer()
        self.currentHandNo = 0
        
    def nextPlayer(self) -> None:
        if self.currentPlayerNo == len(self.players) - 1:
            self.currentPlayerNo = -1
            self.start_tick = pygame.time.get_ticks()
        elif self.players[self.currentPlayerNo+1].purse == 0 and self.players[self.currentPlayerNo+1].bet == 0:
            self.currentPlayerNo += 1
            self.nextPlayer()
        else:
            self.currentPlayerNo += 1
        self.currentHandNo = 0
            
    def _nextHand(self) -> None:
        if self.currentHandNo == len(self.players[self.currentPlayerNo].hands) - 1:
            self.currentHandNo = 0
            self.nextPlayer()
        else:
            self.currentHandNo += 1

    def _dealCard(self, player:Player) -> None:
        player.hands[self.currentHandNo].cards.append(self.shoe.drawCard())
        
    def actionNumber(self, number:int) -> None:
        #raise NotImplementedError
        match number:
            case 1: return self._actionHit()
            case 2: return self._actionStand()
            case 3: return self._actionDouble()
            case 4: return self._actionSplit()
            case 5: return self._actionInsure()
            case 6: return self._nextHand()
            
    def _actionInsure(self) -> None:
        raise NotImplementedError
            
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
        self.players[self.currentPlayerNo].hands[self.currentHandNo].bet *= 2
        self._nextHand()

    def _actionSplit(self) -> None:
        self.players[self.currentPlayerNo].split(self.currentHandNo)
        self.players[self.currentPlayerNo].hands[self.currentHandNo].cards.append(self.shoe.drawCard())
        self.players[self.currentPlayerNo].hands[self.currentHandNo+1].cards.append(self.shoe.drawCard())

    def _drawPlayers(self, WINDOW, W, H) -> None:
        for pN, player in enumerate(self.players):
            if player.purse == 0 and player.bet == 0:
                continue
            for hN in range(len(player.hands)):
                if self.currentPlayerNo == pN and self.currentHandNo == hN:
                    pygame.draw.circle(WINDOW, RED, (W - (((W/(len(self.players)+1))*2)/(len(player.hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN)))-(W*0.024), H*0.385), 20)
                for cN in range(len(player.hands[hN].cards)):
                    drawCard(WINDOW,
                        player.hands[hN].cards[cN],
                        (
                        W - (((W/(len(self.players)+1))*2)/(len(player.hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN))) + cN*0.005*W,
                        H*(0.45+cN*0.03),
                        ),
                        rotated=(player.hands[hN].doubled and cN == len(player.hands[hN].cards)-1)
                    )

                renderText(WINDOW,
                    (
                    W - (((W/(len(self.players)+1))*2)/(len(player.hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN))),
                    H*(0.35)
                    ),
                    f"{"H" if player.hands[hN].calcValue()[1] else "S"}{player.hands[hN].calcValue()[0]}", int(H*0.025), colour=WHITE)
                            
    def _drawDealer(self, WINDOW, W, H) -> None:
        for cN in range(len(self.dealer.cards)):
            if cN == 0 and (self.currentPlayerNo not in [-1, -2]):
                drawCard(WINDOW, self.dealer.cards[cN], (W*0.5, H*0.15), faceDown=True)
            else:
                drawCard(WINDOW, self.dealer.cards[cN], ((W*0.5 + cN*0.005*W), H*(0.15+cN*0.03)))
                
        if self.currentPlayerNo in [-1, -2]:
            renderText(WINDOW, (W*0.5, H*0.04), str(self.dealer.calcValue()[0]), int(H*0.025), colour=WHITE)
            if self.dealer.calcValue()[0] > 21:
                renderText(WINDOW, (W*0.5, H*0.06), "BUST", int(H*0.025), colour=WHITE)
                
    def _drawPurses(self, WINDOW, W, H):
        rect = pygame.Rect(W*0.67, H*0.05, W*0.25, H*0.25)
        pygame.draw.rect(WINDOW, GREY, rect, 0, 5)
        pygame.draw.rect(WINDOW, YELLOW, rect, 2, 5)
        
        for pN, player in enumerate(self.players):
            if player.purse == 0 and player.bet == 0: p = "BUST"
            else: p = f"${player.purse}"
            renderText(WINDOW, (W*0.68, H*0.07 + pN*(H*0.05+H*0.25)/(len(self.players)+1)), f"Player {player.num+1}: {p}", int(H*0.025), colour=WHITE, centered = False)
            
    def _drawPursesCentered(self, WINDOW, W, H):
        rect = pygame.Rect(W*0.67, H*0.05, W*0.25, H*0.25)
        rect.center = (W/2, H*0.25)
        pygame.draw.rect(WINDOW, GREY, rect, 0, 5)
        pygame.draw.rect(WINDOW, YELLOW, rect, 2, 5)
        
        for pN, player in enumerate(self.players):
            if player.purse == 0: p = "BUST"
            else: p = f"${player.purse}"
            renderText(WINDOW, (W*0.38, H*0.13 + pN*(H*0.05+H*0.25)/(len(self.players)+1)), f"Player {player.num+1}: {p}", int(H*0.025), colour=WHITE, centered = False)
            
    def _drawBets(self, WINDOW, W, H):
        for pN, player in enumerate(self.players):
            if player.purse == 0 and player.bet == 0:
                continue
            
            for hN, hand in enumerate(player.hands):
                if hand.bet == 0:
                    #continue
                    pass
                renderText(WINDOW, (
                        W - (((W/(len(self.players)+1))*2)/(len(player.hands)+1)*(hN+1)+((W/(len(self.players)+1))*(pN))),
                        H*(0.60)+len(hand.cards)*0.03*H,
                        ), f"${hand.bet}", int(H*0.025), colour=WHITE)
    
    def update(self, WINDOW) -> None:
        self.seconds=(pygame.time.get_ticks()-self.start_tick)/1000
        W, H = WINDOW.get_size()
        if self.currentPlayerNo != -3:
            self._drawPlayers(WINDOW, W, H)
            self._drawDealer(WINDOW, W, H)
            if self.currentPlayerNo != -2: self._drawBets(WINDOW, W, H)
            self._drawPurses(WINDOW, W, H)
        
        if self.currentPlayerNo == -1:
            if self.sleep(random.uniform(1, 2)):
                self.dealer.getAction()
                if self.dealer.getAction() == "hit":
                    self.dealer.hit()
                    self.start_tick = pygame.time.get_ticks()
                elif self.dealer.getAction() == "stand":
                    self._endGame()
                    
        if self.currentPlayerNo == -2:
            if self.sleep(5):
                self.currentPlayerNo = -3
                
        if self.currentPlayerNo == -3:
            self._drawPursesCentered(WINDOW, W, H)
            self._placeBets(WINDOW, W, H)

        
    def sleep(self, seconds:int) -> bool:
        if self.seconds >= seconds:
            return True
        
    def _placeBets(self, WINDOW, W, H) -> None:
        for event in self.events:
            for bN, box in enumerate(self.input_boxes):
                if self.players[bN].purse == 0:
                    continue
                box.handle_event(event)
        for bN, box in enumerate(self.input_boxes):
            if self.players[bN].purse == 0:
                renderText(WINDOW, (W-((W/(len(self.input_boxes)+1))*(bN+1)), H*0.45), f"Player {bN+1} BUST", int(H*0.025), colour=WHITE)
                continue
            box.update(WINDOW, (W-((W/(len(self.input_boxes)+1))*(bN+1)), H*0.5), W*0.1, H*0.05)
            renderText(WINDOW, (W-((W/(len(self.input_boxes)+1))*(bN+1)), H*0.45), f"Player {bN+1} Bet", int(H*0.025), colour=WHITE)
        for pN, player in enumerate(self.players):
            if player.purse == 0:
                continue
            if player.provisionalBet != 0:
                if player.provisionalBet > player.purse:
                    player.provisionalBet = player.purse
                renderText(WINDOW, (W-((W/(len(self.players)+1))*(pN+1)), H*0.55), f"{player.provisionalBet}", int(H*0.025), colour=WHITE)
        if all(player.provisionalBet != 0 for player in self.players if player.purse != 0):
            for pN, player in enumerate(self.players):
                player.bet = player.provisionalBet
            self._newRound()

    def _endGame(self) -> None:
        for player in self.players:
            reward = player.getReward(self.dealer.calcValue()[0], (self.dealer.calcValue()[0] == 21 and len(self.dealer.cards) == 2))
            if reward > 0:
                player.purse += reward
            if reward < 0 and player.purse+reward <= 0:
                player.purse = 0
        self.currentPlayerNo = -2