import re
from soduko import SodukoBoard
from itertools import product

def parse_board(board_str):
  board_arr = board_str.split('\n')
  board = SodukoBoard()
  for x,y in product(range(9), range(9)):
    if board_arr[y][x] != '0':
      board.place(ord(board_arr[y][x])-ord('0'), x, y)
  return board

def solve(board: SodukoBoard):
  tpl = board.best_slot()
  while tpl is not None:
    ops_c, x, y = tpl
    if ops_c > 1:
      ops = board.options(x, y)
      for opt in ops:
        b = board.clone()
        b.place(opt, x, y)
        if b.is_dead_end():
          continue
        try:
          rb = solve(b)
          return rb
        except AttributeError as e:
          pass
      raise AttributeError()
    ops = board.options(x, y)
    board.place(ops[0], x, y)
    tpl = board.best_slot()
  
  if any(None in c for c in board.values):
    raise AttributeError()
  return board
  
with open('./input.txt', 'r') as file:
  data = file.read()
  strings = [s for s in re.split('\n?Grid.*\n', data) if s != '']
  s = 0
  for c, st in enumerate(strings):
    s += solve(parse_board(st)).value()
    print(f'{c+1}/50')
  print(s)