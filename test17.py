g = (x * x for x in range(11))


for n in g:
    print(n)

print('\n')

def fib():
    print('s 1')
    yield 1
    print('s 2')
    yield 2
    print('s 3')
    yield 3

f = fib()
print(next(f))
print(next(f))
print(next(f))

for n in f:
    print(n)


#1,1,2,3,5,8,13,21,34,55,89....
#next yield

def fib(max = 10):
    n,a,b = 0,0,1
    fib_list = [a,b]
    while n < max:
        c = a + b
        a = b
        b = c
        fib_list.append(c)

        n += 1

    return fib_list


def fib(max = 10):
    n,a,b = 0,0,1
    while n < max:
        c = a + b
        a = b
        b = c
        yield c
        n += 1

f = fib()

print(next(f))
print(next(f))
print(next(f))
print(next(f))