def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    return a//b

try:
    r = divide (4,0)
    print(r)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")