# What is the output of this code?
try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

# Result:
# Divided by zero
