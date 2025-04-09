from gui import GUI

class Game:

    def __init__(self):
        
        self.gui = GUI()
    
    def run(self):
        
        self.gui.initialize()
        
        while True:

            self.gui.handle_events()
            self.gui.draw_board()
    

if __name__ == "__main__":
    game = Game()
    game.run()