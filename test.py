from settings import *
from shoe import Shoe
from controller import Controller
from card import *
import sys

controller = Controller(2)

controller.newGame()

for player in controller.players:
    print(player.hands[0].cards)
    for card in player.hands[0].cards:
        print(convertCardToName(card))
    print(player.hands[0].calcValue())
    print(player.hands[0].getActions())
    print()