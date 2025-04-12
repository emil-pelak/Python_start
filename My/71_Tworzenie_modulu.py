import my_module

msg = my_module.my_function('Emil')

print(msg)
print(my_module.x)

from my_module import my_function
from my_module import x
msg = my_function('Emil')
print(msg)
print(x)      