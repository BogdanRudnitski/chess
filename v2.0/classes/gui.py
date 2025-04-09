import pygame
from gamestate import GameState

class GUI:
    
    def __init__(self, res = (800,800)):
        
        self.game_state = GameState()
        self.screen = pygame.display.set_mode(res)
        pygame.font.init()
        self.check_message = pygame.font.SysFont('Calibri', 100).render('CHECK',False,'blue')
        
        
    def initialize(self):
        
        self.game_state.set_board()
        
        
    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = self.get_mouse()
                self.game_state.click(mouse)
                   
        
    def draw_board(self):
        
        mouse = self.get_mouse()
        tiles = self.game_state.get_tiles()
        
        for tile in tiles:
            color = self.color_selector(tile, mouse)
            pygame.draw.rect(self.screen, color, 
                             [tile.x * 100, tile.y * 100,
                              100, 100])
            if tile.has_piece():
                load_image = pygame.image.load(tile.get_image())
                display = pygame.transform.scale(load_image, (100, 100))
                self.screen.blit(display, (tile.x * 100, tile.y * 100))
        
        if self.game_state.check:
            self.screen.blit(self.check_message, (230,345))
        pygame.display.flip()
        
        pygame.display.update()
        
    
    def color_selector(self, tile, mouse):
        
        selected_tile = self.game_state.selected_tile
        valid_moves = self.game_state.valid_moves
        attack_moves = self.game_state.attack_moves
        
        if tile == selected_tile:
            color = "orange"
        elif tile.pos == mouse:
            color = "yellow"
        elif tile.pos in attack_moves:
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