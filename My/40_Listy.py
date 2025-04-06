# my_list = [1,2,3,4,5, 'Emil']
# print(my_list)
# my_list[4] = 'coś'

# print(my_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
# for i in my_list:
#     print(i)
    

my_list.append(11)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

# print(my_list[::-1])
# print(my_list[0:3])

my_list_2 = [10,20,30,40,50]
my_list_3 = [11,22,33,44,55]
my_list_4 = my_list + my_list_2 + my_list_3
my_list.sort()
print(my_list_4)

print(len(my_list_4))
print(33 not in my_list_4)

print(type(my_list_4))