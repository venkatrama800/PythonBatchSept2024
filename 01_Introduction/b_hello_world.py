#!/usr/bin/python3

"""
Purpose: Basic PEP-8 guidelines and 
         shebang line
   PEP - Python Enhancement proposal
   PEP 8 - coding style guide

   https://peps.python.org/pep-0008/
    
"""
# print as a statement in python2
# print "Hello world!"

# print as a function in python 2 & 3
print("Hello world!")
print(True)
print(True,123,None)

def wishes(name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("Venkatrama")

# python 3 supports UTF-8