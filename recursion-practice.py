import pdb

def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for x in range(1000):
    print(f'{x}: {fib(x)}')
