from BridgeCross import GameSetup as gs
GS = gs.GameSetup


class Agent(GS):

    def __init__(self, screen, maze, tilesize):
        GS.__init__(self, screen=screen, maze=maze, tilesize=tilesize )
        self.tilesize = tilesize
        self.brick_count = list(range(len(gs.GameSetup.bricks)))
    def agent_block(self, dir):
        x, y = gs.GameSetup.agent[0][0]/self.tilesize, gs.GameSetup.agent[0][1]/self.tilesize

        for i in range(len(GS.blocks)):
            X = GS.blocks[i][0]/self.tilesize
            Y = GS.blocks[i][1]/self.tilesize
            if x == X and y == Y:
                if dir == 'R':
                    gs.GameSetup.agent[0][0] = gs.GameSetup.agent[0][0] - self.tilesize
                if dir == 'U':
                    gs.GameSetup.agent[0][1] = gs.GameSetup.agent[0][1] + self.tilesize
                if dir == 'L':
                    gs.GameSetup.agent[0][0] = gs.GameSetup.agent[0][0] + self.tilesize
                if dir == 'D':
                    gs.GameSetup.agent[0][1] = gs.GameSetup.agent[0][1] - self.tilesize



        for i in range(len(GS.water)):
            X = GS.water[i][0]/self.tilesize
            Y = GS.water[i][1]/self.tilesize
            if x == X and y == Y:
                if dir == 'R':
                    gs.GameSetup.agent[0][0] = gs.GameSetup.agent[0][0] - self.tilesize
                if dir == 'U':
                    gs.GameSetup.agent[0][1] = gs.GameSetup.agent[0][1] + self.tilesize
                if dir == 'L':
                    gs.GameSetup.agent[0][0] = gs.GameSetup.agent[0][0] + self.tilesize
                if dir == 'D':
                    gs.GameSetup.agent[0][1] = gs.GameSetup.agent[0][1] - self.tilesize

    def brick_move(self, dir):
        x, y = gs.GameSetup.agent[0][0] / self.tilesize, gs.GameSetup.agent[0][1] / self.tilesize

        for i in range(len(gs.GameSetup.bricks)):
            X = GS.bricks[i][0] / self.tilesize
            Y = GS.bricks[i][1] / self.tilesize
            if i == self.brick_count[i]:
                if x == X and y == Y:
                    if dir == 'R':
                        gs.GameSetup.bricks[i][0] = gs.GameSetup.bricks[i][0] + self.tilesize
                        for k in range(len(gs.GameSetup.blocks)):
                            Bx = gs.GameSetup.blocks[k][0]
                            By = gs.GameSetup.blocks[k][1]
                            if (gs.GameSetup.bricks[i][0] == Bx) and (gs.GameSetup.bricks[i][1] == By):
                                gs.GameSetup.bricks[i][0] = gs.GameSetup.bricks[i][0] - self.tilesize
                    if dir == 'U':
                        gs.GameSetup.bricks[i][1] = gs.GameSetup.bricks[i][1] - self.tilesize
                        for j in range(len(gs.GameSetup.water)):
                            if (gs.GameSetup.bricks[i][0] == gs.GameSetup.water[j][0]) and (gs.GameSetup.bricks[i][1] == gs.GameSetup.water[j][1]):
                                gs.GameSetup.water[j] = [0, 0, 0, 0]
                                self.brick_count[i] = len(gs.GameSetup.bricks) + 1
                                return [True, 20]
                        return [True, 10]
                    if dir == 'L':
                        gs.GameSetup.bricks[i][0] = gs.GameSetup.bricks[i][0] - self.tilesize
                        for l in range(len(gs.GameSetup.blocks)):
                            Bx = gs.GameSetup.blocks[l][0]
                            By = gs.GameSetup.blocks[l][1]
                            if (gs.GameSetup.bricks[i][0] == Bx) and (gs.GameSetup.bricks[i][1] == By):
                                gs.GameSetup.bricks[i][0] = gs.GameSetup.bricks[i][0] + self.tilesize
                    if dir == 'D':
                        gs.GameSetup.bricks[i][1] = gs.GameSetup.bricks[i][1] + self.tilesize


        if (x == gs.GameSetup.goal[0][0]/self.tilesize) and (y == gs.GameSetup.goal[0][1]/self.tilesize):
            return [False, 10]

        return [True, -1]

    # def agent_enemy_goal(self):
    #     x, y = gs.GameSetup.agent[0][0] / self.tilesize, gs.GameSetup.agent[0][1] / self.tilesize
    #
    #     for i in range(len(GS.enemies)):
    #         X1 = GS.enemies[i][0]/self.tilesize
    #         Y1 = GS.enemies[i][1]/self.tilesize
    #         if len(GS.goal)-1 >= i:
    #             X2 = GS.goal[i][0] / self.tilesize
    #             Y2 = GS.goal[i][1] / self.tilesize
    #         if x == X1 and y == Y1:
    #             return [True, -10]
    #         elif x == X2 and y == Y2:
    #             return [False, 10]
    #     return [True, -1]






