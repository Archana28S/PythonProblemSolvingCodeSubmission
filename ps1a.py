# Problem Set 1
# Name: Archana Sharma
# Time Spent: 12:00

#Problem 1:
#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month. 
#Use input() to ask for the following three floating point numbers:
#the outstanding balance on the credit card
#annual interest rate
#minimum monthly payment rate
#For each month, print the minimum monthly payment, remaining balance, principle paid in the format shown in the test cases below. All numbers should be rounded to the nearest paisa. Finally, print the result, which should include the total amount paid that year and the remaining balance.


outstand_balance = float(input('Enter the outstanding balance on your credit card:'))
ann_interest_rt = float(input('Enter the annual credit card interest rate as a decimal:'))
min_month_rt = float(input('Enter the minimum monthly payment rate as a decimal:'))
Month = int(1)

for month in range (0,12):
    
    Min_monthly_payment = round((min_month_rt * outstand_balance),2)
    Interest_paid = round((ann_interest_rt/12 * outstand_balance),2)
    Principle_paid = round((Min_monthly_payment - Interest_paid),2)
    Remaining_balance = round((outstand_balance - Principle_paid),2)
    outstand_balance = Remaining_balance
    Month +=1
    print (("Minmimum monthly payment ") + str(Min_monthly_payment))
    print (("Principle Paid ") + str(Principle_paid))
    print (("Remaining Balance ") + str(Remaining_balance))
    print (("Month: ") + str(Month))

print("Remaining Balance",Remaining_balance)    
    



