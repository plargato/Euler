from itertools import combinations
from collections import defaultdict

def init_squares(max_len):
  squares = defaultdict(lambda: set())

  i = 1
  while len(str(i*i)) <= max_len:
    squares[len(str(i*i))].add(str(i*i))
    i += 1
  return squares

def get_square_max(w1, w2, squares: dict[int, set[str]]):
  if len(w1) != len(w2):
    return 0
  sqs = squares[len(w1)]
  mx = 0
  for sq in sqs:
    mp = {}
    failed = False
    vs = [False] * 10
    for i, c in enumerate(w1):
      if c not in mp:
        if vs[int(sq[i])]:
          failed = True
          break
        mp[c] = sq[i]
        vs[int(sq[i])] = True
      elif mp[c] != sq[i]:
        failed = True
        break
    if failed:
      continue
    sq2 = ''.join(mp[c] for c in w2)
    if sq2 not in sqs:
      continue
    mx = max(mx, max(int(sq), int(sq2)))
    
  return mx


with open('input.txt', 'r') as file:
  data = file.read()
  words = [w[1:-1] for w in data.split(',')]
  wrds = defaultdict(lambda: [])
  
  for word in words:
    s = ''.join(sorted(word))
    wrds[s].append(word)

  keys = sorted(wrds.keys(), key=len, reverse=True)
  max_len = len(keys[0])
  squares = init_squares(max_len)

  mx = 0
  for k in keys:
    for w1, w2 in combinations(wrds[k], 2):
      mx = max(mx, get_square_max(w1, w2, squares))
  print(mx)


  