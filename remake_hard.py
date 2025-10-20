loan_amo = eval(input("Enter loan amount ---> "))
loan_per = eval(input("Enter loan period in years ---> "))

loan_per *= 12
principal = loan_amo / loan_per
balance = loan_amo
print("PAYMENT SCHEDULE")
print("|Month|\t|Monthly Payment|\t|Interest|\t|Principal|\t|Reamaining Loan|")

for i in range(1, loan_per + 1, 1):
    balance -= principal
    interest = balance * 0.0125
    monthly = interest + principal
    print(f"{i}\t {round(principal,2)}\t\t\t{round(balance,2)}\t\t{round(interest,2)}\t\t{round(monthly,2)}")
