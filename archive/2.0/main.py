import pygame, sys, os


  
class BS_Error(Exception):
    def __init__(self, error, info):
        self.error = error
        self.info = info
        super().__init__(f"{self.error} | {self.info}")

class inputs:
    def __init__(self, keys, key):
        self.key = key
        self.keys = keys
    
    def return_key(self):
        return self.keys[ord(self.key)]

class Screen:
    def __init__(self):
        self.mouse_pressed = False
        self.running = True
        self.NameError_x11 = True
        
        self.keypress = None
        
        self.using_while = False
        self.using_listener = False
        self.using_draw = False
        self.unicode = False
        dev_on = False
        
        self.runned = True
        self.key_on = False
        
        self.mouse_click_type = None
        self.event_key_num = None
        self.event_key = None
        
        self.inputsd = 0.1
        self.listener = 0
        self.mouse_x, self.mouse_y = 0,0
        self.width = 1280
        self.height = 720
        self.background_color = (0,0,0)
    
    
    def set_screen(self,width,height,caption):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
    
    def use_drawing(self,path):
        self.draw_path = path
        self.using_draw = True
    
    def use_while(self, path):
        self.while_path = path
        self.using_while = True
        
    def use_listener(self, path):
        try:
            self.listener_path = path
            self.using_listener = True
        except NameError:
            self.using_listener = False
            raise BS_Error("NameError", "Change listener name")
    
    def input(self,key):
        self.key = key
        if self.key == self.keys[pygame.key.key_code(self.key)]:
            return True
    
    def return_key(self):
        self.keywant = 0
        if self.keywant == 0:
            return self.event_key_num, self.keypress
        
    def return_keys(self):
        return self.keys
    
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("OGEngine APP")
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.clock = pygame.time.Clock()
        self.keypress = False
        
        
        while self.runned:
            self.clock.tick(80)
            for event in pygame.event.get():
                # Key inputs
                self.keys = pygame.key.get_pressed()
                self.key_on = True
                
                
                if self.using_listener:
                    try:
                        self.listener_path()
                    except TypeError:
                        self.using_listener = False
                        raise BS_Error("TypeError", "Listener can't running!!")
                
                try:
                    self.screen.fill(self.background_color)
                except SyntaxError:
                    self.screen.fill(0,0,0)
                    raise BS_Error("SyntaxERROR", "Background Color Error")
            
                if self.using_draw:
                    try:
                        self.draw_path()
                    except TypeError:
                        self.using_draw = False
                        raise BS_Error("TypeError", "Draw path error")
                
                if event.type == pygame.QUIT:
                    self.running = False
                    if dev_on == False:
                        self.runned = False
                if event.type == pygame.KEYDOWN:
                    self.event_key = event.key
                    self.event_key_num = pygame.key.name(self.event_key)
            
            
            if self.running:
                if self.listener < 0:
                    self.keypress = True
                    self.listener = 1
            
                for key in self.keys:
                    if key:
                        self.listener += 1
                    
                try:
                    if self.using_while == True:
                        self.while_path()
                except TypeError:
                    self.using_while = False
                    raise BS_Error("TypeError", "While path error")
                            
                pygame.display.update()
                pygame.display.flip()
        pygame.quit()

class Circle:
    def __init__(self, x, y, radius, color):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, surface):
        self.surface = surface.screen
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
        self.surface = surface.screen
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.size_x, self.size_y))
        
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
            self.surface = surface.screen
            self.surface.blit(self.image, (self.x, self.y))
        
class Line:
    def __init__(self, start_x, start_y, end_x, end_y, color, thickness=1):
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.thickness = thickness

    def draw(self, surface):
        self.surface = surface.screen
        pygame.draw.line(self.surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.thickness)

class Text:
    def __init__(self, x, y, text, font=None,font_size=20, font_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.text = text

    def draw(self, surface):
        self.surface = surface.screen
        font = pygame.font.Font(self.font, self.font_size)
        text_surface = font.render(self.text, True, self.font_color)
        self.surface.blit(text_surface, (self.x + 5, self.y + 5))