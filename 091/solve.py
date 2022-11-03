from time import perf_counter
from math import gcd

GRID_SIZE = 50
start_time = perf_counter()

def get_diagonal_vector(v):
    return -v[1], v[0]

def minify_vector(v):
    if v[0] == 0:
        return 0, 1
    elif v[1] == 0:
        return 1, 0
    d = gcd(v[0], v[1])
    return v[0] // d, v[1] // d

def get_triangles_at(v):
    if v == (0,0):
        return GRID_SIZE * GRID_SIZE
    def count_steps(source, step):
        def r(loc, s):
            if s > 0:
                return (GRID_SIZE - loc) // s
            elif s < 0:
                return loc // -s
            else: 
                return GRID_SIZE * 2

        sx = r(source[0], step[0])
        sy = r(source[1], step[1])
        return min(sx, sy)
    d = get_diagonal_vector(v)
    step = minify_vector(d)
    return count_steps(v, step) + count_steps(v, (-step[0], -step[1]))
grid = [[0] * (GRID_SIZE+1) for _ in range(GRID_SIZE + 1)]

for y in range(0, GRID_SIZE + 1):
    for x in range(0, GRID_SIZE + 1):
        grid[y][x] = get_triangles_at((x, y))

end_time = perf_counter()
delta = end_time - start_time
print(f'Solution: {sum([sum(r) for r in grid])}')
print(f'Time: {delta:0.4f}s')