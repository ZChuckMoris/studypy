# The contents of a file that has been opened in text mode can be read using the read method.
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

# This will print all of the contents of the file "filename.txt".
