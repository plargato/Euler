from itertools import product
import numpy as np

# states
# node_edge_fn: (out_s) -> Dict[in_s, p]
dbl_chance = 1/4
dbl_dist = [
  (2, 1/16),
  (4, 1/16),
  (6, 1/16),
  (8, 1/16),
]

cube_dist = [
  (3, 2/16),
  (4, 2/16),
  (5, 4/16),
  (6, 2/16),
  (7, 2/16),
]
def build_transition(states, node_edge_fn):
  n = len(states)
  trans = np.zeros(shape=(n,n))
  
  for (out_i, out_s) in enumerate(states):
    edge_dict = node_edge_fn(out_s)
    for (in_i, in_s) in enumerate(states):
      trans[in_i][out_i] = edge_dict[in_s] if in_s in edge_dict else 0

  return trans

def read_monopol_input():
  with open('input.txt', 'r') as file:
    dataRaw = file.read()
    data = dataRaw.split('\n')
    return data
  raise Exception('cant read input')

def get_monopol_board_dist():
  board = read_monopol_input()
  board_s = len(board)
  states = list(product(range(board_s), range(3)))

  JAIL = board.index('JAIL')
  GO = board.index('GO')
  C1 = board.index('C1')
  E3 = board.index('E3')
  H2 = board.index('H2')
  R1 = board.index('R1')
  U1 = board.index('U1')

  def next_railway(i):
      for v in range(i, board_s):
        if board[v].startswith('R'):
          return v
      return R1

  def next_utility(i):
    for v in range(i, board_s):
      if board[v].startswith('U'):
        return v
    return U1

  def node_edge(out_s):
    (out_i, out_dbl) = out_s

    edges = {}

    def edge_chance(s, p):
      if s in edges:
        edges[s] += p
      else:
        edges[s] = p

    def add_edges_by_land(land_s, land_p):
      def land_chance(s, p):
        edge_chance(s, p*land_p)
      
      land_i, land_dbl = land_s

      land_name = board[land_i]
      if land_name == 'G2J':
        land_chance((JAIL, 0), 1)
      elif land_name.startswith('CC'):
        land_chance((land_i, land_dbl), 14/16)
        land_chance((GO, land_dbl), 1/16)
        land_chance((JAIL, 0), 1/16)
      elif land_name.startswith('CH'):
        land_chance((land_i, land_dbl), 6/16)
        land_chance((GO, land_dbl), 1/16)
        land_chance((JAIL, 0), 1/16)
        land_chance((C1, land_dbl), 1/16)
        land_chance((E3, land_dbl), 1/16)
        land_chance((H2, land_dbl), 1/16)
        land_chance((R1, land_dbl), 1/16)
        land_chance((next_railway(land_i), land_dbl), 2/16)
        land_chance((next_utility(land_i), land_dbl), 1/16)
        land_chance((land_i - 3, land_dbl), 1/16)
      else:
        land_chance((land_i, land_dbl), 1)

    if out_dbl == 2:
      edge_chance((JAIL, 0), dbl_chance)
    else:
      for rv, rp in dbl_dist:
        add_edges_by_land(((out_i+rv)%board_s, out_dbl+1), rp)
    
    for rv, rp in cube_dist:
      add_edges_by_land(((out_i+rv)%board_s, 0), rp)

    return edges

  vec = np.zeros(shape=(len(states),1))
  vec[states.index((0, 0))] = 1
  trans = build_transition(states, node_edge)
  state_dist = np.linalg.matrix_power(trans, 100000000) @ vec
  board_dist = [0] * board_s
  for state_i, (board_i, _) in enumerate(states):
    board_dist[board_i] += state_dist[state_i][0]
  return board_dist

board_dist = get_monopol_board_dist()
mi1,mx1 = max(enumerate(board_dist), key=lambda tpl: tpl[1])
mi2,mx2 = max(((i,k) for i,k in enumerate(board_dist) if i not in (mi1,)), key=lambda tpl: tpl[1])
mi3,mx3 = max(((i,k) for i,k in enumerate(board_dist) if i not in (mi1,mi2)), key=lambda tpl: tpl[1])
mxs = [(mi1, mx1), (mi2, mx2), (mi3, mx3)]
sol = ''
for mi, mx in mxs:
  sol += str(mi).ljust(2, '0')
print(sol)