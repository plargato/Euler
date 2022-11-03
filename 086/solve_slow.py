import time
from is_square import is_square

start_time = time.perf_counter()

TARGET = 2000


valid_cubes = 0
c = 0
while valid_cubes < TARGET and c < 10:
    c += 1
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if is_square(a*a + b*b + c*c + 2*a*b):
                print(f'{a} {b} {c}')
                valid_cubes += 1
    print(f'{c}: {valid_cubes}')
end_time = time.perf_counter()

print(f'Solution: {c}')
print(f'Took {(end_time-start_time):0.4f}s')