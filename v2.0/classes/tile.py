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