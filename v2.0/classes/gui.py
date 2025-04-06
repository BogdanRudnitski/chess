import pygame

class GUI:
    
    def __init__(self, board, res = (800,800)):
        
        self.board = board
        self.screen = pygame.display.set_mode(res)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = self.get_mouse()
                self.board.click(mouse)
                   
        
    def draw_board(self):
        
        mouse = self.get_mouse()
        
        for tile in self.board.get_tiles():
            color = self.color_selector(tile, mouse)
            pygame.draw.rect(self.screen, color, 
                             [tile.x * 100, tile.y * 100,
                              100, 100])
            if tile.piece:
                load_image = pygame.image.load(tile.piece.image)
                display = pygame.transform.scale(load_image, (100, 100))
                self.screen.blit(display, (tile.x * 100, tile.y * 100))
        
        pygame.display.update()
        
    
    def color_selector(self, tile, mouse):
        
        selected_tile = self.board.selected_tile
        valid_moves = self.board.possible_moves
        in_danger = self.board.in_danger
        
        if tile == selected_tile:
            color = "orange"
        elif tile.pos == mouse:
            color = "yellow"
        elif tile.pos in in_danger:
            color = "red"
        elif tile.pos in valid_moves:
            color = "green"
        else:
            color = tile.color
        
        return color
    
    def get_mouse(self):
        
        mouse = pygame.mouse.get_pos()
        position = (mouse[0] // 100, mouse[1] // 100)
        return position