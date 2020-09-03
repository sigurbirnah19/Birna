choice = input("Input f|a|b (fibonacci, abundant or both): ")

if(choice == 'f' or choice == 'b'):
    
    length_seq = int(input("Input the length of the sequence: "))

    print("Fibonacci Sequence:")
    print("-------------------")
    
    curr_num = 0
    prev_num = 0

    for i in range(0,length_seq):
     
        fib_num = curr_num + prev_num
        print(fib_num)
        prev_num = curr_num
        curr_num = fib_num
        
        if(i <= 1):
            curr_num = 1
            prev_num = 0
        
  

if(choice == 'a' or choice == 'b'):
    
    max_num = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    
    for i in range(1,max_num + 1):
        
        summa = 0

        for k in range(1,i):
            
             if i % k == 0:
                 summa = summa + k

        if summa > i:
            print(i)

        

