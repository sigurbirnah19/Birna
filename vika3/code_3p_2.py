num = 9
found_it = False
while ( not found_it and num < 100 ):

    num = num + 1

    first_num  = num // 10**0 % 10
    second_num = num // 10**1 % 10

    square = num * num
    first_num_sq =  square // 10**0 % 10
    second_num_sq = square  // 10**1 % 10

    if( first_num == first_num_sq and second_num == second_num_sq ):
        found_it = True

if( found_it):
    print (num)
else:
    print ("didn't find it")