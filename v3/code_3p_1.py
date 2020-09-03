n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
count = 2
if( n == 1):
    prime = False
else:
    prime = True

while (prime == True and count<n):
    if( n % count == 0):
        prime = False
        break

    count = count + 1


# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")
