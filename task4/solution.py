class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    COLUMN_NUMBERS = '321'
    ROW_LETTERS = 'ABC'
    VALUES = ['X', 'O']
    GAME_IN_PROGRESS = 'Game in progress.'
    DRAW = 'Draw!'
    X_WINS = 'X wins!'
    O_WINS = 'O wins!'
    BOARD_SIZE = 3

    def __init__(self):
        self.KEYS = [row + column
                     for column in self.COLUMN_NUMBERS
                     for row in self.ROW_LETTERS]

        self.board = dict()
        self.status = self.GAME_IN_PROGRESS
        self.last_move = None

    def __getitem__(self, key):
        return self.board.get(key, ' ')

    def __setitem__(self, key, value):
        if key in self.board:
            raise InvalidMove
        elif key not in self.KEYS:
            raise InvalidKey
        elif value not in self.VALUES:
            raise InvalidValue
        elif value == self.last_move:
            raise NotYourTurn
        else:
            self.board[key] = value
            self.last_move = value
            self.update_game_status()

    def update_game_status(self):
        if self.status == self.GAME_IN_PROGRESS:
            for value in self.VALUES:
                if any(len([row + column
                            for row in self.ROW_LETTERS
                            if self.board.get(row + column, None) == value]) ==
                       self.BOARD_SIZE
                       for column in self.COLUMN_NUMBERS):
                    self.status = getattr(self, value + '_WINS')
                    return

                elif any(len([row + column
                              for column in self.COLUMN_NUMBERS
                              if self.board.get(row + column, None) == value]) ==
                         self.BOARD_SIZE
                         for row in self.ROW_LETTERS):
                    self.status = getattr(self, value + '_WINS')
                    return

                elif len([row + column
                          for row, column
                          in zip(self.ROW_LETTERS,
                                 reversed(self.COLUMN_NUMBERS))
                          if self.board.get(row + column, None) == value]) ==\
                        self.BOARD_SIZE:
                    self.status = getattr(self, value + '_WINS')
                    return

                elif len([row + column
                          for row, column
                          in zip(self.ROW_LETTERS, self.COLUMN_NUMBERS)
                          if self.board.get(row + column, None) == value]) ==\
                        self.BOARD_SIZE:
                    self.status = getattr(self, value + '_WINS')
                    return

            if len(self.board) == len(self.KEYS):
                self.status = self.DRAW

    def __str__(self):
        return ('\n' +
                '  -------------\n' +
                '3 | {} | {} | {} |\n' +
                '  -------------\n' +
                '2 | {} | {} | {} |\n' +
                '  -------------\n' +
                '1 | {} | {} | {} |\n' +
                '  -------------\n' +
                '    A   B   C  \n').format(*[self.board.get(key, " ")
                                              for key in self.KEYS])

    def game_status(self):
        return self.status
