import pygame
pygame.init()

from card_images import *

#custom shoe to use for testing spliting hands
#CUSTOM_SHOE = [[2, 0] for i in range(104)]
CUSTOM_SHOE = [[1, 0], [2, 0], [3,0], [4, 0], [10, 0], [11, 0], [12, 0], [13, 0]]

PLAYERS = 3

WIDTH, HEIGHT = 1366, 768

GREEN = "#339933"
WHITE = "#F6F0F0"
RED = "#f01e28"
BLACK = "#100010"
YELLOW = "#ffbb00"
GREY = "#1B2631"

BUTTON_ACTIVE_COL = WHITE
BUTTON_HOVER_COL = "#c0a5d0"

CARDS_PER_COLUMN = 4

DECKS = 2

STARTING_MONEY = 1000

BUTTON_ACTIONS = {
    1:"hit",
    2:"stand",
    3:"double",
    4:"split",
    5:"insure",
    6:"next"
}

SUITS = {
    0:"Clubs",
    1:"Diamonds",
    2:"Hearts",
    3:"Spades"
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
    1:1,
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