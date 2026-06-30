
#User Input for compound interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Calculate the final amount
amount = principal * (1 + rate / (100 * n)) ** (n * time)

# Calculate compound interest
compound_interest = amount - principal

print(f"\nFinal Amount = {amount:.2f}")
print(f"Compound Interest = {compound_interest:.2f}")



'''-----------------------------------output----------------------------------
Enter the principal amount: 20000
Enter the annual interest rate (%): 10.25
Enter the time (in years): 4
Enter the number of times interest is compounded per year: 4

Final Amount = 29981.10
Compound Interest = 9981.10
-------------------------------------------------------------------------------
'''