# You can import a module or object under a different name using the as keyword. This is mainly used when a module or object has a long or confusing name.
# For example:

#from math import sqrt as square_root
#print(square_root(102))

# Result: 10

# My variation of code:
from math import sqrt as math_sqrt
i = float(input("Enter any number you wish to get sqaure root from: \n"))
if i % 1 == 0:
    result = math_sqrt(int(i))
else:
    result = math_sqrt(i)
if result % 1 == 0:
    result = int(result)
print(result)


