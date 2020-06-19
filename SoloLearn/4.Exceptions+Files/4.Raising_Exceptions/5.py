# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
# For example:
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise

# Result:
"""
An error occurred
ZeroDivisionError: division by zero
"""
