from tilemap import *
from tilemap import NUM_ROBOTS
import pygame
import random



class Agent(pygame.sprite.Sprite):


    def __init__(self, row,col):
        self.row = row
        self.col = col
        self.samples = 0
        self.ship_x = 0
        self.ship_y= 0
        self.in_ship = False
        self.obj = 10

    def get_pos(self):
        return self.row, self.col 
    
    def getobj(self):
        return self.obj
    
    def set_ship(self, x ,y):
        self.ship_x = x
        self.ship_y = y

    def north_sensor(self):
        return maze[self.row - 1][self.col] not in ('Z', 'G')

    def east_sensor(self):
        return maze[self.row][self.col + 1] not in ('Z', 'G')

    def south_sensor(self):
        return maze[self.row + 1][self.col] not in ('Z', 'G')

    def west_sensor(self):
        return maze[self.row][self.col - 1] not in ('Z', 'G')
    
    def sample_sensor(self):
        return maze[self.row][self.col] == 'R'

    def move_sensors(self):
        possible_moves = [] # U D

        if self.north_sensor():
            possible_moves.append('U')
        if self.east_sensor():
            possible_moves.append('R')
        if self.south_sensor():
            possible_moves.append('D')
        if self.west_sensor():
            possible_moves.append('L')

        return random.choice(possible_moves)

    def retreat(self):
        print("retirada")
        possible_moves = []

        if self.col < self.ship_x:
            if self.east_sensor():
                possible_moves.append('R')
        elif self.col > self.ship_x:
            if self.west_sensor():
                possible_moves.append('L')

        if self.row < self.ship_y:
            if self.south_sensor():
                possible_moves.append('D')
        elif self.row > self.ship_y:
            if self.north_sensor():
                possible_moves.append('U')
        
        if len(possible_moves) == 0:
            possible_moves = self.move_sensors()

        self.move(random.choice(possible_moves))


    def deliver(self):
        self.obj-=self.samples
        self.samples = 0
        self.move(self.move_sensors())
        print("entregado")
        

    def ship_sensor(self):
        return maze[self.row][self.col] == 'P'


    def check_action(self):

        if self.samples > 0:
            self.retreat()
            return

        self.move(self.move_sensors())

    
    def move(self, m):
  
        
        # Definir los cambios de fila y columna para cada movimiento
        moves = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }

        # Verificar si es un movimiento válido y actualizar la posición
        if m in moves:
            dr, dc = moves[m]
            new_row, new_col = self.row + dr, self.col + dc

            if maze[self.row][self.col] != 'P' and maze[self.row][self.col] == 'A':
                maze[self.row][self.col] = 'B'  # Actualizar la posición anterior
            self.row, self.col = new_row, new_col # Actualizar la posición actual
            if self.sample_sensor(): 
                self.samples+=1
                
            print(self.samples)