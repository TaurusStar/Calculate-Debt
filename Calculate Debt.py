from inputCheck import canBeFloat

debt = input('Enter amount of debt:')
interest_rate = input('Enter % interest rate:')
monthly_payment = input('Enter monthly payment:')

# check if inputs can be converted to integers
if canBeFloat(debt) and canBeFloat(interest_rate) and canBeFloat(monthly_payment):

    #convert inputs to floats
    debt = float(debt)
    interest_rate = float(interest_rate)
    monthly_payment = float(monthly_payment)
    
    if monthly_payment < 100:
        print('You will need to make bigger payments.\nAt this rate you will never pay off the debt.')
    else:#monthly payment is large enough
        #assign debt to the origin balance
        balance = debt
        #let mounth count begin from 0
        y = 0
        while balance > 0:
            if balance > monthly_payment:
                y = y + 1
                Interest = (interest_rate*0.01/12)*balance
                mp = monthly_payment*y
                if monthly_payment <= Interest:
                    balance = balance + Interest
                else:
                    balance = balance + Interest - monthly_payment
                print('Month =',y)
                print('Interest this month = '"{0:.2f}".format(Interest))
                print('Balance going forward = '"{0:.2f}".format(balance))
                print('Total payments = '"{0:.2f}".format(mp))
            else:
                y = y + 1
                Interest = (interest_rate*0.01/12)*balance
                mp = monthly_payment*(y-1) + balance + Interest
                balance = 0
                print('Month =',y)
                print('Interest this month = '"{0:.2f}".format(Interest))
                print('Balance going forward = '"{0:.2f}".format(balance))
                print('Total payments = '"{0:.2f}".format(mp))

else:#inputs cannot be floats
    print('Bad input, enter a number next time.')
    
#Loop prints 'Press enter to exit' until the user enters
#the empty string when prompted    
while True:
    x = input('Press enter to exit')
    if x =='':
        break



         
