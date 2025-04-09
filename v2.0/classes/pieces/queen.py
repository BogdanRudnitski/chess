from piece import Piece
from pieces.rook import Rook
from pieces.bishop import Bishop

class Queen(Piece):
    
    name = "queen"
    
    def __init__(self, team):
        
        super().__init__(team)
    
    
    def __str__(self):
        
        return super().__str__()
    
    
    def get_moves(self, board, pos):
        
        valid_moves = []
        attack_moves = []
        
            
        valid, attack = Rook.get_moves_static(board, pos, self.team)
        valid_moves.extend(valid)
        attack_moves.extend(attack)
        valid, attack = Bishop.get_moves_static(board, pos, self.team)
        valid_moves.extend(valid)
        attack_moves.extend(attack)
        
        return valid_moves, attack_moves
    
    @staticmethod
    def get_moves_static(board, pos, team):
        
        valid_moves = []
        attack_moves = []
        
            
        valid, attack = Rook.get_moves_static(board, pos, team)
        valid_moves.extend(valid)
        attack_moves.extend(attack)
        valid, attack = Bishop.get_moves_static(board, pos, team)
        valid_moves.extend(valid)
        attack_moves.extend(attack)
        
        return valid_moves, attack_moves
    
    @staticmethod
    def get_attack_moves_static(board, pos, team):
        
        _, attack_moves = Queen.get_moves_static(board, pos, team)
            
        return attack_moves