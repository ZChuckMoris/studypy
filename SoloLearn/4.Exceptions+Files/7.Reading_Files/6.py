# To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
# For example:
file = open("filename.txt", "r")
print(file.readlines())
file.close()

# Result:
"""
['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
"""

# You can also use a for loop to iterate through the lines in the file:
"""
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()
"""

# Result:
"""
Line 1 text

Line 2 text

Line 3 text
"""

# In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.

# to print without new lines you can specify end == '' as argument for print.
"""
file = open("filename.txt", "r")

for line in file:
    print(line, end = '')

file.close()
"""
