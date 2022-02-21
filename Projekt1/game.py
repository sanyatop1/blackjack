from os import remove
import Player
import colorama
from deck import Deck
import random
from itertools import product
from const import NAMES
import voice11
import time

class Game:
    max_pl_count = 4
    list_points = []

    def __init__(self):
        self.players = []
        self.player = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0
        self.player_pos = None

    def _launching(self):
        voice11.speak(("Привет, введи своё имя"))
        pl_name = input("Привет, введи своё имя: ")
        voice11.speak(("Привет", pl_name, "Теперь ты игрок"))
        colorama.init()
        print(colorama.Fore.RED,pl_name, ':  ТЕПЕРЬ ТЫ ИГРОК')
        print(colorama.Style.RESET_ALL)
        time.sleep(2)
        while True:
          voice11.speak((pl_name,"Введи число ботов"))
          bots_count = int(input("Введи число ботов: "))
          if bots_count <= self.max_pl_count - 1:
              break
        self.all_players_count = bots_count + 1
        time.sleep(1)
        voice11.speak(("Создание ботов"))
        time.sleep(1.5)
        for _ in range(bots_count):
            for self.bot_name in product(random.choices(NAMES)):
                b = Player.Bot(self.bot_name)
            self.players.append(b)
            voice11.speak(("Игрок", self.bot_name, "создан"))
            print("Игрок", self.bot_name[0], "создан")
            time.sleep(1.5)
        self.player = Player.Player(pl_name)
        self.player_pos = random.randint(0, self.all_players_count)
        voice11.speak((pl_name,"Твоя позиция в игре", self.player_pos))
        print(colorama.Fore.RED,"Твоя позиция в игре: ", self.player_pos)
        print(colorama.Style.RESET_ALL)
        time.sleep(1.5)
        self.players.insert(self.player_pos, self.player)
    
    def ask_money(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
            
    def ask_cards(self):
        for player in self.players:
            while player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)
                if isinstance(player, Player.Player):
                    player.print_cards()

    def win_player(self): 
        for _ in self.players:
            win_point = max(self.list_points)
            if win_point > 21:
              self.list_points.remove(win_point)
        for i in self.players:
            if win_point == i.fullpoints:
                voice11.speak(("Победил: ", i.name))
                colorama.init()
                print(colorama.Fore.GREEN,"Победил: ", i.name)
                print(colorama.Style.RESET_ALL)
                
              
    def start_game(self):
        self._launching()
        self.ask_money()
        self.first_descr()
        self.player.print_cards()
        self.ask_cards()
        
        



    

