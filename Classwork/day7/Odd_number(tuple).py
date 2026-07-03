#Create a blank list 
number=[]
print("Enter 15 numbers:")
for i in range(15):
    num=int(input())
    number.append(num)
#Change it to tuple 
tuple1=tuple(number)
print("Tuple is:",tuple1)
#--------------------------
print("------------------------")
#Accessing each element of tuple
print("Odd numbers are:")
for i in tuple1:
    #Condition for odd number
    if i%2!=0:
        print(i,end=",")

