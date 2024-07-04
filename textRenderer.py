from settings import *

def renderText(window, pos, text, fontSize, colour = BLACK, font="Hack-Regular.ttf", centered = True):
    textFont = pygame.font.Font(font, fontSize)
    
    text = textFont.render(text, True, colour)
    textRect = text.get_rect()
    if centered:
        textRect.center = pos
    else:
        textRect.topleft = pos
    window.blit(text, textRect)