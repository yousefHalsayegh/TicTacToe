from copy import deepcopy
class Board:
    
    matrix= []
    status = -1
    turn = -1
    condition = -1
    index = -1

    def __init__(self):
        self.matrix = [[None] * 3, [None] * 3, [None] * 3]
        self.turn = 0
    
    def reset(self):
        """
        This method reset all the variables inside
        the board to start a new game
        """
        self.matrix = [[None] * 3, [None] * 3, [None] * 3]
        self.turn = 0
        self.status = -1
        self.condition = -1

    def legal_moves(self):
        """
        return:
        moves: a list of moves
        -----------------------------------------
        This method check all the possible moves you 
        can take in your turn 
        """
        moves = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] is None:
                    moves.append((i + 1, j + 1))
        #print(moves)
        return moves

    def terminal_test(self):
        """
        this method does a test to check if the board
        reached a terminal state as in one player 
        won or its a draw
        """
        for row in range (0,3):
            if ((self.matrix [row][0] == self.matrix[row][1] == self.matrix[row][2]) and(self.matrix [row][0] is not None)):
                return 0 if self.matrix[row][0] == 'X' else 1

        for col in range (0, 3):
            if (self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col]) and (self.matrix[0][col] is not None):
                return 0 if self.matrix[row][0] == 'X' else 1

        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) and (self.matrix[0][0] is not None):
            return 0 if self.matrix[row][0] == 'X' else 1


        if (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]) and (self.matrix[0][2] is not None):
            return 0 if self.matrix[row][0] == 'X' else 1

        if(all([all(row) for row in self.matrix]) and self.status == -1 ):
            return 2

        return -1


    def terminal(self):
        """
        return:
        status: who won in this match or if its a draw
        condition: used to see if the game ended with
        a row, coloum or diagonal win
        index: saves the row or coloum that lead 
        to victory
        ----------------------------------------------
        this method does a test to check if the board
        reached a terminal state as in one player 
        won or its a draw
        """
        for row in range (0,3):
            if ((self.matrix [row][0] == self.matrix[row][1] == self.matrix[row][2]) and(self.matrix [row][0] is not None)):
                self.status =  0 if self.matrix[row][0] == 'X' else 1
                self.condition = 1 
                self.index = row
                break

        for col in range (0, 3):
            if (self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col]) and (self.matrix[0][col] is not None):
                self.status =  0 if self.matrix[0][col] == 'X' else 1
                self.condition = 2
                self.index = col
                break

        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) and (self.matrix[0][0] is not None):
            self.status =  0 if self.matrix[0][0] == 'X' else 1
            self.condition = 3

        if (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]) and (self.matrix[0][2] is not None):
            self.status =  0 if self.matrix[0][2] == 'X' else 1
            self.condition = 4

        if(all([all(row) for row in self.matrix]) and self.status == -1 ):
            self.status = 2

    def utility(self, id, status):
        """
        args:
        id: the player id 0 being X and 1 being O
        -----------------------------------------
        return:
        inf if its the current player that won
        -inf if he/she lost
        0 if its a draw
        ----------------------------------------
        this method checks if the winner
        is the current player or if its 
        a draw
        """
        if(status == id):
            return float("inf")
        elif(status == 2):
            return 0
        else:
            return float('-inf')

    def check(self, id):
        """
        args: 
        id: the player id 0 if X 1 if O
        -----------------------------------------
        return:
        The number of possible player wins - number of possible
        oppopent wins
        ------------------------------------------
        This the heuristic to help the Ai choose
        the best move currently
        """
        player = ''
        playerc = 0
        opp = ''
        oppc = 0
        if id == 0:
            player = 'X'
            opp = 'O'
        else:
            player = 'O'
            opp = 'X'

        for row in range (0,3):

            if ((self.matrix [row][0] == self.matrix[row][1]) and self.matrix[row][2] is None):
                if(self.matrix[row][0] == player):
                    playerc += 1
                else:
                    oppc += 1

            if ((self.matrix [row][0] == self.matrix[row][2]) and self.matrix[row][1] is None):
                if(self.matrix[row][0] == player):
                    playerc += 1
                else:
                    oppc += 1

            if ((self.matrix [row][1] == self.matrix[row][2]) and self.matrix[row][0] is None):
                if(self.matrix[row][1] == player):
                    playerc += 1
                else:
                    oppc += 1

        for col in range (0, 3):

            if ((self.matrix [0][col] == self.matrix[1][col]) and self.matrix[2][col] is None):
                if(self.matrix[0][col] == player):
                    playerc += 1
                else:
                    oppc += 1

            if ((self.matrix [0][col] == self.matrix[2][col]) and self.matrix[1][col] is None):
                if(self.matrix[0][col] == player):
                    playerc += 1
                else:
                    oppc += 1

            if ((self.matrix [1][col] == self.matrix[2][col]) and self.matrix[0][col] is None):
                if(self.matrix[1][col] == player):
                    playerc += 1
                else:
                    oppc += 1


        
        if ((self.matrix [0][0] == self.matrix[1][1]) and self.matrix[2][2] is None):
                if(self.matrix[0][0] == player):
                    playerc += 1
                else:
                    oppc += 1

        if ((self.matrix [0][0] == self.matrix[2][2]) and self.matrix[1][1] is None):
            if(self.matrix[0][0] == player):
                playerc += 1
            else:
                oppc += 1

        if ((self.matrix [1][1] == self.matrix[2][2]) and self.matrix[0][0] is None):
            if(self.matrix[1][1] == player):
                playerc += 1
            else:
                oppc += 1



        if ((self.matrix [0][2] == self.matrix[1][1]) and self.matrix[2][0] is None):
                if(self.matrix[0][2] == player):
                    playerc += 1
                else:
                    oppc += 1

        if ((self.matrix [0][2] == self.matrix[2][0]) and self.matrix[1][1] is None):
            if(self.matrix[0][2] == player):
                playerc += 1
            else:
                oppc += 1

        if ((self.matrix [1][1] == self.matrix[2][0]) and self.matrix[0][2] is None):
            if(self.matrix[1][1] == player):
                playerc += 1
            else:
                oppc += 1

        return playerc - oppc


    def result(self, action): 
        """
        args:
        action: the action we want to test on
        -------------------------------------
        This create a copy of the board 
        so we can test a new move on it
        """
        assert action in self.legal_moves()
        newBoard = deepcopy(self)
        newBoard.matrix[action[0]-1][action[1]-1] = 'X' if newBoard.turn == 0 else 'O'
        newBoard.turn ^= 1
        return newBoard
