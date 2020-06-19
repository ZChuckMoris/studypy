# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

# This ensures that the file is always closed, even if an error occurs.
