#!/usr/bin/python3
"""
Assignment
-----------
1) WAP to display the multiplication table from 10 to 1, for the first 10 tables
1 * 10 = 10
1 * 9  =  9
"""
for num in range(1, 11):  # From 1 to 10
    print(f"Multiplication table for {num}:")
    for i in range(10, 0, -1):  # From 10 down to 1
        print(f"{num} x {i} = {num * i}")
    print()