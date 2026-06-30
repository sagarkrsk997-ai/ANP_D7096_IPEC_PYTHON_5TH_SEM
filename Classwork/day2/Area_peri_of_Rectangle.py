'''Calculating Area and Radius of Rectangle'''


#input of length from the  user
length = float(input("Enter the length (in meters): "))
#checking whether  user's input is valid or not
if(length<=0):
    exit("Length cannot be zero or negative")

#input of breadth from the  user
breadth = float(input("Enter the Breadth (in meters): "))

#checking whether  user's input is valid or not
if(breadth<=0):
    exit("Breadth cannot be zero or negative")




#displaying Area of rectangle
print("Area of the reactangle = ",length*breadth)



#displaying Perimeter of rectangle
print("Perimeter of the reactangle = " , 2*(length + breadth))


''' Output
Enter the length (in meters): 2
Enter the Breadth (in meters): 3
Area of the reactangle =  6.0
Perimeter of the reactangle =  10.0'''


