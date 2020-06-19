def shortest_string(x, y):
    if str(len(x)) <= str(len(y)):
        return x
    else:
        return y

print(shortest_string("Hello, World!", "Hello, great new world!"))
