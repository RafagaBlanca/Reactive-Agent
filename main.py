import pygame
import random

from agent import Agent
from tilemap import *

# we initialize pygame module
pygame.init()

clock = pygame.time.Clock()

# create a surface represent our window
screen = pygame.display.set_mode((1280, 960))
# agent creation
random_row = random.randint(1, n - 2)
random_col = random.randint(1, m - 2)
player = Agent(random_row, random_col)
home(player)
agent_set(player)

def main():
    running = True
    # the game loop
    while running:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # draw
        draw(screen,player)


        # update

        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()