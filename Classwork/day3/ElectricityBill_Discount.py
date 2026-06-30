'''------- Problem Statement: Electricity Bill Discount 

An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 or more.
 Otherwise, no discount is applied.
  
 Write a Python program to accept the total bill amount from the user and 
 display the final amount to be paid. 
 ----------------------------------
Sample Input 1 
Enter the electricity bill amount: 6200 
------------------------------------
Sample Output 1 
Discount Applied! Final Bill Amount: ₹5580.0 
-------------------------------------
Sample Input 2 
Enter the electricity bill amount: 4200
---------------------------------------
Sample Output 2 
No Discount Applied! Final Bill Amount: ₹4200 
--------------------------------------------------------------
'''

# ------Coding-------

#input of bill from the user
bill = int(input("Enter the electricity bill amount: "))

#validate the bill
if(bill>=0):
    if(bill>=5000):
         discounted_amount = bill/10
         bill = bill - discounted_amount
         print("Discount Applied! Final Bill Amount: ", bill)
    else:
         print("No Discount Applied! Final Bill Amount: ",bill)

else:
     print("Please enter valid amount !!!")
     
#----------------------------------------------------
'''Output : 
Enter the electricity bill amount: 8762
--------------------------------------------
Discount Applied! Final Bill Amount: 7885.8
--------------------------------------------'''



   








