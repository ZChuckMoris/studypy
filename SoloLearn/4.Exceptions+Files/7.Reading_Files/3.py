# How many characters would be in each line printed by this code, if one character is one byte?
file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()

# Result: 4
