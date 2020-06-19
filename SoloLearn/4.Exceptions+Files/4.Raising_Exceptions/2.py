# Which errors occur during the execution of this code?
try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError

# Result:
# ZeroDivisionError and ValueError
