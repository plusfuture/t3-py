CONST_BLANK = ' '

class T3Game:
    def __init__(self):
        self.board = Board()
            
    def setup(self):
        self.p1 = Player(None, 1)
        self.p2 = Player(None, 2)
        self.assign_shape(self.p1)
        self.assign_shape(self.p2)

        print('Done setting up.\n')

    def assign_shape(self, player):
        while True:
            shape = input('P' + str(player.name) + ': Please indicate your desired shape: ')

            if len(shape) > 1 or not shape.isalpha():
                print('Shape must be one alphabetical character only.')
                continue
            
            player.shape = shape # fix this ugly bit somehow

            if self.p2.shape == self.p1.shape: 
                print('Shape must be different from player 1\'s shape!')
                continue

            break

    def make_move(self, player):
        while True:
            p_move_s = input('Player ' + str(player.name) + ': indicate cell for your move: ')
            if not p_move_s.isnumeric():
                print('You must enter a number..')
                continue

            p_move = int(p_move_s)
            if p_move < 1 or p_move > 9:
                print('Cell must be between 1 and 9..')
                continue
            if not self.place(player, p_move):
                print('Cell already taken. Pick another cell.')
                continue

            print('Succesfully placed ' + str(player.shape) + ' to ' + str(p_move))
            break
    
    def get_coords(self, move):
        if move < 4:
            cell_x = 0
            cell_y = move - 1
        elif move < 7:
            cell_x = 1
            cell_y = move - 4
        elif move < 10:
            cell_x = 2
            cell_y = move - 7

        return (cell_x, cell_y)
        
    def place(self, player, move):
        cell = self.get_coords(move)
        cell_x = cell[0]
        cell_y = cell[1]
        if self.board.grid[cell_x][cell_y] == CONST_BLANK:
            self.board.grid[cell_x][cell_y] = player.shape
            return True
        return False

    def get_winner(self):
        win_shape = self.board.get_winner_shape();
        if win_shape is not None:
            if win_shape == self.p1.shape:
                return self.p1
            else: return self.p2
        return None
    
    def check_winner(self, player):
        pass
        

class Player:
    def __init__(self, shape, name):
        if shape is None: # defaults for players
            if name == 1:
                self.shape = 'o'
            else: self.shape = 'x'
        self.shape = shape
        self.name = name


class Board:
    def __init__(self):
        self.grid = []
        self.grid.append([CONST_BLANK, CONST_BLANK, CONST_BLANK])
        self.grid.append([CONST_BLANK, CONST_BLANK, CONST_BLANK])
        self.grid.append([CONST_BLANK, CONST_BLANK, CONST_BLANK])
               
    def print(self):
        print('Current board looks like: ')
        for row in self.grid:
            for i in range(0, len(row)):
                print(row[i], end="")
                if i != 2:
                    print('|', end="")
            print('\n-----')
    
    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == CONST_BLANK:
                    return False
        return True

    def get_winner_shape(self):
         # check rows
        for row in self.grid:
            has_match = True
            match = row[0]
            for cell in row:
                if cell == CONST_BLANK:
                    has_match = False
                    break
                if match != cell:
                    has_match = False
                    break
            if has_match:
                return match

        # check cols
        for i in range(0,len(self.grid)):
            has_match = True
            match = self.grid[0][i]
            for k in range(0,len(self.grid)):
                cur = self.grid[k][i]
                if cur == CONST_BLANK:
                    has_match = False
                    break
                if match != cur:
                    has_match = False
                    break
            if has_match:
                return match

        # check diags
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            if self.grid[0][0] != CONST_BLANK:
                return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            if self.grid[0][2] != CONST_BLANK:
                return self.grid[0][2]

        return None


        
t3 = T3Game()
print('Welcome to Tic-tac-toe!')
print('You can specify your move by entering a cell\'s corresponding number:')
print('1|2|3')
print('-----')
print('4|5|6')
print('-----')
print('7|8|9')
print('')
t3.setup()

while True:
    t3.board.print()

    t3.make_move(t3.p1)
    t3.board.print()
    winner = t3.get_winner()
    if winner is not None:
        print('Player ' + str(winner.name) + ' wins!')
        break
    if t3.board.is_full():
        print('Game over; no winner!')
        break

    t3.make_move(t3.p2)
    t3.board.print()
    winner = t3.get_winner()
    if winner is not None:
        print('Player ' + str(winner.name) + ' wins!')
        break
    if t3.board.is_full():
        print('Game over; no winner!')
        break

    






