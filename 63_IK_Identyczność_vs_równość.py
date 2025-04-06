a = 1
b = 1

print(a == b)
print(a is b)

c = [1, 2, 3]
d = [1, 2, 3]

print(c == d)
print(c is d)

print(id(a), id(b))
print(id(c), id(d))

print('\n')

c = d

print(id(c), id(d))