# When a file is opened in write mode, the file's existing content is deleted.
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text\n")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

# Result:
"""
Reading initial contents
some initial text
Finished
Reading new contents
Some new text
Finished
"""
