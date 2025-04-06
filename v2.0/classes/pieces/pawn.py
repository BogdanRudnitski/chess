from piece import Piece

class Pawn(Piece):
    
    def __init__(self, team):
        
        super().__init__("pawn", team)
        self.moves = []
    
    
    def __str__(self):
        
        return super().__str__()
    
    
    def get_moves(self, board, pos):
        
        moves = []
        
        start = 1 if self.team == "B" else 6
        reach = 2 if pos[1] == start else 1
        direction = (0, 1) if self.team == "B" else (0, -1)
        
        moves.extend(super().check_next_move(board, pos, direction, reach))
        
        for x in [-1, 1]:
            next_move = (pos[0] + x, pos[1] + direction[1])
            if board.tile_at(next_move):
                if board.team_at(next_move):
                    moves.append(next_move)
                    board.in_danger.append(next_move)
        
        return moves
        