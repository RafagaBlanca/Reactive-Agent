from tilemap import maze
import pygame
import random



class Agent(pygame.sprite.Sprite):


    def __init__(self, row,col):
        self.row = row
        self.col = col
        self.samples = 0

    def get_pos(self):
        return self.row, self.col 

        
        
    
    def check_action(self):
        possile_moves = []

        if(maze[self.row][self.col]=='R'):
            self.samples+=1

        if(maze[self.row][self.col+1]!='Z' and maze[self.row][self.col+1]!='G'):
            possile_moves.append('R')
        if(maze[self.row][self.col-1]!='Z' and maze[self.row][self.col-1]!='G'):
            possile_moves.append('L')
        if(maze[self.row-1][self.col]!='Z' and maze[self.row-1][self.col]!='G'):
            possile_moves.append('U')
        if(maze[self.row+1][self.col]!='Z' and maze[self.row+1][self.col]!='G'):
            possile_moves.append('D')
        self.move(possile_moves)
    
    def move(self, possible_moves):
        
        m = possible_moves[random.randint(0,len(possible_moves)-1)]
        if(m=='R'):
            self.col+=1
        if(m=='L'):
            self.col-=1
        if(m=='U'):
            self.row-=1
        if(m=='D'):
            self.row+=1