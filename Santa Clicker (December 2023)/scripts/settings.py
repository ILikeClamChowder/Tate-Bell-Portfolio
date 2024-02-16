import os.path

import pygame as pg
import random
import math
import time

TITLE = "Santa Clicker"
WIDTH = 1280
HEIGHT = 720
FPS = 60
tile_count = (16, 9)
tile_size = (WIDTH/tile_count[0], HEIGHT/tile_count[1])
tile_width = tile_size[0]
tile_height = tile_size[1]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY1 = (80, 80, 80)
GREY2 = (120, 120, 120)
GREY3 = (160, 160, 160)
GREY4 = (200, 200, 200)
GREY5 = (240, 240, 240)

game_dir = os.path.dirname(__file__)
game_dir = game_dir.replace("\dropper", "")
assets_dir = os.path.join(game_dir,"assets/")
maps_dir = os.path.join(assets_dir,"maps")
sounds_dir = os.path.join(assets_dir, "sounds")
sprite_dir = os.path.join(assets_dir, "sprites")

print(game_dir)

def draw_text(screen, text, size, color, x, y, font="broadway"):
    font_name = pg.font.match_font(font)
    font = pg.font.Font(font_name, size)
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.midtop = (x, y)
    screen.blit(text_img, rect)

def draw_screen(path, x, y, screen):
    test_img = pg.image.load(path).convert_alpha()
    test_img = pg.transform.scale(test_img, (WIDTH, HEIGHT))
    rect = test_img.get_rect()
    rect.x = x
    rect.y = y
    screen.blit(test_img, rect)
