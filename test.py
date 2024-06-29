from settings import *
from shoe import Shoe
from dealer import Dealer

controller = Dealer(2)

controller.newGame()

for player in controller.players:
    print(player.hand.cards)