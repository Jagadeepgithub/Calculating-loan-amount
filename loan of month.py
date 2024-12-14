#Get details of loan
money_owed=float(input("How much money you want,in dollars?\n"))#50000
apr=float(input("What is the annual percentage rate of intrest of the loan?\n"))#3%
payment=int(input("How much money you will pay for month,in dollars?\n"))#1000
months=int(input("How many months do you want to see results for?\n"))#24

monthly_rate=apr/100/12

#calculate the intrest to pay
intrest_paid=money_owed*monthly_rate

#add in intrest
money_owed=money_owed+intrest_paid

#make payment
money_owed=money_owed-payment

print('paid',payment,'of which',intrest_paid,'was intrest',end='')
print('now i owe',money_owed)