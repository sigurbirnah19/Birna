length = int(input("Input the length of series: "))
summa = 0
for i in range(1,length+1):
    if(i%2==0):
        number = -i*2
    else:
        number = i*2
        
    summa += number
    print(number)
    
print("Sum: " + str(summa))