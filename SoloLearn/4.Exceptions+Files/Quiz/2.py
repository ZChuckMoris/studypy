# Fill in the blanks to try to open and read from a file. Print an error message in case of exception.

try:
    with open("test.txt") as f:
        print(f.read())
except:
    print("Error!")
