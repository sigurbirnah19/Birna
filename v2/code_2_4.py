d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if d1 <= 0 or d1 > 6 or d2 <= 0 or d2 > 6:
    print("Invalid input")
    
elif d1 == d2:
    print ("Pair")

else:
    print(d1+d2)