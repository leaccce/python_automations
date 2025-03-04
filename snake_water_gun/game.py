import os
import random
os.chdir("Projects/snake_water_gun")
name=input("Welcome to the Snake Water Gun Game !\nPlease enter your Name :")
print(f"""Welcome {name} !. The Rules are simple.\nYou have to choose between Snake, Water and Gun.
The computer will also choose between Snake, Water and Gun. 
The gun beats the snake, the snake beats the water and the water beats the gun.
Your score will increase by one if you win. You can play till you lose to the computer.""")
bucket=['s','w','g']
score=0
def score_upate(score):
    with open("score.txt","w") as f:
        f.write(str(score))
while True:    
    choice=input("Enter your choice - 's' for Snake, 'w' for Water and 'g' for Gun: ")
    # raise ValueError("Please enter a valid choice") if choice not in bucket else None
    x=random.choice(bucket)
    print(f"Computer's choice is {x}")
    match choice:
        case 's':
            match x:
                case 's':
                    print("It's a tie !")
                case 'w':
                    print("You win !")
                    score+=1
                case 'g':
                    print("You lose !")
                    break
        case 'w':
            match x:
                case 's':
                    print("You lose !")
                    break
                case 'w':
                    print("It's a tie !")
                case 'g':
                    print("You win !")
                    score+=1
        case 'g':
            match x:
                case 's':
                    print("You win !")
                    score+=1
                case 'w':
                    print("You lose !")
                    break
                case 'g':
                    print("It's a tie !")
print(f"Your score is {score}")
with open("score.txt") as f:
    high_score=max(int(f.read()),score)
    score_upate(high_score) 

h=input("Do you want to see the highscore ?")
if h=="yes":
    with open("score.txt","r") as f:
        print(f.read())