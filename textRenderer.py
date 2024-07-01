from settings import *

def renderText(window, center, text, fontSize, colour = BLACK, font="Hack-Regular.ttf"):
    textFont = pygame.font.Font(font, fontSize)
    
    text = textFont.render(text, True, colour)
    textRect = text.get_rect()
    textRect.center = center
    window.blit(text, textRect)