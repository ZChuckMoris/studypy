# What is the highest number that would be printed by this code?
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)

# Result: 3
