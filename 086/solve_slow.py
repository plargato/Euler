TARGET = 1000000
is_square_buffer = [True]
square_size = 0

def expand_squares():
    global is_square_buffer, square_size
    start = square_size * square_size + 1
    square_size += 1
    end = square_size * square_size

    for _ in range(start, end):
        is_square_buffer.append(False)
    
    is_square_buffer.append(True)

def is_square(n):
    global is_square_buffer
    while n >= len(is_square_buffer):
        expand_squares()
    return is_square_buffer[n]

valid_cubes = 0
c = 0
while valid_cubes < TARGET:
    expand_squares()
    c += 1
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if is_square(a*a + b*b + c*c + 2*a*b):
                valid_cubes += 1

print(c)
    
