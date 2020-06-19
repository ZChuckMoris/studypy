# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

# Result:
# Error occurred
