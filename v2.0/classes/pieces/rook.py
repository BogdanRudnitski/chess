from piece import Piece

class Rook(Piece):
    
    name = "rook"
    
    def __init__(self, team):
        
        super().__init__(team)
    
    
    def __str__(self):
        
        return super().__str__()
    
    
    def get_moves(self, board, pos):
        
        valid_moves = []
        attack_moves = []
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            
            valid, attack = Piece.check_next_move(board, pos, direction, -1, self.team)
            valid_moves.extend(valid)
            attack_moves.append(attack)
        
        return valid_moves, attack_moves
    
    @staticmethod
    def get_moves_static(board, pos, team):
        
        valid_moves = []
        attack_moves = []
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            
            valid, attack = Piece.check_next_move(board, pos, direction, -1, team)
            valid_moves.extend(valid)
            attack_moves.append(attack)
        
        return valid_moves, attack_moves
    
    @staticmethod
    def get_attack_moves_static(board, pos, team):
        
        _, attack_moves = Rook.get_moves_static(board, pos, team)
        
        return attack_moves