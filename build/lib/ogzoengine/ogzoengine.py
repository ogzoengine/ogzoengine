import pygame, keyboard
import sys

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
        self.mouse_pressed = False
        self.mouse_click_type = None
        self.set_icon = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("OGEngine APP")
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
    
    def get_mouse_pos(self):
        return pygame.mouse.get_pos()
    
    def get_mouse_info(self):
        return self.mouse_pressed, self.mouse_click_type
    
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
        clock = pygame.time.Clock()
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click_type = event.button
                    self.mouse_pressed = True
                    

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_click_type = None
                    self.mouse_pressed = False

            self.screen.fill(self.background_color)
            
            if self.using_while == True:
                self.while_path()
            
            pygame.display.flip()
            clock.tick(120)

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
        self.doit = None
        self.surface = None

    def draw(self, surface):
        self.surface = surface
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size_x, self.size_y))
        
    def mouse_touch(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if (self.x < self.mouse_x < self.x + self.size_x and
                self.y < self.mouse_y < self.y + self.size_y):
            return True
        
    def mouse_clicked(self, mouse_pressed, mouse_click_type, wan_type):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.wan_type = wan_type
        
            
        if (self.x < mouse_x < self.x + self.size_x and self.y < mouse_y < self.y + self.size_y):
            if mouse_click_type and mouse_click_type == self.wan_type:
                return True
            elif not mouse_click_type and mouse_click_type == self.wan_type:
                return False
        
        
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

class Text:
    def __init__(self, x, y, text, font=None,font_size=20, font_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.text = text

    def draw(self, surface):
        font = pygame.font.Font(self.font, self.font_size)
        text_surface = font.render(self.text, True, self.font_color)
        surface.blit(text_surface, (self.x + 5, self.y + 5))
            