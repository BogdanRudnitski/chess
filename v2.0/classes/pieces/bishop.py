from piece import Piece

class Bishop(Piece):
    
    def __init__(self, team):
        
        super().__init__("bishop", team)
    
    
    def __str__(self):
        
        return super().__str__()
    
    
    def get_moves(self, board, pos):
        
        moves = []
        
        moves.extend(super().check_next_move(board, pos, (1, 1), -1))
        moves.extend(super().check_next_move(board, pos, (1, -1), -1))
        moves.extend(super().check_next_move(board, pos, (-1, -1), -1))
        moves.extend(super().check_next_move(board, pos, (-1, 1), -1))
        
        return moves