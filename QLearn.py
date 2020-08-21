from BridgeCross import Main
from BridgeCross import GameSetup as gs
import pygame as pg
import numpy as np

LR = 0.1
ED = 0.95
ER = 1
max_ER = 1
min_ER = 0.01
decay_ER = 0.01

Maze = Main.MazeGame()
Episodes = Maze.Episodes = 10000

screen = Maze.screen
Observation = [Maze.cols, Maze.rows]
Action = 4

q_table = np.load('q_table_bridge.npy')
#np.random.uniform(low=-2, high=2, size=(Observation+[Action]))
reward_episodes = []
clock = pg.time.Clock()
iter = 0

for i in range(Episodes):
    Maze.Episodes = Maze.Episodes - (Maze.Episodes - i)
    done = True
    state = Maze.reset()
    Maze.iter = 0
    reward_current_episode = 0
    while done and Maze.iter <= 1000:

        clock.tick(60)
        thershold_ER = np.random.uniform(low=0, high=1)
        #if thershold_ER > ER:
        action = np.argmax(q_table[state])
        #else:
            #action = np.random.randint(low=0, high=4)

        new_state, reward, done, Maze.iter = Maze.gameLoop(action)

        max_q = np.max(q_table[new_state])
        old_q = q_table[state+(action, )]
        new_q = ((1 - LR)*old_q + LR*(reward + ED*max_q))
        q_table[state+(action, )] = new_q

        reward_current_episode = reward_current_episode + reward
        state = new_state

        print(new_state, Maze.iter, i, reward_current_episode, ER)
        if i % 10 == 0:
            Maze.GS.draw_table(q_table)
            pg.display.update()

    reward_episodes.append(reward_current_episode)
    ER = min_ER + (max_ER - min_ER)*np.exp(-decay_ER*i)









