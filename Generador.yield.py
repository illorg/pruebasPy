stop = False

def get_squares(n): # classic function approach
    return [x ** 2 for x in range(n)]
print(get_squares(10))

def get_squares_gen(n): # generator approach
    for x in range(n):
        yield x ** 2 # we yield, we don't return

def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1

print(list(get_squares_gen(10)))

c = counter()
print(next(c))
print(next(c))

print(next(c))
stop = True