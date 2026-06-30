'''Calculate Area of Circle'''


#Taking Radius input from the user
radius = float(input("Enter the Radius of a Circle (in meters):"))
pie = 3.14 #universal value of pie is 3.14 

#Validing the Radius whether it is valid or not 
if(radius<=0):
    exit("Side cannot be zero or negative")


#Displaying the area of a circle 
print("Area of Circle: ",pie*radius*radius , " meters Square")
