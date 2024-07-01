from settings import *

'''
#BROKEN FUNCTION AS OF 2021-09-29
#console can not encode
#UnicodeEncodeError: 'charmap' codec can't encode character '\u2660' in position 1: character maps to <undefined>

def convertCardToSymbol(card:list) -> str:
    suits = ['♠', '♣', '♥', '♦']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return f"{numbers[card[0] - 1]}{suits[card[1]]}"
'''

def convertCardToSymbol(card:list) -> str:
    suits = ["S", "C", "H", "D"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return f"{numbers[card[0] - 1]} {suits[card[1]]}"

def convertCardToName(card:list) -> str:
    return f"{NAMES[card[0]]} of {SUITS[card[1]]}"

#print(convertCardToName([1, 0])) # Ace of Spades
#print(convertCardToSymbol([1, 0])) # A S

def drawCard():
    raise NotImplementedError