# CIS 41A
# Simon Zhang
# 06/18/2020

# Create Fibonacci numbers (1, 1, 2, 3, 5, 8, etc.)
# using an iterator and a generator (Both).


def fib():
    """unbounded generator, creates Fibonacci sequence"""
    x = 0
    y = 1
    while True:
        x, y = y, x + y
        yield x


if __name__ == "__main__":
    g = fib()
    for i in range(9):
        print(next(g))

"""
1
1
2
3
5
8
13
21
34
"""