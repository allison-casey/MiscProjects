

class TicTacToe(object):

    """Container for the game Tic Tac Toe"""

    def __init__(self):
        """Create the board"""
        self._board = [ [-1 
                        for x in range(3)]
                            for y in range(3)]
    
    def get_row(self, row):
        return self._board[row]
    
    def get_column(self, column):
        return [c[column] for c in self._board]

    def move(self, player, position_x, position_y):
        if player not in [0, 1]:
            return -1
        if position_x < 0 or position_x > 3:
            return -1
        if position_y < 0 or position_y > 3:
            return -1
        
        if self._board[position_x][position_y] == -1:
            self._board[position_x][position_y] = player
            return 1
        else:
            return -1
        return 0


    def winner(self):
        
        for player in [0, 1]:
            win = [player for num in range(3)]
            if  self._board[0] == win or \
                self._board[1] == win or \
                self._board[2] == win or \
                self.get_column(0) == win or \
                self.get_column(1) == win or \
                self.get_column(2) == win or \
                [self._board[i][i] for i in range(3)] == win or \
                [row[-i-1] for i, row in enumerate(self._board) ] == win:
                return player

        return  -1
        
        
    def __str__(self):
        s = '{}\n{}\n{}'.format(self._board[0], self._board[1], self._board[2])

        return s

if __name__ == "__main__":
    
    game = TicTacToe()
    
    num_rounds = 0
    while game.winner() == -1:
        print('--------------- ROUND {} --------------'.format(num_rounds))
        print(game)
        while True:
            print("X", 'enter your square')
            if game.move(0, input("Enter row: "), input("Enter column: ")):
                break

        print(game)
        while True:
            print("O, enter your square")
            if game.move(1, input("Enter row: "), input("Enter column: ")):
                break










