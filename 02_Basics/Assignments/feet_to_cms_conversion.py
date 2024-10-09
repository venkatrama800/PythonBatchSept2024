#!/usr/bin/python3
"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""

feet = float(input("Enter the value in feet: "))
inches = feet * 12  # 1 foot = 12 inches
centimeters = inches * 2.54  # 1 inch = 2.54 centimeters

print("Value in feet: ", feet)
print("Value in inches: %.2f" % inches)
print("Value in centimeters: %.2f" % centimeters)