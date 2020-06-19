# There is another kind of import that can be used if you only need certain functions from a module.
# These take the form from module_name import var, and then var can be used as if it were defined normally in your code.
# For example, to import only the pi constant from the math module:

# Use a comma separated list to import multiple objects. For example:
#from math import pi, sqrt

# * imports all objects from a module. For example: from math import *
# This is generally discouraged, as it confuses variables in your code with variables in the external module.

from math import pi

print(pi)

