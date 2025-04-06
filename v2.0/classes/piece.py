class Piece:
    
    def __init__(self, name, team):
        
        self.name = name
        self.team = team
        self.image = f"v2.0/classes/images/{'black' if team == 'B' else 'white'} {name}.png"
    
    def __str__(self):
        
        return self.image
    
    
    
    def check_next_move(self, board, pos, direction, reach):
        
        moves = []
        
        next_move = (pos[0] + direction[0], pos[1] + direction[1])
        if board.tile_does_not_exist(next_move):
            return moves
        next_tile = board.tile_at(next_move)
        
        if reach != 0:
            
            if next_tile.is_empty():
                moves.append(next_move)
                moves.extend(self.check_next_move(board, next_move, direction, reach - 1))
            elif board.team_at(next_move) != self.team:
                moves.append(next_move)
                board.in_danger.append(next_move)
            
        return moves