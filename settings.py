import pygame
pygame.init()

WIDTH, HEIGHT = 1366, 768

GREEN = "#10a023"
WHITE = "#f0cef0"
RED = "#f01e28"
BLACK = "#100010"

BUTTON_ACTIVE_COL = WHITE
BUTTON_HOVER_COL = "#c0a5d0"
BUTTON_INACTIVE_COL = "#90729d"

CARDS_PER_ROW = 4

DECKS = 2

STARTING_MONEY = 1000

SUITS = {
    0:"Spades",
    1:"Clubs",
    2:"Hearts",
    3:"Diamonds"
}

COUNT_VALUES = {
    1:-1,
    2:1,
    3:1,
    4:1,
    5:1,
    6:1,
    7:0,
    8:0,
    9:0,
    10:-1,
    11:-1,
    12:-1,
    13:-1
}

NAMES = {
    1:"Ace",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
    10:"Ten",
    11:"Jack",
    12:"Queen",
    13:"King"
}

CARD_VALUES = {
    1:11,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    11:10,
    12:10,
    13:10
}