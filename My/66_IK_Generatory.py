def number_generator(end):
    n = 1
    while n < end:
        yield n        
        n += 1

def string_generator(end):
    n = 1
    while n < end:
        yield 'Hello'
        n += 1
      

values = number_generator(100)
# print(next(values))

for v in values:
    print(v)

strings = string_generator(100)

for s in strings:
    print(s)