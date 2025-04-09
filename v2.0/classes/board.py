from pieces import *

from tile import Tile

class Board:
    
    def __init__(self):
        
        self.tiles = { (x,y) : Tile(x, y, 'white' if (x + y) % 2 == 0 else 'grey') 
                      for y in range(8) for x in range(8) }
        
        self.turn = ""
        self.king_positions = {}
        self.selected_tile = None
        self.possible_moves = []
        self.in_danger = []
        
        
    def initialize(self):
        
        self.set_board()
        
    
    
    
    
    def move(self, origin, destination):
        destination.piece = origin.piece
        origin.piece = None
        piece = destination.piece
        if piece.get_type() == "king":
            return destination.pos

    
    
    def get_tiles(self):
        
        return self.tiles.values()
        
    def tile_at(self, pos):
        
        return self.tiles.get((pos[0], pos[1]))
    
    def is_valid_tile(self, pos):
        
        return not self.invalid_tile(pos)
    
    def invalid_tile(self, pos):
        
        return self.tile_at(pos) == None
    
    def piece_at(self, pos):
        
        tile = self.tile_at(pos)
        
        if tile.is_empty():
            return
        return tile.piece
        
        
    def team_at(self, pos):
        
        piece = self.piece_at(pos)
        
        if piece:
            return piece.team
        return 
        
        
    
    def set_board(self):
        
        # Set pawns
        for x in range(8):
            self.tiles[(x, 1)].piece = Pawn("B")
            self.tiles[(x, 6)].piece = Pawn("W")

        # Set rooks
        for x in [0, 7]:
            self.tiles[(x, 0)].piece = Rook("B")
            self.tiles[(x, 7)].piece = Rook("W")

        # Set knights
        for x in [1, 6]:
            self.tiles[(x, 0)].piece = Knight("B")
            self.tiles[(x, 7)].piece = Knight("W")

        # Set bishops
        for x in [2, 5]:
            self.tiles[(x, 0)].piece = Bishop("B")
            self.tiles[(x, 7)].piece = Bishop("W")

        # Set queens
        self.tiles[(3, 0)].piece = Queen("B")
        self.tiles[(3, 7)].piece = Queen("W")

        # Set kings
        self.tiles[(4, 0)].piece = King("B")
        self.tiles[(4, 7)].piece = King("W")
    
    
    def __repr__(self):
        
        printed_board = ""
        
        for tile in self.tiles.values():
                
            if tile.piece == None:
                printed_board += " .. "
            else:
                printed_board += " " + str(tile.piece.team) + str(tile.piece.name[0]) + " "
                
            if tile.x == 7:
                printed_board += "\n\n"
                
        return printed_board