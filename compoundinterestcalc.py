#####################################################################
#     Program:  Compound Interest Calculator V1.0.0
# 
#  Created by:  Chad Stalnaker            Date Created: July 29, 2023
# 
# Language(s): Python v3.10.4            Last Modified: N/A
#
#                                                  REV: 0
#
# Use: Calculates compound interest earned based on user input
# 
# Defined Functions:
#
#   questions():
#       - Gets user input
#
#   calculation(principal, annual_rate, time, compoundtime):
#       - Preforms compound interest calculation, if additional
#         deposits are not desired.
#
#   strtointtime(strngnput):
#       - Converts string input of time period into integer.
#
#   additionpayments():
#       - Gets user input for additional payment calculations.
#
#####################################################################

# Gets the input from user to preform the calculations.
def questions():
    principal = input("How much are you starting with in the account?")
    annual_rate = float(input("What is the annual rate of interest?"))
    interestcomp = input("Is interest compounded Daily, Monthly, Quarterly, or Annually?")
    time = input("How many years do you want to calculate for?")
    
    addpayments = 0
    morepayments = input("Will you make additional deposits? [Y/N]")
    if morepayments.lower() == 'y':
        addpayments = 1

    principal = int(principal)
    annual_rate = float(annual_rate/100)
    time = int(time)
    
    answers = {'principal':principal, 
               'annual_rate':annual_rate, 
               'interestcomp':interestcomp, 
               'time':time, 
               'addpayments':addpayments}
    
    return answers
    
# Calculates for compound interest if additional deposits are not
# desired.
def calculation(principal, annual_rate, time, compoundtime):
    principal = int(principal)
    annual_rate = float(annual_rate)
    time = int(time)
    compoundtime = int(compoundtime)
    amount_after = float((principal*(( 1+(annual_rate/compoundtime))
                    **(compoundtime * time))))
    fnlnmbrs = {'amount_after':amount_after, 
                'compoundtime':compoundtime}
    return fnlnmbrs
    
# Converts str() input to int() output
def strtointtime(strngnput):
    if strngnput.lower() == 'd' or 'daily':
        numberout = int(365)
    elif strngnput.lower() == 'w' or 'weekly':
        numberout = int(52)
    elif strngnput.lower == 'b' or 'bi-weekly':
        numberout = int(26)
    elif strngnput.lower() == 'm' or 'monthly':
        numberout = int(12)
    elif strngnput.lower() == 'q' or 'quarterly':
        numberout = int(4)
    elif strngnput.lower() == 'a' or 'annually':
        numberout = int(1)
    else:
        numberout = str("Something went wrong, type the correct letter.")
    return numberout
    
# Calculates the compound interest if additional deposits are desired.
def additionpayments():
    print("How aften will you be making additional payments?")
    ans = str(input("Daily, Weekly, Bi-Weekly, Monthly, Quarterly, Annually?"))
    addmoney = float(input("How much will you be depositing?"))
    deptime = strtointtime(ans)
    additionaldeps = {'addmoney':addmoney, 'deptime':deptime, 'ans':deptime}
    
    return additionaldeps


# Main Program

stepone = questions()
principal = int(stepone['principal'])
annual_rate = float(stepone['annual_rate'])
interestcomp = str(stepone['interestcomp'])
time = stepone['time']
addpayments = int(stepone['addpayments'])
compoundtime = strtointtime(interestcomp)
secondstep = calculation(principal, annual_rate, time, compoundtime)
amount_after = float(secondstep['amount_after'])

# Checks if additional deposits option was chosen.
if addpayments == 1:
    stepthree = additionpayments()
    additionaldeposit = int(stepthree['addmoney'])
    depositincrements = int(stepthree['deptime'])
    totaldeposits = ((int(time)*int(depositincrements)))
    totalamount = 0
    i = 0
    beginamount = (principal + (principal * ((annual_rate / compoundtime))))
    while totaldeposits > 0:
        adddepandinterest = (additionaldeposit + (additionaldeposit * (annual_rate / compoundtime)))
        if i < 1:
            totalamount = (beginamount + adddepandinterest)
            i = i + 1
            totaldeposits = totaldeposits - 1
        else:
            totalamount = float((totalamount + adddepandinterest))
            totaldeposits = totaldeposits - 1
# Prints results of calculations for additional deposits.
    print("If you start with a deposit of ${} and deposit an additional deposits of ${}".format(principal, additionaldeposit))
    print("\nYou will earn a total of $%.2f after {} years".format(time) %totalamount)
else:
# Prints results of calculations without additional deposits.
    print("You will have a total of $%.2f dollars after {} years".format(time) %amount_after)
    