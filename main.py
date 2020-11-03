BOARD_SIZE = 8

def Board_Indexes():
  board_idx = [[j for j in range(0, BOARD_SIZE)] for i in range(0, BOARD_SIZE)]
  print('This is what the board looks like:\n{}'.format(board_idx))

def Instructions():
  print('There are a total of 5 ships:')
  print('Carrier - occupies 5 spaces')
  print('Battleship - occupies 4 spaces')
  print('Submarine - occupies 3 spaces')
  print('Cruiser - occupies 3 spaces')
  print('Destroyer - occupies 2 spaces')

  Board_Indexes()


class Player:
  def __init__(self, name='User', active_symbol = 'o'):
    self.name = name
    self.board = [['.' for j in range(0, BOARD_SIZE)] for i in range(0, BOARD_SIZE)]
    self.ACTIVE_SYMBOL = active_symbol
    '''
     Ex. (([(1,4),(1,7)], 'o'):
      1,4 is start location, 1,7 is end location 
      'o' is the symbol meaning:
        'o' is an active ship, 'x' is a sunken ship
    '''
    self.ships = {
      'Carrier': [0, 'x'], 
      'Battleship': [0, 'x'],
      'Cruiser': [0, 'x'],
      'Submarine': [0, 'x'],
      'Destroyer': [0, 'x'],
    }
    print('Player {} Created\n'.format(self.name))

  def display_all_ships(self):
    print('{}\'s Ship Choices:'.format(self.name))
    for i in self.ships:
      print(i+':', self.ships[i], ',')
    print()

  def display_active_ships(self):
    print('{}\'s Ships:'.format(self.name))
    anyprinted = False
    for i in self.ships:
      temp = self.ships[i][1]
      if temp == self.ACTIVE_SYMBOL:
        print('{} is at {}'.format(i, self.ships[i][0]))
        anyprinted = True
    
    if not anyprinted:
      print('No Active Ships to Show')
      print('Please initialize your ships!')
    print()
  
  def print_current_board(self):
    board = self.board
    print('Current Board: ')
    for i in range(len(board)):
      for j in board[i]:
        print(j, end=" ")
      print()

  def setBoat(self, type, start, end):
    board = self.board
    active = self.ACTIVE_SYMBOL
    types = {
      'Carrier': 5, 
      'Battleship': 4,
      'Cruiser': 3,
      'Submarine': 3,
      'Destroyer': 2,
    }

    distance = self.calc_distance(start,end)

    if distance != types[type]:
      print('Error: Ship size is invalid')
      print('{} must take up {} spaces'.format(type, types[type]))
      print('input takes up {}\n'.format(distance))
      return

    if self.ships[type][1] == active:
      print(type, self.ships[type])
      x = input('Ship already active, would you like to change location (y/n) ? ')
      if x != 'y':
        print('Aborting new ship save')
        return
      self.place_ship(self.ships[type][0][0], self.ships[type][0][1])

    if self.ships[type]:
      self.ships[type] = [[start, end], active]
    else:
      print('Error: invalid Ship Type')
      print('Please choose a ship listed below:')
      self.display_all_ships()
      return

    if start[0] > len(board):
      print('Error: index overflow')
      return

    self.place_ship(start, end, active)

    print('{} Created!\n'.format(type))

  def calc_distance(self, start, end):
    x1, y1 = start
    x2, y2 = end
    return (abs(y2 - y1) if x1 == x2 else abs(x1 - x2)) + 1

  def place_ship(self, start, end, symbol='.'):
    x1,y1 = start
    x2,y2 = end
    run = False
    board = self.board
    
    if x1 == x2:
      for i in range(len(board)):
        if x1 == i:  
          board[i][y1] = symbol
          for j in range(len(board[i])):
            if y2+1 > j and y1 < j:
              board[i][j] = symbol
    elif x1 < x2:
      '''
        vertical placement assumes y1 == y2,
        diagonals are not allowed
      '''
      for i in range(len(board)):
        if i == x1 or run:
          board[i][y1] = symbol
          run = True
          if i == x2:
            run = False
  def hit(self, x, y):
    print('Enemy is launching an attack!')
    self.board[x][y] = 'x'

# print_current_board(board_idx, 1)
# print('\n')
# print_current_board(board)

# setBoat(board, 'r', (3,2), (6,2))
# print_current_board(board)
x = Player('nolo', active_symbol='O')

x.print_current_board()
x.display_all_ships()
x.display_active_ships()

x.setBoat('Destroyer', (3,2), (4,2))
x.display_active_ships()
x.print_current_board()
x.setBoat('Destroyer', (5,5), (5,6))
x.setBoat('Carrier', (1,3), (1,7))
x.setBoat('Battleship', (3,3), (6,3))
x.setBoat('Cruiser', (7,4), (7,6))
x.setBoat('Submarine', (2,0), (2,2))
x.display_active_ships()
x.print_current_board()

x.hit(2,1)
x.print_current_board()