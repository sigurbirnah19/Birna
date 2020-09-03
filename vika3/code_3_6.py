a0 = int(input("Input a positive int: "))   # Do not change this line

# Fill in the missing code below
while a0 != 1:
    print(a0)
    
    if a0 % 2 == 0 :
        a0=int(a0/2)
    else:
        a0=int(3*a0 + 1)

print(a0)