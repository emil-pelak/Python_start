my_tuple = (1,1,3,4,5,6,7,8,9,10)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:3])
print(my_tuple[0:3])
print(my_tuple[0:10:2])
print(my_tuple[::-1])

for i in my_tuple:
    print(i)

print(my_tuple.count(1))
print(2 in my_tuple)
print(my_tuple.index(1))