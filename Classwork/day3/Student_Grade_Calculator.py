'''-------------- Problem Statement 3 : Student Grade Calculator

A school assigns grades based on the marks obtained by students according to the following criteria:
* Marks 90 and above → Grade A
* Marks 75 to 89 → Grade B
* Marks 50 to 74 → Grade C
* Below 50 → Grade F

Write a Python program to accept marks from the user and display the corresponding grade.
-------------------------------------------------------------'''
#------- Coding ---------------
#input of marks from the user
Marks = float(input("Enter Marks: "))

# validate the marks
if(Marks >= 90):
   print("Grade A")
elif(Marks >= 75 and Marks<=89):
   print("Grade B")
elif(Marks >= 50 and Marks<=74):
   print("Grade C")
elif(Marks <= 49):
   print("Grade F")

#----------------------------------------------------
'''Output : 
Enter Marks: 42
Grade F
--------------------------------------------'''