#!/usr/bin/python3
"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

Get all values in runtime
"""

# Inputs
P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 0.05 for 5%): "))
t = float(input("Enter the time (t) in years: "))

# Simple Interest
A_simple = P * (1 + r * t)
print("Simple Interest Final Amount (A): %.2f" % A_simple)

# Number of times interest is compounded per year for compound interest
n = int(input("Enter the number of times the interest is compounded per year (n): "))

# Compound Interest
A_compound = P * (1 + r / n) ** (n * t)
print("Compound Interest Final Amount (A): %.2f" % A_compound)