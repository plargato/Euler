import numpy as np
from itertools import product
from transition_builder import build_transition

def node_edge(out_s):
  if out_s == 1:
    return dict((i+1, 0.25) for i in range(4))
  return dict((i%4+1, 1 if i == out_s else 0) for i in range(1, 5))

trans = build_transition(list(range(1, 5)), node_edge)
print(trans)

vec = np.zeros(shape=(4,1))
vec[1][0] = 1


print(np.linalg.matrix_power(trans, 10000) @ vec)