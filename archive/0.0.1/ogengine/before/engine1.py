import pygame as p
import sys, os , re, math

p.init()


# Otomatik
player_pos_x = 0
player_pos_y = 0
player_size_x = 50
player_size_y = 50
player_color = (255, 0, 0)
developer_mode = True

font = p.font.Font(None, 36)

img_path = "player.png"
player_create = False  # Değişiklik burada
fly = False  # Değişiklik burada

# Variables
screen_size = (800, 600)
background_color = (0, 0, 0)

fps = 60

clock = p.time.Clock()

# Errors
font_error = False


caption = ""
screen = None

def set_screen(caption_text, size):
    global screen, caption
    caption = caption_text
    screen = p.display.set_mode(size)
    p.display.set_caption(caption)

def set_background_color(color):
    global background_color
    background_color = color

def create_character(fly_state, color, size_x, size_y):
    global player_create, fly, player_color, player_size_x, player_size_y
    player_create = True
    fly = fly_state
    player_color = color
    player_size_x = size_x
    player_size_y = size_y

def create_object():
    pass

def set_font(set_font):
    global font
    font = set_font
    

def set_developermode(developer_mode_input):
    global developer_mode
    developer_mode = developer_mode_input

def draw_player():
    global player_pos_x, player_pos_y, player_size_x, player_size_y, player_color
    
    if player_create:  # Değişiklik burada
        p.draw.rect(screen, player_color, (player_pos_x, player_pos_y, player_size_x, player_size_y))
        
def run_game(developer_mode):
    global player_pos_x, player_pos_y, player_create, fly
    
    running = True

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                running = False

        mouse_x, mouse_y = p.mouse.get_pos()
        
        keys = p.key.get_pressed()
        
        if developer_mode:
            print("developer on")
        elif developer_mode:
            print("developer off")
        
        
        if player_create:
            if fly:
                if keys[p.K_w]:
                    player_pos_y -= 10
                elif keys[p.K_s]:
                    player_pos_y += 10

            if keys[p.K_a]:
                player_pos_x -= 10
            elif keys[p.K_d]:
                player_pos_x += 10

        clock.tick(fps)
        screen.fill(background_color)

        draw_player()

        p.display.flip()
        clock.tick(60)  # Değişiklik burada
