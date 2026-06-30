''' Program for ATM PIN Verification '''
#input of number from the user
num = int(input("Enter any number : "))

# Given pin to verify
pin = 4589

while(num != pin):
    print("Incorrect PIN ")
    num = int(input("Enter Your pin number Again: "))



print("Access Granted ")

