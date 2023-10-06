import sdl2
import sdl2.ext

class GameEngine:
    def __init__(self, width, height):
        sdl2.ext.init()
        self.width = width
        self.height = height
        self.background_color = sdl2.ext.Color(0, 0, 0)
        self.window = sdl2.ext.Window("Simple Game", size=(self.width, self.height))
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
            self.window.clear()

            if self.using_while:
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
        renderer = surface.get_renderer()
        sdl2.ext.fill_circle(renderer, int(self.x), int(self.y), self.radius, self.color)


class Square:
    def __init__(self, x, y, size, color):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self, surface):
        renderer = surface.get_renderer()
        sdl2.ext.fill_rect(renderer, sdl2.SDL_Rect(self.x, self.y, self.size, self.size), self.color)


def main():
    engine = GameEngine(800, 600)

    # Initialize a circle and a square
    circle = Circle(400, 300, 20, sdl2.ext.Color(255, 0, 0))
    square = Square(400, 300, 40, sdl2.ext.Color(0, 0, 255))

    engine.use_while(None)

    engine.run()


if __name__ == "__main__":
    main()
