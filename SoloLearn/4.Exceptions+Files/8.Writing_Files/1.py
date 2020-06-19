# To write to files you use the write method, which writes a string to the file.
# For example:
file = open("newfile.txt", "w")
file.write("This has been written to a file\n")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

# Result:
"""
This has been written to a file
"""
# The "w" mode will create a file, if it does not already exist.
