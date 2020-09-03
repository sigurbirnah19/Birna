year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below
is_leap = False
if year % 4 != 0:
    is_leap = False
elif year % 100 != 0:
    is_leap = True
elif year % 400 == 0:
    is_leap = True
else:
    is_leap = False
    
print(is_leap)