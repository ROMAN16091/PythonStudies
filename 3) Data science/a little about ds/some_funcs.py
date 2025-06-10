from itertools import zip_longest
list1 = [1,2,3]
list2 = ['a', 'b']

result = zip(list1, list2)
print(list(result))
result2 = zip_longest(list1, list2, fillvalue='N/A')
print(list(result2))

nums = [1,2,3,4,5]
print(sorted(nums, reverse=False))
print(sorted(nums, reverse=True))

list3 = ['apple', 'banana']
print(list(enumerate(list3)))
for i, v in enumerate(list3):
    print(i,v)

from functools import reduce
list4 = list(range(1, 11))
print(list4)
result = filter(lambda x: x % 2 == 0, list4)
print(list(result))
result2 = map(lambda x: x**2, result)
print(list(result2))
result3 = reduce(lambda x, y: x + y, list4)
print(result3)


from itertools import combinations, permutations

items = ['a','b','c', 'd']
print(list(combinations(items, 3)))
print(list(permutations(items, 3)))


from functools import lru_cache

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))