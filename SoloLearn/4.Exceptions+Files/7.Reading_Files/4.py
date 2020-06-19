# After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

# Result:
"""
Re-reading

Finished
"""

# Just like passing no arguments, negative values will return the entire contents.
