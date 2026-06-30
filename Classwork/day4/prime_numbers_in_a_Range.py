''' Count Prime Numbers in a Range '''

# input of numbers from user

num1 = int(input("Enter your starting number: "))
num2 = int(input("Enter your ending number: "))

count = 0

if(num1 < num2):

    for i in range(num1, num2 + 1):

        if(i > 1):          # Prime numbers start from 2

            flag = True     # Assume number is prime

            for j in range(2, i):

                if(i % j == 0):
                    flag = False
                    break

            if(flag):
                count = count + 1
                print(i, end=" ")

elif(num1 > num2):
    print("Please enter range in increasing way")

elif(num1 == num2):
    print("Both numbers are same")

else:
    print("Please enter valid number")

print("\nTotal number of prime numbers :", count)