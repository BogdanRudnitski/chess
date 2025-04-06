from piece import Piece

class Knight(Piece):
    
    def __init__(self, team):
        
        super().__init__("knight", team)
    
    
    def __str__(self):
        
        return super().__str__()
    
    
    
    def get_moves(self, board, pos):
        
        moves = []
        
        moves.extend(super().check_next_move(board, pos, (1, 2), 1))
        moves.extend(super().check_next_move(board, pos, (-1, 2), 1))
        moves.extend(super().check_next_move(board, pos, (-1, -2), 1))
        moves.extend(super().check_next_move(board, pos, (1, -2), 1))
        moves.extend(super().check_next_move(board, pos, (2, 1), 1))
        moves.extend(super().check_next_move(board, pos, (-2, 1), 1))
        moves.extend(super().check_next_move(board, pos, (-2, -1), 1))
        moves.extend(super().check_next_move(board, pos, (2, -1), 1))
        
        return moves