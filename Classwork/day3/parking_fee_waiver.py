'''----- Problem 2: Parking Fee Waiver 


A shopping mall waives the parking fee if a customer has made purchases worth ₹2,000 or more.
 Otherwise, the customer must pay a parking fee of ₹100. 
 
 Write a Python program to accept the purchase amount and display whether the parking fee is waived or payable. 


----------------------------------
Sample Input 1 
Enter the purchase amount: 2500 
------------------------------------
Sample Output 1 
Parking Fee Waived! Parking Fee: ₹0  
-------------------------------------
Sample Input 2 
Enter the purchase amount: 1500 
---------------------------------------
Sample Output 2 
Parking Fee Applicable! Parking Fee: ₹100 
--------------------------------------------------------------
'''

# ------Coding-------

#input of bill from the user
bill = int(input("Enter the purchase amount: "))

#validate the bill
if(bill>=0):
    if(bill>=2000):
         print("Parking Fee Waived! Parking Fee: ₹0 ")
    else:
         print("Parking Fee Applicable! Parking Fee: ₹100")

else:
     print("Please enter valid amount !!!")
     
#----------------------------------------------------

'''Output : 

Enter the purchase amount: 5325
--------------------------------------------
Parking Fee Waived! Parking Fee: ₹0 
--------------------------------------------'''