def my_decorator(fn):
    def wrapper():
        print("Before the function call")
        fn()
        print("After the function call")
    return wrapper

@my_decorator
def get_5_values():
    my_list = [v for v in range(1, 10)]
    print(my_list)

get_5_values()

print("===" * 10)
# Using the decorator without @ syntax
my_decorator(get_5_values)()