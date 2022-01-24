def monthly_interest():
    print("Monthly Interest Calculator!")
    annual_interest = eval(input("Enter your annual interest rate: "))
    billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    net_balance = eval(input("Enter your net balance: "))
    payment_amount = eval(input("Enter the payment amount: "))
    day_of_payment = eval(input("Enter the day of the billing cycle in which the payment was made: "))
    step_1 = net_balance * billing_cycle
    step_2 = payment_amount * day_of_payment
    step_3 = step_1 - step_2
    step_4 = step_3 / billing_cycle
    step_5 = annual_interest / 12
    step_6 = step_5 / 100
    step_7 = step_4 * step_6
    print("The monthly interest rate will be $"+str(step_7))
