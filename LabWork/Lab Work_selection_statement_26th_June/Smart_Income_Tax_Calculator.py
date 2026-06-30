''' Problem Statement: Smart Income Tax Calculator 
A government tax portal calculates tax based on the following conditions: 

 •Income up to ₹5,00,000 → No tax 
 • ₹5,00,001 to ₹10,00,000 → 10%  
 • ₹10,00,001 to ₹20,00,000 → 20%  
 • Above ₹20,00,000 → 30%  

 Additional Benefits: 
 •Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
 • Women taxpayers receive an additional 2% rebate on tax.  

 Write a Python program to calculate the final tax amount payable. '''

#  ---------------Coding----------------------------------

# User input of income , age and gender

income = int(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ")

# default rebate is 0
age_rebate = 0
gender_rebate = 0


# Applying conditions whether to pay tax or not
if(income>500000):
    # Tax to pay if income is between 5 lakh and 10 lakh 
    if(income>=500001 and income<=1000000):
        tax = (income*10)/100
        print("Tax before rebate: ₹",tax)

        if(age>=60):
            age_rebate = (tax*5)/100
            print("Senior Citizen Rebate: ₹",age_rebate)

        if(gender.lower() == "female" ):
            gender_rebate = (tax*2)/100
            print("Women Rebate: ₹",gender_rebate)

        final_tax = tax - (age_rebate + gender_rebate)    
        print("Final Tax Payable: ₹", final_tax)
# Tax to pay if income is between 10 lakh and 20 lakh
    elif(income>=1000001 and income<=2000000):
        tax = (income*20)/100  
        print("Tax before rebate: ₹",tax)

        if(age>=60):
            age_rebate = (tax*5)/100
            print("Senior Citizen Rebate: ₹",age_rebate)
        if(gender.lower() == "female" ):
            gender_rebate = (tax*2)/100
            print("Women Rebate: ₹",gender_rebate)

        final_tax = tax - (age_rebate + gender_rebate)    
        print("Final Tax Payable: ₹", final_tax)    
        
# Tax to pay if income is above 20 lakh
    elif(income>=2000001):
        tax = (income*30)/100
        print("Tax before rebate: ",tax)

        if(age>=60):
            age_rebate = (tax*5)/100
            print("Senior Citizen Rebate: ",age_rebate)


        if(gender.lower() == "female" ):
            gender_rebate = (tax*2)/100
            print("Women Rebate: ₹",gender_rebate)    



        final_tax = tax - (age_rebate + gender_rebate)    
        print("Final Tax Payable: ₹", final_tax)    


else:
    print("No tax applicable !!!")




# ---------------------------------------------------------------------

''' Output : 
Enter Annual Income: 989898
Enter Age: 78
Enter Gender (M/F): female
--------------------------------------------
Tax before rebate: ₹ 98989.8
Senior Citizen Rebate: ₹ 4949.49
Women Rebate: ₹ 1979.796
Final Tax Payable: ₹ 92060.514
--------------------------------------------'''
    


        





