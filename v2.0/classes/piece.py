class Piece:
    
    name = "piece"
    
    def __init__(self, team):
        
        self.team = team
        self.image = f"v2.0/classes/images/{'black' if team == 'B' else 'white'} {self.name}.png"
    
    def __str__(self):
        
        return self.image
    
    
    @staticmethod
    def check_next_move(board, pos, direction, reach, team):
        
        valid_moves = []
        attack_move = ()
        
        if reach != 0:
            
            next_move = (pos[0] + direction[0], pos[1] + direction[1])
            if board.is_valid_tile(next_move):
                next_tile = board.tile_at(next_move)
                if next_tile.is_empty():
                    valid_moves.append(next_move)
                    valid, attack = Piece.check_next_move(board, next_move, direction, reach - 1, team)
                    valid_moves.extend(valid)
                    attack_move = attack
                elif next_tile.get_team() != team:
                    valid_moves.append(next_move)
                    attack_move = next_move
            
        return valid_moves, attack_move
    
    
    @staticmethod
    def get_attack_move(board, pos, direction, reach, team):
        
        _, attack_move = Piece.check_next_move(board, pos, direction, reach, team)
        return attack_move
    
    
    def get_team(self):
        return self.team
    
    def get_type(self):
        return self.name
    
    def get_image(self):
        return self.image