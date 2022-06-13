import random

print("Rules of the Rock paper scissor game is : \n"
    +"Rock vs paper->paper wins \n"
    + "Rock vs scissor->Rock wins \n"
    +"paper vs scissor->scissor wins \n")

R = "rock"
P = "paper"
S = "scissor"
results= [("R","S"),("P","R"),("S","P")]

moves=[result[1]for result in results]



player = input("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n:  ")
while player == "rock" or "paper" or "paper":
    computer = random.choice(moves)
    print("computer: " + computer)
    if player == computer:
        print("Its a tie.Play again")
    elif(player,computer) in results  :
        print("player wins")
    elif(computer,player) in results:
        print("computer wins")
    else:
        print("Invalid choice ")
        player = input("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n:  ") 
    break
        
print("Do you want to play again? (Y/N)")
ans = input()

if ans == 'n' or ans == 'N':
    print("\nThanks for playing")
       
           
               