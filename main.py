"""
This program calculates the employee's productivity bonus
"""

# Define and initialize variables here
# Bonus score

bonusScore1 = 50.00
bonusScore2 = 75.00
bonusScore3 = 100.00
bonusScore4 = 200.00

# Input statements

employeeName = input("Employee's name: ")
numShifts = int(input("Number of Shifts: "))
numTrans = int(input("Number of transactions: "))
transValue = float(input("Transaction dollar value: "))


# If Statements here

prodScore = ((transValue/numTrans)/numShifts) 

if prodScore <= 30:
    bonus = bonusScore1
elif prodScore >= 31 and prodScore <= 69: 
      bonus = bonusScore2 
elif prodScore >= 70 and prodScore <= 199:
        bonus = bonusScore3
elif prodScore >=200:
    bonus = bonusScore4 


# Output Statements
print ("Employee Name: " + employeeName)
print ("Employee Bonus: $" + str(bonus))



