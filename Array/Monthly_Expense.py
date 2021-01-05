# Let's make a list first for 5 month's expenses.
# January - 3000 $
# February - 2200 $
# March - 2100 $
# April - 2500 $
# May - 1800 $
# Let's define an array for the list given above by name exps
exps = [3000,2200,2100,2500,1800]
# 1. In February, how many dollars you spent less compare to January ?
print("In Febryary this much less was spent compare to January: ",exps[0]-exps[1]) # 800 $
# 2. Find out the total of first Three month's Expenses.
print("Total Expense of January, February and March: ",exps[0]+exps[1]+exps[2]) # 7300 $
# 3. Find out if you spent exactly 2100 $ in any month.
print("Did I spent 2100 $ in any month ?: ", 2100 in exps) # March - True
# 4. June is just finished and you have spent 2300 $. Add this to the Expense list.
exps.append(2300)
print("Expense at the end of June: ",exps) # [3000,2200,2100,2500,1800,2300]
# 5. You have mistaken an entry in the month of April, revise it with 500$ deduction.
exps[3] = exps[3] - 500
print("Expenses after revised: ",exps) # [3000,2200,2100,2000,1800,2300]
