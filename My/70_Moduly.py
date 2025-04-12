import sys
from random import randint

print(dir(sys))
print(sys.version)
print(sys.platform)

print(dir(randint))
print(randint(1, 10))

my_list = [v for v in range(randint(1, 10))]
print(my_list)