n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 0
sec_num = 0
third_num = 1

for i in range(1,n+1):    

    next_num = first_num + sec_num + third_num
    print (next_num)

    first_num = sec_num
    sec_num = third_num
    third_num = next_num

    if ( i == 2 ) :
        first_num = 0
