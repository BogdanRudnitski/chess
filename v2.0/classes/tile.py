class Tile:
    
    def __init__(self, x, y, color, piece = None):
        
        self.x = x
        self.y =y
        self.pos = (x, y)
        self.color = color
        self.piece = piece
        
    def select(self):
        
        if self.piece:
            if self.is_selected:
                self.is_selected = False
            else:
                self.is_selected = True

    def is_empty(self):
        return self.piece == None
    
    def has_piece(self):
        return not self.is_empty()
    
    def get_piece(self):
        if self.piece:
            return self.piece
        return None
    
    def get_team(self):
        if self.piece:
            return self.piece.get_team()
        return None
        
    def get_image(self):
        if self.piece:
            return self.piece.get_image()
        return None
    
    def get_piece_type(self):
        if self.piece:
            return self.piece.name
        return None