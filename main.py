from settings import *
from player import Player
from button import Button

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('blackjack')
clock = pygame.time.Clock()

userChoiceButtons = [
    Button(
        ((i+1)/7*WIDTH, HEIGHT*0.91), 
        (WIDTH*0.13, HEIGHT*0.06), 
        None)
    for i in range(3)]

run = True
while run:
    WINDOW.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for button in userChoiceButtons:
        button.update(WINDOW)
            
    pygame.display.flip()
    clock.tick(60)