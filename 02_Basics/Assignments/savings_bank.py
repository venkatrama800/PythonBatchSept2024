"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

#!/usr/bin/python3

# Create a variable 'balance'
balance = 0
print("Initial Balance:", balance)

# Initial Deposit
initial_deposit = 1500
balance += initial_deposit
print("After Initial Deposit of 1500: Balance =", balance)

# Salary Credited
salary = 3300
balance += salary
print("After Salary Credited of 3300: Balance =", balance)

# Online Purchase
online_purchase = 33.33
balance -= online_purchase
print("After Online Purchase of 33.33: Balance =", balance)

# House Rent
house_rent = 1500
balance -= house_rent
print("After House Rent Paid of 1500: Balance =", balance)

# balance
print("Final Balance:", balance)