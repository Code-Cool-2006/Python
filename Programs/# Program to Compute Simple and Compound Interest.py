# Program to Compute Simple Interest and Compound Interest

# Input: Principal, Rate of Interest, and Time
print("Enter Principal Amount: ")
principal = float(input())
print("Enter Rate of Interest: ")
rate = float(input())
print("Enter Time in years: ")
time = float(input())

# Validate the inputs
if principal <= 0 or rate < 0 or time <= 0:
    print("Enter Valid Inputs")
    exit()
else:
    # Calculate Simple Interest
    simple_interest = (principal * rate * time) / 100
    
    # Calculate Compound Interest
    amount = principal * (1 + rate / 100) ** time  # Total amount with Compound Interest
    compound_interest = amount - principal
    
    # Output Results
    print("Principal Amount is:", principal)
    print("Rate of Interest is:", rate)
    print("Time in years is:", time)
    print("Simple Interest is:", simple_interest)
    print("Compound Interest is:", compound_interest)
    print("Total Amount with Simple Interest is:", principal + simple_interest)
    print("Total Amount with Compound Interest is:", principal + compound_interest)
