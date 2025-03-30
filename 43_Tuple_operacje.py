my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
my_tuple = tuple(my_list)
print(my_tuple)

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = my_tuple
print(a)

my_list[0] = 100
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = my_tuple
print(a)

