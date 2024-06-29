from settings import *
from player import Player

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('blackjack')
clock = pygame.time.Clock()



run = True
while run:
    WINDOW.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)