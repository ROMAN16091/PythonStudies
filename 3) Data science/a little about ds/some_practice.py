from itertools import chain

list1 = [1, 2, 3]
tuple1 = ('a', 'b', 'c')
combined = chain(list1, tuple1)
result = list(combined)
print(result)
list2 = list(tuple1)
print(list1 + list2)
