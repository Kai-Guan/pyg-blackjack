from settings import *
from shoe import Shoe
from dealer import Dealer
from card import *
import sys

controller = Dealer(2)

controller.newGame()

for player in controller.players:
    print(player.hand.cards)
    for card in player.hand.cards:
        print(convertCardToName(card))