import pygame as p
import sys, os , re, math


p.init()

# Colors

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

# Automatic Variables
caption = 'ogzengine'
screen_size = (500, 500)
font_32 = p.font.Font(None, 32)
font_36 = p.font.Font(None, 36)
font_64 = p.font.Font(None, 64)

# Errors
font_error = False

# Variables
whiles_ = False
running = True
fps = 60
clock = p.time.Clock()

# defs
def set_screen(caption_text, screen_size):
    global screen, caption
    caption = caption_text
    screen = p.display.set_mode(screen_size)
    p.display.set_caption(caption)

def set_font(req_font):
    global font_32, font_36, font_64, font_error
    try:
        font_32 = p.font.Font(req_font, 32)
        font_36 = p.font.Font(req_font, 36)
        font_64 = p.font.Font(req_font, 64)
    except FileExistsError:
        font_32 = p.font.Font(None, 32)
        font_36 = p.font.Font(None, 36)
        font_64 = p.font.Font(None, 64)
        font_error = True
        
def whiles_sys(req_w):
    global whiles
    whiles = req_w

def developer_texts():
    pass

def set_background_color(color):
    global background_color
    background_color = color

def run_game(dev_mod):
    global running
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            running = False
            
    if dev_mod == True: developer_texts()
            
    clock.tick(fps)
    screen.fill(background_color)
        
    # Draww
        
    p.display.flip()
    clock.tick(60)

def close():
    global running
    running = False
    p.quit()
    sys.exit()
