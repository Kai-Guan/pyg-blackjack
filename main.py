from settings import *
from player import Player
from button import Button
from controller import Dealer
from card import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('blackjack')
clock = pygame.time.Clock()

controller = Dealer(2)

controller.newGame()

playerChoiceButtons = [
    Button(i+1)
    for i in range(4)]

run = True
while run:
    WINDOW.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            for button in playerChoiceButtons:
                if button.state == "hover":
                    controller.actionNumber(button.action)
                    controller.players[controller.currentPlayer].hand.update()
    
    
    for button in playerChoiceButtons:
        if BUTTON_ACTIONS[button.action] not in controller.players[controller.currentPlayer].hand.getActions():
            button.state = "inactive"
    
    activeButtons = [_ for _ in playerChoiceButtons if _.state != "inactive"]
    #print([BUTTON_ACTIONS[button.action] for button in activeButtons])
    for i,button in enumerate(activeButtons):
        button.updateDraw(WINDOW, (((i+1)/(len(activeButtons)+1))*WIDTH, HEIGHT*0.91), (WIDTH*0.13, HEIGHT*0.06))
        
    drawCard(WINDOW, controller.players[controller.currentPlayer].hand.cards[0], (WIDTH*0.5, HEIGHT*0.5))
        
    pygame.display.update()
    clock.tick(60)