# maximum of two numbers

# x = input()
# y = input()

a = -5
b = -3


def max_of(x, y):
    if x > y:
        print('x is max', x)
    elif x < y:
        print('y is max', y)
    else:
        print('both are equal')


max_of(a, b)
