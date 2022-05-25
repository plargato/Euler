
n = 6

dct = {}
mn = n - 2

def ways(score, mn):

    fins = 0

    if score % 2 == 0 and ((2 <= score <= 40) or score == 50):
        fins += 1

    wys = fins
    for i in range(mn, 0, -1):
        factor = 1
        if i % 2 == 0:
            factor += 1
        if i % 3 == 0:
            factor += 1

        n_score = score-i
        sub_ways = factor*ways(n_score, min(i, n_score)) 
        if score == 6:
            print(f'ways({n_score}, min({i}, {n_score}))={sub_ways}')
        wys += sub_ways
    return wys

print(ways(6, 6))
