# Ask for user input
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F.")

# Ask for user input
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Display the result
print(f"{fahrenheit}°F is equal to {celsius}°C.")