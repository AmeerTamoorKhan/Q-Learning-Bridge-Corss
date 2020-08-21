import pygame as pg
import sys
from BridgeCross import GameSetup as gs
from BridgeCross import Agent
import numpy as np


class MazeGame:

    pg.init()
    # maze = [
    #     "XXXXXXXXXXXXXXXXXXXX",
    #     "X        EXXXXXXX  G",
    #     "X XXXXXXX         EX",
    #     "X XXXXXXX XXXXXXXXEX",
    #     "X                X X",
    #     "X XXXXXXXXXXXXXXXX X",
    #     "X XE      E        X",
    #     "X XXXX XXXXXXXXXXX X",
    #     "XO       E         X",
    #     "XXXXXXXXXXXXXXXXXXXX"
    # ]
    maze = [
        "XXXXXXXXXXXXXXXXXXGXX",
        "X                   X",
        "X                   X",
        "XWWWWWWWWWWWWWWWWWWWX",
        "X     E             X",
        "X                   X",
        "XWWWWWWWWWWWWWWWWWWWX",
        "X                   X",
        "X         E         X",
        "X                   X",
        "X                   X",
        "XWWWWWWWWWWWWWWWWWWWX",
        "X        E          X",
        "XO                  X",
        "XXXXXXXXXXXXXXXXXXXXX"
    ]
    # maze = ["XXXXXXXXXXXXXXXXXXXXXXXX",
    #         "X      XXXXXXXXXXXXXXX G",
    #         "XEXXXX                 X",
    #         "X   EX XXXXXXXXXXXXX XEX",
    #         "X XXXX XXXXXXXXXXXXX X X",
    #         "X X                    X",
    #         "X X XXXXXXXXXXXXXXXXXX X",
    #         "X X XE               XEX",
    #         "X X XXXXXXXXXXXXXXXX X X",
    #         "X                      X",
    #         "X XXXXXXXXXXXXXXXXXXXXXX",
    #         "X                  XXXXX",
    #         "XOXXXXXXXXXXXXXXXX    EX",
    #         "XXXXXXXXXXXXXXXXXXXXXXXX"
    #         ]
    rows = len(maze)
    cols = len(maze[:][0])
    tileSize = 32
    width = len(maze[:][0])*tileSize                #640
    height = len(maze)*tileSize
    goal_position = 0
    agent_init = 0
    iter = 0
    Episodes = 1000

    def __init__(self):
        self.screen = pg.display.set_mode([self.width, self.height])
        pg.display.set_caption("Maze Runner")
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        self.GS = gs.GameSetup(self.screen, self.maze, self.tileSize)
        self.GS.setup()
        self.agent_object = Agent.Agent(self.screen, self.maze, self.tileSize)
        self.agent_init = (int(self.GS.agent[0][0] / self.tileSize), int(self.GS.agent[0][1] / self.tileSize))
        self.goal_position = (int(self.GS.goal[0][0]/self.tileSize), int(self.GS.goal[0][1]/self.tileSize))

    def reset(self):
        del self.GS
        gs.GameSetup.blocks = []
        gs.GameSetup.agent = []
        gs.GameSetup.bricks = []
        gs.GameSetup.goal = []
        gs.GameSetup.water = []
        gs.GameSetup.field = []
        self.GS = gs.GameSetup(self.screen, self.maze, self.tileSize)
        self.GS.setup()
        self.agent_object = Agent.Agent(self.screen, self.maze, self.tileSize)
        self.agent_init = (int(self.GS.agent[0][0] / self.tileSize), int(self.GS.agent[0][1] / self.tileSize))
        self.goal_position = (int(self.GS.goal[0][0] / self.tileSize), int(self.GS.goal[0][1] / self.tileSize))
        cord = tuple(self.tileSize*x for x in self.agent_init)
        gs.GameSetup.agent = [pg.draw.rect(self.screen, pg.Color('blue'),pg.Rect(cord, (self.tileSize, self.tileSize)))]
        return self.agent_init

    def score_text(self):
        text = self.font.render(f"Episode: {self.Episodes} Iteration: {int(self.iter)}", True, (255, 0, 0))
        self.screen.blit(text, [10, 10])

    def gameLoop(self, action):

        if action == 0:
            self.GS.agent[0][0] = self.GS.agent[0][0] + self.tileSize
            self.agent_object.agent_block('R')
            running, reward = self.agent_object.brick_move('R')
        if action == 1:
            self.GS.agent[0][1] = self.GS.agent[0][1] - self.tileSize
            self.agent_object.agent_block('U')
            running, reward = self.agent_object.brick_move('U')
        if action == 2:
            self.GS.agent[0][0] = self.GS.agent[0][0] - self.tileSize
            self.agent_object.agent_block('L')
            running, reward = self.agent_object.brick_move('L')
        if action == 3:
            self.GS.agent[0][1] = self.GS.agent[0][1] + self.tileSize
            self.agent_object.agent_block('D')
            running, reward = self.agent_object.brick_move('D')


        self.GS.draw_scene()
        #running, reward = self.agent_object.agent_enemy_goal()
        self.score_text()

        # if self.iter >= 900:
        #     pg.display.update()

        self.iter = self.iter + 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        return [(int(self.GS.agent[0][0]/self.tileSize), int(self.GS.agent[0][1]/self.tileSize)), reward, running, self.iter]
