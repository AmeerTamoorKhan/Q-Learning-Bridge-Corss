import pygame as pg
import numpy as np

class GameSetup:
    blocks = []
    agent = []
    bricks = []

    goal = []
    water = []
    field = []
    def __init__(self, screen, maze, tilesize):
        self.screen = screen
        self.maze = maze
        self.tilesize = tilesize
        self.font = pg.font.SysFont(None, 20)

    def setup(self):
        for rows in range(len(self.maze)):
            for cols in range(len(self.maze[0][:])):
                if self.maze[rows][cols] == 'X':
                    self.blocks.append(pg.draw.rect(self.screen, pg.Color('black'), pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize))))
                elif self.maze[rows][cols] == 'G':
                    self.goal.append(pg.draw.rect(self.screen, pg.Color('green'),pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize))))
                elif self.maze[rows][cols] == 'E':
                    self.bricks.append(pg.draw.rect(self.screen, pg.Color('red'),pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize))))
                elif self.maze[rows][cols] == 'O':
                    self.agent.append(pg.draw.rect(self.screen, pg.Color('blue'),pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize))))
                elif self.maze[rows][cols] == 'W':
                    self.water.append(pg.draw.rect(self.screen, pg.Color('blue'),pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize))))

    def draw_scene(self):
        self.screen.fill((255, 255, 255))
        for rows in range(len(self.maze)):
            for cols in range(len(self.maze[:][0])):
                if self.maze[rows][cols] == 'X':
                    pg.draw.rect(self.screen, pg.Color('black'), pg.Rect((cols*self.tilesize, rows*self.tilesize), (self.tilesize, self.tilesize)))
                elif self.maze[rows][cols] == 'G':
                    pg.draw.rect(self.screen, pg.Color('green'), pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize)))
                elif self.maze[rows][cols] == 'O':
                    pg.draw.rect(self.screen, pg.Color('blue'), pg.Rect((self.agent[0][0], self.agent[0][1]), (self.tilesize, self.tilesize)))
                elif self.maze[rows][cols] == 'W':
                    pg.draw.rect(self.screen, pg.Color('blue'), pg.Rect((cols * self.tilesize, rows * self.tilesize), (self.tilesize, self.tilesize)))

        for i in range(len(self.bricks)):
            pg.draw.rect(self.screen, pg.Color('red'), pg.Rect((self.bricks[i][0], self.bricks[i][1]), (self.tilesize, self.tilesize)))

    def draw_table(self, q_table):
        for rows in range(len(self.maze)):
            for cols in range(len(self.maze[:][0])):
                if self.maze[rows][cols] == ' ':
                    q_value = np.argmax(q_table[cols][rows])
                    text1 = self.font.render(str(q_value), True, (255, 0, 0))
                    self.screen.blit(text1, [cols * self.tilesize +10, rows * self.tilesize+10])
                elif self.maze[rows][cols] == 'G':
                    q_value = np.argmax(q_table[cols][rows])
                    text1 = self.font.render(str(q_value), True, (255, 0, 0))
                    self.screen.blit(text1, [cols * self.tilesize +10, rows * self.tilesize+10])
                elif self.maze[rows][cols] == 'E':
                    q_value = np.argmax(q_table[cols][rows])
                    text1 = self.font.render(str(q_value), True, (255, 0, 0))
                    self.screen.blit(text1, [cols * self.tilesize +10, rows * self.tilesize+10])
                elif self.maze[rows][cols] == 'O':
                    q_value = np.argmax(q_table[cols][rows])
                    text1 = self.font.render(str(q_value), True, (255, 0, 0))
                    self.screen.blit(text1, [cols * self.tilesize +10, rows * self.tilesize+10])




