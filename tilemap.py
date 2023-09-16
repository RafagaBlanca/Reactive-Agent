import pygame
from agent import *


TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 5

# texture of colors
YELLOW  = (255, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0 , 0, 255)
GREEN   = (0, 255, 0)
BROWN   = (160, 82, 45)
PURPLE  = (125, 2, 247)
BLACK   = (0,0,0)



def create_texture(color):
    image = pygame.Surface((TILE_SIZE, TILE_SIZE))
    image.fill(color)
    return image

# 0x0 -> grass
# 0xb -> dirt
textures = {
    'G' : create_texture(GREEN),
    'B' : create_texture(BROWN),
    'Y' : create_texture(YELLOW),
    'A' : create_texture(BLUE),
    'P' : create_texture(PURPLE),
    'R' : create_texture(RED),
    'Z' : create_texture(BLACK)
}

tiles = ['G', 'B', 'Y','A', 'P','R', 'Z']

maze = [
    ['Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z'],
    ['Z','B','B','B','B','B','B','B','B','B','B','B','R','B','B','B','B','B','P','Z'],
    ['Z','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','Z'],
    ['Z','B','B','B','B','B','R','B','G','B','B','B','B','B','B','B','B','B','B','Z'],
    ['Z','B','B','R','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','Z'],
    ['Z','B','B','B','B','B','B','B','B','B','B','G','B','B','B','B','B','B','B','Z'],
    ['Z','B','B','B','B','G','B','B','B','B','B','B','B','B','B','B','B','B','B','Z'],
    ['Z','B','B','B','B','B','B','B','B','B','B','R','B','B','B','B','B','B','B','Z'],
    ['Z','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','Z'],
    ['Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z','Z'],
]


def agent_set(player):
    x, y = player.get_pos()
    maze[x][y] = 'A'

def agent_update(player):
    player.check_action()
    x, y = player.get_pos()
    maze[x][y]='B'
    x, y = player.get_pos()
    maze[x][y] = 'A'


def draw(screen, player):
    agent_update(player)
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = textures[maze[row][column]]
            screen.blit(tile, (x, y))
