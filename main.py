from settings import *
from button import Button
from controller import Controller
from card import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE, pygame.SCALED)
pygame.display.set_caption('blackjack')
clock = pygame.time.Clock()

controller = Controller(PLAYERS)

controller.newGame()

playerChoiceButtons = [
    Button(i+1)
    for i in range(6)
    ]

run = True
while run:
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
    WINDOW.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            for button in playerChoiceButtons:
                if button.state == "hover":
                    controller.actionNumber(button.action)
   

    #print(controller.players[controller.currentPlayerNo].hands[controller.currentHandNo].getActions())
    
    for button in playerChoiceButtons:
        print(controller.dealer.cards[1][0])
        if controller.currentPlayerNo in [-1, -2]:
            button.state = "inactive"
        elif controller.currentHandNo == 0 and CARD_VALUES[controller.dealer.cards[1][0]] in [1, 10] and len(controller.players[controller.currentPlayerNo].hands[0].cards) == 2 and controller.players[controller.currentPlayerNo].hands[0].isSplitHand == False and button.action == 5:
            button.state = "active"
        elif BUTTON_ACTIONS[button.action] not in controller.players[controller.currentPlayerNo].hands[controller.currentHandNo].getActions():
            button.state = "inactive"
        else:
            button.state = "active"

    activeButtons = [_ for _ in playerChoiceButtons if _.state != "inactive"]
    #print([BUTTON_ACTIONS[button.action] for button in activeButtons])
    for i,button in enumerate(activeButtons):
        button.updateDraw(WINDOW, (((i+1)/(len(activeButtons)+1))*WIDTH, HEIGHT*0.91), (WIDTH*0.13, HEIGHT*0.06))

    #drawCard(WINDOW, controller.players[controller.currentPlayerNo].hand.cards[0], (WIDTH*0.5, HEIGHT*0.5))
    #print(convertCardToName(controller.players[controller.currentPlayerNo].hand.cards[0]))
    controller.update(WINDOW)

    pygame.display.flip()
    clock.tick(60)