# interchange first and last elements in a list

lst = [1, 2, 3, 5, 7, 8]
temp = lst[len(lst)-1]
lst[len(lst)-1] = lst[0]
lst[0] = temp
print(lst)
