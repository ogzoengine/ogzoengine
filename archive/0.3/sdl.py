import sdl2
import sdl2.ext

class GameEngine():
    def __init__(self):
        sdl2.ext.init()
        self.width = 800
        self.height = 600
        self.background_color = sdl2.ext.Color(0, 0, 0)
        self.using_while = False
        self.window = sdl2.ext.Window("OGEngine APP", size=(self.width, self.height))
        self.window.show()
    
    def use_while(self, path):
        self.while_path = path
        self.using_while = True
    
    def set_screen(self, width, height, caption):
        self.width = width
        self.height = height
        self.window.size = (self.width, self.height)
        self.window.title = caption
    
    def run(self):
        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False

            sdl2.SDL_SetRenderDrawColor(self.window.get_surface(), *self.background_color)
                        
            if self.using_while == True:
                self.while_path()
            
            self.window.refresh()

        sdl2.ext.quit()

class Circle:
    def __init__(self, x, y, radius, color):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, surface):
        surface.fill(self.color, (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))
        
class Square:
    def __init__(self, x, y, size_x, size_y, color):
        self.color = color
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def draw(self, surface):
        rect = sdl2.SDL_Rect(self.x, self.y, self.size_x, self.size_y)
        sdl2.SDL_FillRect(surface, rect, self.color)
        
class Image:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path
        self.image_surface = self.load_image(self.image_path)
        
    def load_image(self, image_path):
        return sdl2.ext.load_image(image_path)
        
    def set_scale(self, img_size_x, img_size_y):
        new_surface = sdl2.SDL_CreateRGBSurface(0, img_size_x, img_size_y, 32, 0, 0, 0, 0)
        sdl2.SDL_BlitScaled(self.image_surface, None, new_surface, None)
        self.image_surface = new_surface
        
    def draw(self, surface):
        sdl2.SDL_BlitSurface(self.image_surface, None, surface, sdl2.SDL_Rect(self.x, self.y, 0, 0))


        
class Line:
    def __init__(self, start_x, start_y, end_x, end_y, color, thickness=1):
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.thickness = thickness

    def draw(self, surface):
        # Draw a line using SDL2
        sdl2.SDL_SetRenderDrawColor(surface, *self.color)
        sdl2.SDL_RenderDrawLine(surface, self.start_x, self.start_y, self.end_x, self.end_y)
