n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
counter = 1
while(counter <= n):
    if(n%counter == 0):
        print(counter)
    counter = counter + 1