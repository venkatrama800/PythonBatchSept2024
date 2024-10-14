#!/usr/bin/python3

i = 1
while i <= 10:  
    j = 1
    while j <= 10:  
        product = j * i
        output = f"{str(j).zfill(2)} * {str(i).zfill(2)} = {str(product).zfill(3)}"
        print(output, end="  ")
        j += 1  
    print() 
    i += 1 