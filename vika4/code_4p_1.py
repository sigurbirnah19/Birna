max_num = int(input("Input maximum number: "))

for i in range(1,max_num+1):

    j = len(str(i))
    summa = 0
    for k in range(0,j):
        digit = (i // 10**k % 10)
        summa += digit

    summa_power = summa ** 3
    
    if(summa_power == i):
        print(i)