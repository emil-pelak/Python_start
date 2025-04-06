a = set([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
b = set([5, 5, 6, 6, 7, 7, 8, 8, 9, 9])

print(a)
print(b)

print(a.intersection(b))

print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))