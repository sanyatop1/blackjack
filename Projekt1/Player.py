import abc
from deck import Deck
import random
import game
import voice11
import time


class AbstractPlayer(abc.ABC):
    
    def __init__(self) :
        
        self.cards = []
        self.bet = 0
        self.fullpoints = 0
        self.name = None
         
    def change_points(self):
        self.fullpoints =sum([card.points for card in self.cards])

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()
 
    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

    def print_cards(self):
        print(self.name)
        for card in self.cards:
            print(card)
        print("Все очки: ", self.fullpoints)
        game.Game.list_points.append(self.fullpoints)
     

class Player(AbstractPlayer):
    def __init__(self,pl_name):
        super().__init__()
        self.name = pl_name

    def change_bet(self, max_bet, min_bet):
        while True:
          voice11.speak(("Сделай свою ставку, игрок"))
          value = int(input('Сделай свою ставку: '))
          time.sleep(1.5)
          if value < max_bet and value > min_bet:
            self.bet = value
            break
          print("Твоя ставка: ", self.bet)
    
    def __str__(self) :  
        message =str(self.name )
        return "%s" % (message)

    
    def ask_card(self):
        voice11.speak(("Берёшь ещё карту?"))
        choise = input("Берёшь ещё карту?(y/n): ")
        time.sleep(1.5)
        if choise == "y" and self.fullpoints < 21:
            return True
        else:
            print("Раздача карт закончена!")
            return False


class Bot(AbstractPlayer):

    def __init__(self, bot_name):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = bot_name

    def __str__(self) :  
        message = str(self.name)
        return "%s" % message

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        print(self.name, 'поставил', self.bet, 'денег')

    def ask_card(self):
        if self.fullpoints < self.max_points:
            return True
        else:
            return False

    
       
    
