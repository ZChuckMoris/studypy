# To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# Just like passing no arguments, negative values will return the entire contents.
