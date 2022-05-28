from board import Board
from itertools import product

def get_monopol_board(cube_size=6):
  with open('input.txt', 'r') as file:
    dataRaw = file.read()
    data = dataRaw.split('\n')

    JAIL = data.index('JAIL')
    GO = data.index('GO')
    C1 = data.index('C1')
    E3 = data.index('E3')
    H2 = data.index('H2')
    R1 = data.index('R1')
    U1 = data.index('U1')

    def next_railway(i):
      for v in range(i, len(data)):
        if data[v].startswith('R'):
          return v
      return R1

    def next_utility(i):
      for v in range(i, len(data)):
        if data[v].startswith('U'):
          return v
      return U1

    def roll_iter():
      return product(range(1,cube_size+1), range(1, 3))
      
    def init_dist_fn(i):
      if i in (GO, JAIL):
        return [((0, 0), 1 if i == GO else 0)] + [((rv, rc), 0) for rv, rc in roll_iter()]
      return [((rv, rc), 0) for rv, rc in roll_iter()]

    def land_rules_fn(i):
      triple_rule = [((i, (True, 0, 0)), [(0, (0, 0), 1)])]
      if data[i].startswith('G2J'):
        return [((i, (False, rv, rc)), [(JAIL, (0, 0), 1)]) for rv, rc in roll_iter()] + \
          triple_rule
      elif data[i].startswith('CC'):
        return [((i, (False, rv, rc)), [ \
          (i, (rv, rc), 14/16), \
          (JAIL, (0, 0), 1/16), \
          (GO, (rv, rc), 1/16)]) \
          for rv, rc in roll_iter()] + \
          triple_rule
      elif data[i].startswith('CH'):
        return [((i, (False, rv, rc)), [ \
          (i, (rv, rc), 6/16), \
          (GO, (rv, rc), 1/16), \
          (JAIL, (0, 0), 1/16), \
          (C1, (rv, rc), 1/16), \
          (E3, (rv, rc), 1/16), \
          (H2, (rv, rc), 1/16), \
          (R1, (rv, rc), 1/16), \
          (next_railway(i), (rv, rc), 2/16), \
          (next_utility(i), (rv, rc), 1/16), \
          (i-3, (rv, rc), 1/16)]) \
          for rv, rc in roll_iter()] + \
          triple_rule
      return [((i, (False, rv, rc)), [(i, (rv, rc), 1)]) for rv, rc in roll_iter()] + \
          triple_rule

    def state_reducer(index, state, roll):
      (rv, rc) = state
      if rv == roll:
        if rc == 2:
          return (True, 0, 0)
        return (False, roll, rc+1)
      return (False, roll, 1)
    return Board(len(data), cube_size, init_dist_fn, land_rules_fn, state_reducer)

