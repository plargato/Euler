from queue import PriorityQueue
from time import time

start_time = time()
target = 1000

def volume(a, b, c, n):
    if n < 0:
        return 0
    s = a*b*n+(a+b-1)*(n-1)*n+((n-1)*n*(2*n-1))//3
    return c*(a*b+2*n*(a+b+n-1)) + 2*s

def layer_value(a, b, c, n):
    return volume(a, b, c, n) - volume(a, b, c, n-1)

queue = PriorityQueue()
found = set()

last_value = 0
count = 0
queue.put((layer_value(1, 1, 1, 0), (1, 1, 1, 0)))

def add_node(a, b, c, n):
    tpl = (a,b,c,n)
    global queue, found
    if tpl not in found:
        found.add(tpl)
        queue.put((layer_value(a, b, c, n), tpl))

while not queue.empty():
    value, (a, b, c, n) = queue.get()
    if last_value != value:
        if count == target:
            print(f'C({last_value})={count}')
            break
        last_value = value
        count = 0
    
    if n > 0:
        count += 1

    if a < b:
        add_node(a+1, b, c, n)
    if b < c:
        add_node(a, b+1, c, n)
    add_node(a, b, c+1, n)
    add_node(a, b, c, n+1)

print(f'time {time()-start_time}')
