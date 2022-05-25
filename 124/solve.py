from time import time

N = 100000
rad = [1] * (N+1)

for n in range(1, N+1):
    if rad[n] == 1:
        for i in range(n, N+1, n):
            rad[i] *= n

rad[0]= 0
# print(rad[504])
E = list(range(0, N+1))
E.sort(key=lambda a: rad[a])

print(E[10000])
start_time = time()

end_time = time()

print(f'time elapsed {end_time - start_time}')