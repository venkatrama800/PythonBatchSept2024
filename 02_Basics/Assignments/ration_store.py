#!/usr/bin/python3
"""
Purpose: Ration Store

    -----------------------------------------------
    item    cost        quantity        Amount
    -----------------------------------------------
    wheat   25/kg       30 kgs      25 * 30 = 750/-
    Rice    12/kg       50 kgs      12 * 50 = 600/-
                                -------------------
                                              1350/-
                                subsidy 20%   -270/-
                                --------------------
                                BillableAmount:1080/-
"""


wheat_price_kg = 25
rice_price_kg = 12
wheat_quantity_required = 30
rice_quantity_required = 50
subsidy_provided_percentage = 20

TotalWheatPrice = wheat_price_kg*wheat_quantity_required
print("Total Wheat Price: ",TotalWheatPrice)

TotalRicePrice=rice_price_kg*rice_quantity_required
print("Total Rice Price",TotalRicePrice)

BilledAmount=(TotalRicePrice+TotalWheatPrice)*\
    ((100-subsidy_provided_percentage)/100)

print("Billed Amount: ",BilledAmount)