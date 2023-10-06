import ogengine.engine as e
import ogengine.eg as og
import ogengine.colors as colors
import pygame

def start():
    e.GameEngine().create_screen(800, 600)
    
def whiles():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        
    # Oyun 
    pygame.display.update()

# Oyun tekrarını 
if __name__ == "__main__":
    start()
    e.GameEngine().run_game_loop(whiles)
