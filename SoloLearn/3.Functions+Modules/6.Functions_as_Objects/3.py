# Functions can also be used as arguments of other functions.

def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))
  # (5+10 + 5+10)
a = 5
b = 10

print(do_twice(add, a, b))

# Output = 30
