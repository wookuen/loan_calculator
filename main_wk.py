# This is what I wrote by myself
# write your code here
print("Enter the loan principal:")
loan_principal = int(input())

print("""What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment""")
option = str(input())

monthly_payment_input = int()
remaining_month_input = int()

if option == "m":
    print("Enter the monthly payment:")
    monthly_payment_input = int(input())
    monthly_payment = -(-loan_principal // monthly_payment_input)
    if monthly_payment == 1:
        print("It will take " + str(monthly_payment) + " month to repay the loan")
    else:
        print("It will take " + str(monthly_payment) + " months to repay the loan")
elif option == "p":
    print("Enter the number of months:")
    remaining_month_input = int(input())
    last_month_payment = loan_principal - (remaining_month_input - 1) * -(-loan_principal // remaining_month_input)
    #value = loan_principal / monthly_payment_input
    if loan_principal % remaining_month_input == 0:
        print("Your monthly payment = ", -(-loan_principal // remaining_month_input))
    else:
        print("Your monthly payment = ", -(-loan_principal // remaining_month_input), "and the last payment = ", last_month_payment)
