def get_remainder(a, n):
    if n%2 == 0:
        return 2
    else:
        return (2*a*n)%(a*a)

def get_max_remainder(a):
    return max(get_remainder(a, 2*n+1) for n in range(1, a+1))

print(sum(get_max_remainder(a) for a in range(3, 1001)))