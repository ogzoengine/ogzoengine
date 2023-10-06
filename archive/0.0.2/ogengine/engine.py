import pygame, re, math

class Colors:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    gray = (128, 128, 128)
    brown = (128, 0, 0)
    olive = (128, 128, 0)
    orange = (255, 165, 0)
    pink = (255, 192, 203)
    purple = (128, 0, 128)
    turquoise = (64, 224, 208)
    gold = (255, 215, 0)
    silver = (192, 192, 192)
    black = (0, 0, 0)
    white = (255, 255, 255)
    maroon = (128, 0, 0)
    lime = (0, 128, 0)
    navy = (0, 0, 128)
    teal = (0, 128, 128)
    aqua = (0, 255, 255)
    fuchsia = (255, 0, 255)
    dark_gray = (64, 64, 64)
    light_gray = (192, 192, 192)
    dark_red = (139, 0, 0)
    dark_green = (0, 100, 0)
    dark_blue = (0, 0, 139)
    dark_yellow = (204, 204, 0)
    dark_cyan = (0, 139, 139)
    dark_magenta = (139, 0, 139)
    indigo = (75, 0, 130)
    hot_pink = (255, 105, 180)
    lime_green = (50, 205, 50)
    sky_blue = (135, 206, 235)
    violet = (238, 130, 238)
    coral = (255, 127, 80)

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = None

    def start(self):
        pass

    def create_screen(self, screen_x, screen_y):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_x, screen_y))
        return self.screen

    def run_game_loop(self, whiles_function):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            whiles_function()
            pygame.display.update()

if __name__ == "__main__":
    engine = GameEngine()
    engine.start()
    engine.run_game_loop(engine.whiles)