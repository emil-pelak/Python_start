my_dictionary = {
                'a': 1, 
                'b': True, 
                'c': False, 
                'd': 'Emil',
                'e': [1, 2, 3], 
                'f': (1, 2, 3),
                }

print(my_dictionary)
print(type(my_dictionary))
print(my_dictionary['a'])
print(my_dictionary['b'])
print(my_dictionary['c'])
print(my_dictionary['d'])
print(my_dictionary['e'])
print(my_dictionary['f'])

my_dictionary['g'] = 'Pelak'

print(my_dictionary)

my_dictionary['a'] = 'Modified'

print(my_dictionary)

del my_dictionary['a']
print(my_dictionary)

print(my_dictionary.keys())

my_dictionary.update({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
})

print(my_dictionary)


for key in my_dictionary:
    print(key)
    # print(my_dictionary[key])

print(my_dictionary.items())
print(my_dictionary.keys())
print(my_dictionary.values())
