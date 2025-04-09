from piece import Piece

class Pawn(Piece):
    
    name = "pawn"
    
    def __init__(self, team):
        
        super().__init__(team)
        self.moves = []
    
    
    def __str__(self):
        
        return super().__str__()
    
    
    def get_moves(self, board, pos):
        
        valid_moves = []
        attack_moves = []
        
        start = 1 if self.team == "B" else 6
        reach = 2 if pos[1] == start else 1
        direction = (0, 1) if self.team == "B" else (0, -1)
        

        def pawn_check_move(board, pos, direction, reach):
            moves =[]
            if reach != 0:
                next_move = (pos[0] + direction[0], pos[1] + direction[1])
                if board.is_valid_tile(next_move):
                    if board.tile_at(next_move).is_empty():
                        moves.append(next_move)
                        moves.extend(pawn_check_move(board, next_move, direction, reach - 1))
            return moves
    
        valid_moves = pawn_check_move(board, pos, direction, reach)
        
        for x in [-1, 1]:
            next_move = (pos[0] + x, pos[1] + direction[1])
            if board.is_valid_tile(next_move):
                if board.tile_at(next_move).has_piece() and board.team_at(next_move) != self.team:
                    attack_moves.append(next_move)
                    valid_moves.append(next_move)
        
        return valid_moves, attack_moves
    
    
    @staticmethod
    def get_moves_static(board, pos, team):
        
        valid_moves = []
        attack_moves = []
        
        start = 1 if team == "B" else 6
        reach = 2 if pos[1] == start else 1
        direction = (0, 1) if team == "B" else (0, -1)
        

        def pawn_check_move(board, pos, direction, reach):
            moves =[]
            if reach != 0:
                next_move = (pos[0] + direction[0], pos[1] + direction[1])
                if board.is_valid_tile(next_move):
                    if board.tile_at(next_move).is_empty():
                        moves.append(next_move)
                        moves.extend(pawn_check_move(board, next_move, direction, reach - 1))
            return moves
    
        valid_moves = pawn_check_move(board, pos, direction, reach)
        
        for x in [-1, 1]:
            next_move = (pos[0] + x, pos[1] + direction[1])
            if board.is_valid_tile(next_move):
                if board.tile_at(next_move).has_piece() and board.team_at(next_move) != team:
                    attack_moves.append(next_move)
                    valid_moves.append(next_move)
        
        return valid_moves, attack_moves
    
    @staticmethod
    def get_attack_moves_static(board, pos, team):
        
        _, attack_moves = Pawn.get_moves_static(board, pos, team)
        
        return attack_moves