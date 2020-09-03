p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

# ...now fill in the rest
if((p1_move == 'rock' and p2_move =='paper' ) 
or (p1_move == 'scissors' and p2_move=='rock') 
or (p1_move == 'paper' and p2_move == 'scissors')):
    print ('Winner: Player 2')
elif(p1_move == 'rock' and p2_move == 'rock'
or (p1_move =='scissors' and p2_move == 'scissors')
or (p1_move == 'paper' and p2_move == 'paper')):
    print("It's a draw")
else:
    print('Winner: Player 1')