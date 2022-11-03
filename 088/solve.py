from time import perf_counter
from queue import PriorityQueue
from functools import reduce

MAX_K = 12000
start_time = perf_counter()

def get_queue_pair(factors):
    return reduce(lambda a, b: a*b, factors, 1), factors
def get_children_groups(factors):
    children = []
    for i, v in enumerate(factors):
        if v != 2:
            if i + 1 == len(factors) or factors[i] < factors[i+1]:
                children.append([v2+1 if i2 == i else v2 for i2, v2 in enumerate(factors)])
            if i > 0:
                children.append([v2+1 if i2 == i-1 else v2 for i2, v2 in enumerate(factors)])
            return children
    l = len(factors)
    children.append([v2+1 if i2 == l-1 else v2 for i2, v2 in enumerate(factors)])
    children.append(factors + [2])
    return children

q = PriorityQueue()
q.put(get_queue_pair([2,2]))
min_groups = [0] * (MAX_K + 1)
unknowns = MAX_K - 1
while not q.empty() and unknowns > 0: 
    v, factors = q.get()
    s = sum(factors)
    size = v - s + len(factors)
    if size <= MAX_K and min_groups[size] == 0:
        min_groups[size] = v
        unknowns -= 1
    children = get_children_groups(factors)
    for child in children:
        q.put(get_queue_pair(child))

min_values = set(min_groups)
end_time = perf_counter()
delta = end_time - start_time
print(f'Solution: {sum(min_values)}')
print(f'Time: {delta:0.4f}s')