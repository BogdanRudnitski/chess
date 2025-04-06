from gui import GUI
from board import Board

class Game:

    def __init__(self):
        
        self.board = Board()
        self.gui = GUI(self.board)
    
    def run(self):
        
        self.board.initialize()
        
        while True:

            self.gui.handle_events()
            #self.board.update_game()
            self.gui.draw_board()
    

if __name__ == "__main__":
    game = Game()
    game.run()