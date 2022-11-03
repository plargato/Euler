from itertools import combinations

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for v in range(0, n+1):
        if not is_prime[v]:
            continue
        for ml in range(2*v, n+1, v):
            is_prime[ml] = False
    
    return is_prime
def get_cubics(max_diff):
    cubics = [1]
    v = 2
    cubic = v * v * v
    while cubic - cubics[-1] <= max_diff:
        cubics.append(cubic)
        v += 1
        cubic = v * v * v
    return cubics

    
N = 1000000

is_prime = sieve(N)
c = 0
cubics = get_cubics(N)
for c1, c2 in combinations(cubics, 2):
    if c2 - c1 <= N:
        # print(f'checking {c1} {c2}')
        # print(is_prime[c2-c1])
        if is_prime[c2-c1]:
            c += 1
print(c)