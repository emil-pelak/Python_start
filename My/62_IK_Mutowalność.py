a = 1
print(id(a))

a += 1
print(id(a))

my_list  = [1, 2, 3]
my_tuple = (1, 2, 3, my_list)
print(my_tuple)

my_tuple[3].append(4)
print(my_tuple)