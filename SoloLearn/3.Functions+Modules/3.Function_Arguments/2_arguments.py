def print_sum_twice(x, y):
    print(type(x))
    print(type(y))
    if type(x) == int:
        if type(y) == int:
            print(x + y)
            print(x + y)
        else:
            print(str(y) + " is not integer")
            print(type(y))
    elif type(x) != int:
        print(str(x) + " is not integer")
        print(type(x))

print_sum_twice(5, 8)
