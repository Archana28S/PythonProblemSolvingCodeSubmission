# Problem Set 1
# Name: Archana Sharma
# Time Spent: 3:00

balance = float(input("Enter the outstanding balance on the credit card: "))
ann_interest_rt = float(input("Enter the annual interest rate as a decimal: "))
monthly_interest_rt = ann_interest_rt/12.0
low = balance/12.0
high = (balance * ((1.0 + monthly_interest_rt)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0
def calculate(month, balance, minPay, monthly_interest_rt):
    while month <12:
        unpaid_balance = balance - minPay
        balance = unpaid_balance + (monthly_interest_rt * unpaid_balance)
        month += 1
        return balance
    while abs(balance) >= epsilon:
        balance = initbalance
        month = 0
        balance = calculate(month, balance, minPay, monthly_interest_rt)
        if balance > 0:
            low = minPay
        else:
            high = minPay
            minPay = (high + low)/2.0
            minPay = round(minPay,2)
            print('Lowest Payment: ' + str(minPay))
