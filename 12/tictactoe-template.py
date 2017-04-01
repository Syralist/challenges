DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)

DEBUG = True

def clear():
    if not DEBUG:
        print("\n" * 100)


class TicTacToe:

    def __init__(self):
        '''Constructor, below worked well for us ...'''
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    def __str__(self):
        '''Print the board'''
        return "\n".join([" ".join(self.board[1:4])," ".join(self.board[4:7])," ".join(self.board[7:10])," "])

    def setPosition(self, pos, token):
        try:
            # if self.board[pos] == DEFAULT:
            if pos in VALID_POSITIONS:
                self.board[pos] = token
                VALID_POSITIONS.remove(pos)
                return True
            else:
                print("Position invalid: ", pos) 
                return False
        except IndexError as e:
            print("invalid Position: ", pos) 
            return False

    def is_win(self, token):
        for comb in WINNING_COMBINATIONS:
            num = 0
            for p in comb:
                if self.board[p] == DEFAULT:
                    break
                elif self.board[p] == token:
                    num += 1

            if num == 3:
                return True

        return False

    def is_draw(self):
        if len(VALID_POSITIONS > 0):
            return False
        else:
            return True



    # TODOS:
    # display board in __str__ (clearing screen)
    # have at least an is_win method to exit game
    # num turns = len(VALID_POSITIONS) so might not need is_draw (tie) method
    # have method(s) to get user input and validate
    # if playing against computer (AI) calculate next best move (algorithm)
    # update board upon each turn

class Player:
    def __init__(self, game, token):
        self.game = game
        self.token = token

    def move(self):
        pos = int(input("where to draw?"))
        while not game.setPosition(pos, self.token):
            pos = int(input("where to draw?"))

class AI:
    def __init__(self, game, token, level):
        self.game = game
        self.token = token
        self.level = level


if __name__ == "__main__":
    game = TicTacToe()
    player1 = Player(game, "X")
    while True:
        clear()
        print(game)
        player1.move()
        if game.is_win("X"):
            print("player won!")
            break
        elif game.is_draw():
            print("its a tie!")
            break
        # game.setPosition(1, "X")
        # clear()
        # print(game)
        # game.setPosition(1, "O")
        # clear()
        # print(game)
        # game.setPosition(2, "O")
        # clear()
        # print(game)
        # print(game.is_win("O"))
        # player1.move()
        # game.setPosition(4, "X")
        # clear()
        # print(game)
        # game.setPosition(5, "O")
        # clear()
        # print(game)
        # player1.move()
        # game.setPosition(7, "X")
        # clear()
        # print(game)
        # print(game.is_win("X"))
        # break
        # take turn
        # make move
        # check win - break
        #
        # ask if another game, if n - break
