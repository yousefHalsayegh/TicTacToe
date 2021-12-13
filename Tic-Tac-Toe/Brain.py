import random

class Agent:

    turn = 0
    def __init__(self, type, player):
        self.type = type
        self.player = player

    def action(self, board):
        row = 0
        col = 0
        
        #Random AI 
        if self.type == 0:
            check = False 
            while (not check): 
                row = random.randint(1, 3)
                col = random.randint(1, 3)
                if(row and col and board.matrix[row - 1][col - 1] is None):
                    check = True

        elif self.type == 1:
            row, col = self.min_max(board, 2)
        elif self.type == 2:
            row, col = self.min_max(board, 4)

        print(f"The best action is ({row},{col})")
        return row, col


    def min_max(self, board, depth):
        pass
    
    def min_value(self, board, depth):
        pass

    def max_value(self, board, depth):
        pass


    