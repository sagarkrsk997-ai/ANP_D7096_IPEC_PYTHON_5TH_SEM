#Creating a blank list
number=[]
print("Enter 20 number:")
for i in range(5):
    a=int(input())
    number.append(a)
print("List is:",number)
#-----------------------
print("------------------")
#Take input of a number given by a user 
ele=int(input("Enter any number:"))
c=number.count(ele)
if c>1:
    number.reverse()
    for i in range(c-1):
        number.remove(ele)
elif(c==0):
    print("Number is not present ")

                   
else:
    print("Number is not present more than 1 time ")

number.reverse()     
print("Updated list is:",number)