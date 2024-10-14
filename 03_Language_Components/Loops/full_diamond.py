#!/usr/bin/python3
# full diamond
"""
Assignment:full diamond problem
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
 *************
  ***********
    *******
     *****
      ***
       *

       using both for loop and while loop seperately
"""

num = 0
while num < 10:
    print((9 - num) * ' ' + (2 * num + 1) * '*')
    num += 1
num = 8
while num >= 0:
    print((9 - num) * ' ' + (2 * num + 1) * '*')
    num -= 1