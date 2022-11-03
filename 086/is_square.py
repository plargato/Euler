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