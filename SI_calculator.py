# Simple Interest Calculator in Python

# Get user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (in %): "))
time = float(input("Enter the time in years: "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"Simple Interest is: {simple_interest:.2f}")
