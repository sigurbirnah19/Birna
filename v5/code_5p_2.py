# You might need this to calculate a square root using math.sqrt
import math

num = int(input("Enter a number (-1 to exit) "))
k = 0
total_sum = 0
A1 = 0
Ak = 0
Qk_1 = 0
Qk = 0
# Loop until the user types in -1


while( num != -1 ):
    k += 1
    # Calculate the cumulative moving average and standard deviation
    
    Ak = Ak_1 + ((num - Ak_1)/k)
    current_average = Ak
    # Print them out within the loop

    Qk = Qk_1 + (num - Ak_1)*(num - Ak)

    if( k == 1):
        Qk = 0
        standard_deviation = float(Qk)
    else:
        standard_deviation =math.sqrt( Qk/k)

    Ak_1 = Ak
    Qk_1 = Qk

    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))
    
    
    num = int(input("Enter a number (-1 to exit) "))
