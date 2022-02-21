
from const import SUITS, RANKS, PRINTED
from itertools import product
from random import shuffle

class Card:
    def __init__(self,suit,rank,picture,points):
      self.suit = suit
      self.rank= rank
      self.picture = picture
      self.points = points


    def __str__(self) :
        message = self.picture + 'Points: ' + str(self.points)
        return message
    


class Deck:
    
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)


    def _generate_deck(self):
        cards =[]
        for suit, rank in product(SUITS, RANKS):
            if rank == "ТУЗ":
                points = 11
            else:
              try:
                points = int(rank) 
              except Exception as e:
                points = 10
            
            picture = PRINTED.get(rank)
            c = Card(suit=suit, rank= rank, points= points, picture= picture)
            cards.append(c)
        return cards
        

    def get_card(self):
        return self.cards.pop()


    def __len__(self):
        return len(self.cards)    

