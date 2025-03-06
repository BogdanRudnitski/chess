from tile import Tile
from piece import Piece

class Board:
    
    def __init__(self):
        
        self.board = { (x,y) : Tile(x,y) for y in range(8) for x in range(8) }
        
    def __repr__(self):
        
        for tile in self.board:
            print(tile)
    
    
    def reset_board(self):
        
        board = self.board
        
        board[()]