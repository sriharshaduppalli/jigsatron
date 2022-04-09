# to swap two elements in a list

lst = [1, 3, 5, 6, 7]


def swap(i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst


print('Enter 1st element to swap')
x = input()
print('Enter 2nd element to swap')
y = input()
print('before swap', lst)
swap(int(x), int(y))
print('after swap', lst)
