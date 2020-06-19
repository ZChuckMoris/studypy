import random

# prints 5 times random numbers between 1 and 6
for i in range(5):
   value = random.randint(1, 6)
   print(value)
# alternatively you can use the code below
"""
for i in range(0,5,1):
   # here we use randrange from 1 to 7 (not from 1 to 6) because using randrange we never hit out max value (so we set max in this function to our desired max+1).
   value = random.randrange(1, 7, 1)
   print(value)
"""
