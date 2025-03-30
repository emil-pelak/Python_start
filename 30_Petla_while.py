number = int(input("Enter a number: "))
# counter = 0
while(number>0):
    # print("Hello World!")
    # if counter == 5:
    #     break   

    # if number %2 == 0:
    #     print("Liczba parzysta to: {}".format(number))
    # number -= 1
    number -= 1
    if number % 2 != 0:
        continue
    print(number)
    # number -= 1
    