from time import perf_counter
from math import sqrt, floor

TARGET = 1000000

start_time = perf_counter()

c = 0
cube_count = 0

while cube_count < TARGET:
    c += 1
    max_n = floor(sqrt(5*c*c))
    for n in range(c+1, max_n + 1):
        r_squared = (n+c)*(n-c)
        r = sqrt(r_squared)
        if r.is_integer():
            cube_count += min(r-1, c) - (r+1) // 2 + 1
            
end_time = perf_counter()
delta = end_time - start_time
print(f'Solution {c}')
print(f'Took {delta:0.4f}s')