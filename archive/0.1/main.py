import pygame, sys, os, re


# Fonksiyonlar

clock = pygame.time.Clock()

class Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    



class GameEngine():
    def __init__(self):
        self.caption = "Ogengine app"
        self.size = (800, 600)
        self.screen = None
        self.running = True
        self.developer_mode = False
        self.objects = []
        self.create_screen()
        
    class Circle:
        def __init__(self, screen, x, y, radius):
            self.screen = screen
            self.x = x
            self.y = y
            self.radius = radius

        def draw(self):
            print("running")
            pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.radius)


        
    def create_screen(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

    def set_screen(self, caption_input, size_input):
        self.caption = caption_input
        self.size = size_input
        self.create_screen()
        pygame.display.set_caption(self.caption)
        
    def run_game(self):
        clock = pygame.time.Clock()
        pygame.init()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

            keys = pygame.key.get_pressed()

            if self.developer_mode:
                pass
            
            self.screen.fill((0, 0, 0))  # Fill screen with black
            pygame.display.flip()
            clock.tick(60)