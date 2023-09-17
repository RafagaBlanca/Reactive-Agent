import pygame
from agent import *
import random


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

""" maze = [
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
] """

n = 10
m = 20

# Crear un laberinto vacío lleno de espacios ' '
maze = [[' ' for _ in range(m)] for _ in range(n)]

# Definir constantes
NUM_GOALS = 10
NUM_ROBOTS = 10

random_row = random.randint(1, n - 2)
random_column = random.randint(1, m - 2)
# Colocar al jugador 'P' en una posición específica
maze[random_row][random_column] = 'P'


def home(player):
    player.set_ship(random_column, random_row)

for i in range(n):
    maze[i][0] = 'Z'
    maze[i][m-1] = 'Z'
for j in range(m):
    maze[0][j] = 'Z'
    maze[n-1][j] = 'Z'
# Función para colocar elementos aleatorios en el laberinto
def place_elements(element, num_elements):
    count = 0
    while count < num_elements:
        random_row = random.randint(1, n - 2)
        random_column = random.randint(1, m - 2)
        if maze[random_row][random_column] == ' ':
            maze[random_row][random_column] = element
            count += 1

# Colocar 'G' (metas) en el laberinto
place_elements('G', NUM_GOALS)

# Colocar 'R' (robots) en el laberinto
place_elements('R', NUM_ROBOTS)

# Llenar el laberinto con 'B' (bloques) donde no haya otros elementos
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if maze[i][j] == ' ':
            maze[i][j] = 'B'

def agent_set(player):
    x, y = player.get_pos()
    maze[x][y] = 'A'

def agent_update(player):
    player.check_action()
    if player.ship_sensor():
        player.deliver()
        x, y = player.get_pos()
        maze[x][y] = 'A'
        print(x,y)
        return
    x,y = player.get_pos()
    maze[x][y] = 'A'


def draw(screen, player):
    agent_update(player)
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = textures[maze[row][column]]
            screen.blit(tile, (x, y))
