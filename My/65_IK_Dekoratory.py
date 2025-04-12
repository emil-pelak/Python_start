def my_decorator(fn):
    def wrapper():
        print("Before the function call")
        fn()
        print("After the function call")
    return wrapper

@my_decorator
def get_5_values():
    for v in range(1,6):
        print(v)

get_5_values()

# my_decorator(get_5_values)()