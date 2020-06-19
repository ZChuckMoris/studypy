# Fill in the blanks to raise a ValueError exception, if the input is negative.

num = input(":")
if float(num) < 0:
    raise ValueError("Negative!")
