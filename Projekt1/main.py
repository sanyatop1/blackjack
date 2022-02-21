from deck import Deck
from game import Game
import Player 

if __name__ == '__main__':
    g = Game()
    g.start_game()
    for pl in g.players:
        if isinstance(pl, Player.Bot):
             pl.print_cards()
        print("Следуйщий игрок:\n")
    g.win_player()
    
    
    
   




