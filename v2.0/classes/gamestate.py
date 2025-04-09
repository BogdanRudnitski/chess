from board import Board
from pieces import *

class GameState():
    
    def __init__(self):
        
        self.board = Board()
        
        self.selected_tile = None
        self.valid_moves = []
        self.attack_moves = []
        
        self.turn = ""
        self.king_positions = {}
        
        self.check = False
    
    
    def click(self, mouse):
        
        tile = self.board.tile_at(mouse)
        
        if self.selected_tile:
            if mouse in self.valid_moves:
                self.king_positions[self.turn] = self.board.move(self.selected_tile, tile) or self.king_positions[self.turn]
                self.change_turn()
                self.verify_check()
            self.clear_selection()
        elif tile.has_piece():
            if tile.piece.team == self.turn:
                self.selected_tile = self.board.tile_at(mouse)
                self.valid_moves, self.attack_moves = tile.piece.get_moves(self.board, tile.pos)
                self.verify_moves()
            
    def verify_check(self):
        
        king_pos = self.king_positions.get(self.turn)
        
        for simulation_piece in [Rook, Bishop, Knight, Pawn, King]:
            attack_moves = simulation_piece.get_attack_moves_static(self.board, king_pos, self.turn)
            for move in attack_moves:
                if move:
                    piece = self.board.piece_at(move).name
                    if piece == simulation_piece.name :
                        self.check = True
                        return True
                    elif piece == "queen" and (simulation_piece.name == "rook" or simulation_piece.name == "bishop"):
                        self.check = True
                        return True
        self.check = False
        return False
    
    
    def verify_moves(self):
        
        filtered_valid_moves = []
        filtered_attack_moves = []
        
        for move in self.valid_moves:
            if self.is_valid_move(move):
                filtered_valid_moves.append(move)
                if move in self.attack_moves:
                    filtered_attack_moves.append(move)

        self.valid_moves = filtered_valid_moves
        self.attack_moves = filtered_attack_moves
                
    def is_valid_move(self, move):
        
        checked_status = self.check == True
        stored_piece = self.board.piece_at(move)
        self.board.move(self.selected_tile, self.board.tile_at(move))
        
        original_king_pos = self.king_positions[self.turn]
        if self.board.tile_at(move).get_piece_type() == "king":
            self.king_positions[self.turn] = move

        
        creates_check = self.verify_check()
        self.board.move(self.board.tile_at(move), self.selected_tile)
        self.board.tile_at(move).piece = stored_piece
        
        if self.board.tile_at(move).get_piece_type() == "king":
            self.king_positions[self.turn] = original_king_pos

        
        
        self.set_check(checked_status)
        
        if creates_check:
            return False
        return True
        
        
    def change_turn(self):
        if self.turn == "W":
            self.turn = "B"
        else:
            self.turn = "W"
    
    def clear_selection(self):
        self.selected_tile = None
        self.valid_moves.clear()
        self.attack_moves.clear()
        
    def set_check(self, boolean):
        self.check = boolean
        
    def set_board(self):
        
        self.board.set_board()
        self.turn = "W"
        self.king_positions = {"B" : (4, 0), "W" : (4, 7)}
        
    
    def get_tiles(self):
        
        return self.board.get_tiles()