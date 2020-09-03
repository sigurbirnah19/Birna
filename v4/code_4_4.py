max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

days_when_amount_acquired = 0
amount = 1
summa=0

# Fill in the missing code
for i in range (1,max_days+1):
    summa += amount
    amount = amount * 2
    if(summa >= target):
        days_when_amount_acquired = i
        break

print('Days needed:',days_when_amount_acquired)