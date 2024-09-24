#!/usr/bin/python3
"""
Purpose: Importance of Indentation
"""

print("hello world1!")

#  print("hello world2!")  # IndentationError: unexpected indent
print("hello world3!")


# block code - if, else, elif, for, while, def , class, ...
# if 12 > 3:
# print('12 is greater than 3')

# IndentationError: expected an indented block after 'if' statement on line 13


if 12 > 3:
    print('12 is greater than 3')


if 12 > 34:
    print("greater")
else:
    print("It is lesser")



if 1 < 2:
    print("case 1")
elif 2 > 1:
    print("case 2")
else:
    print("case 3")



if 1 < 2:
    if 2 < 3:
        if 3 < 4:
            if 4 < 5:
                print("LESSER")
            else:
                print("something")
        else:
            print("something")
    else:
        print("something")


# tabs vs white-space
# PEP 8 (Python Enhancement Proposal) - code style guide
# Prefer white-spaces, to tabs; four white-spaces