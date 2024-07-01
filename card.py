from settings import *

'''
#BROKEN FUNCTION AS OF 2021-09-29
#console can not encode
#UnicodeEncodeError: 'charmap' codec can't encode character '\u2660' in position 1: character maps to <undefined>

def convertCardToSymbol(card:list) -> str:
    suits = ['♣', '♦', '♥', '♠']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return f"{numbers[card[0] - 1]}{suits[card[1]]}"
'''

def convertCardToSymbol(card:list) -> str:
    suits = ["C", "D", "H", "S"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return f"{numbers[card[0] - 1]} {suits[card[1]]}"

def convertCardToName(card:list) -> str:
    return f"{NAMES[card[0]]} of {SUITS[card[1]]}"

#print(convertCardToName([1, 0])) # Ace of Clubs
#print(convertCardToSymbol([1, 0])) # A S

def drawCard(WINDOW, card:list, pos:list, faceDown:bool=False):
    imgSurf = pygame.image.load(CARD_IMAGES[card[0]][card[1]])
    imgSurf = pygame.transform.scale(imgSurf, (int(imgSurf.get_width()*CARD_SIZE_MULTIPLIER), int(imgSurf.get_height()*CARD_SIZE_MULTIPLIER)))
    size = imgSurf.get_size()
    WINDOW.blit(imgSurf, (pos[0]-size[0]/2, pos[1]-size[1]/2))