import pygame, keyboard

class Input:
    def __init__(self):
        pass

    def pressed(self, key):
        return keyboard.is_pressed(key)

class GameEngine():
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.background_color = (0,0,0)
        self.using_while = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("OGEngine APP")
    
    def set_background(self, back_color):
        self.background_color = back_color
    
    def use_while(self, path):
        self.while_path = path
        self.using_while = True
    
    def set_screen(self, width, height, caption):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
    
    def clear_screen(self):
        self.screen.fill(self.background_color)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.background_color)
            
            if self.using_while == True:
                self.while_path()
            
            pygame.display.flip()

        pygame.quit()
        keyboard.unhook_all()

class Circle:
    def __init__(self, x, y, radius, color):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, surface):
        self.surface = surface
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
        
class Square:
    def __init__(self, x, y, size_x, size_y, color):
        self.color = color
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def draw(self, surface):
        self.surface = surface
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size_x, self.size_y))
        
class Image:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path
        self.continue_write = None
        self.image = pygame.image.load(self.image_path)
        
        
    def set_scale(self, img_size_x, img_size_y):
        if self.continue_write != False:
            self.img_size_x = img_size_x
            self.img_size_y = img_size_y
            self.image = pygame.transform.scale(self.image, (img_size_x, img_size_y)) 
        
    def draw(self, surface):
        if self.continue_write != False:
            self.surface = surface
            surface.blit(self.image, (self.x, self.y))
        
class Line:
    def __init__(self, start_x, start_y, end_x, end_y, color, thickness=1):
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.thickness = thickness

    def draw(self, surface):
        pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.thickness)
