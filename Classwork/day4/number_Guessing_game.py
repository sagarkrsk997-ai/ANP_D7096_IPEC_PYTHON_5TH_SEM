'''Number Guessing Game'''

#input of number from user
num = int(input("guess the number: "))


secret_number = 37

# using loop to validate condition
while(num != secret_number):
    #    if number is greater
       if(num > secret_number):
           print("Too high")
           num = int(input("guess the number: "))

       
    #    if number is smaller
       elif(num < secret_number):       
           print("Too low")    
           num = int(input("guess the number: "))


print("Correct")       
