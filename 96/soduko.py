from copy import deepcopy
from itertools import product

class SodukoBoard:
  def __init__(self):
    self.values = [[None] * 9 for _ in range(9)]
    self.is_allowed = [[[True] * 9 for _ in range(9)] for _ in range(9)]

  def place(self, digit, x, y):
    if not self.is_allowed[y][x][digit-1]:
      raise Exception('attempt to place invalid value')
    self.values[y][x] = digit
    digit -= 1
    for i in range(9):
      self.is_allowed[y][x][i] = False
      self.is_allowed[y][i][digit] = False
      self.is_allowed[i][x][digit] = False

      cy = (y // 3)*3 + i // 3
      cx = (x // 3)*3 + i % 3
      self.is_allowed[cy][cx][digit] = False

  def best_slot(self):
    triplets = [(sum(1 for i in range(9) if self.is_allowed[y][x][i]), x, y) for x, y in product(range(9), range(9))]
    if(all(trip[0] == 0 for trip in triplets)):
      return None
    return min((trip for trip in triplets if trip[0] > 0), key=lambda tpl: tpl[0])

  def options(self, x, y):
    return [d+1 for d in range(9) if self.is_allowed[y][x][d]]
    
  def clone(self):
    return deepcopy(self)

  def value(self):
    return 100*self.values[0][0] + 10*self.values[0][1] + self.values[0][2]

  def is_dead_end(self):
    return any(
      (self.values[y][x] is None and not any(self.is_allowed[y][x]))
      for x,y
      in product(range(9), range(9))
    )
  def __str__(self):
    filled = sum(sum(1 for v in c if v is not None) for c in self.values)
    board = ''
    for y in range(9):
      for x in range(9):
        board += str(self.values[y][x] or 0)
      board += '\n'
    return f'{filled}/81\n' + board