# An except statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
# For example:
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")
