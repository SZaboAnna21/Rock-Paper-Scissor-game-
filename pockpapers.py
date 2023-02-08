#rock paper sicisors 
import time
import random

print("Hello this is a Rock Paper Scissors game")

comuter_points = 0
player_points = 0



def IsThePlayerReady():
    valid_answer =["yes", "no", "Yes", "No"]
    valid= False
    while valid == False:
        answer = input("Do you want to play ( yes or no)  ")
        if answer not in valid_answer :
            print("Please choose form yes or no")
        elif answer == "no" or answer =="No":
            print("thank you for playing! ")
            print(f"I win: {comuter_points} times \nYou win: {player_points} ")
            exit()
        else:
            valid = True
            return True


valid= IsThePlayerReady()

while valid:
    print('Rock, Paper, Scissors - Shoot!')
    time.sleep(2)
    valid_choises=["R", "P", "S"]
    valid2=True
    while valid2:
        player_chiose = input("Choose your weapon! \n[R]ock], [P]aper, or [S]cissors:  ")
        if (player_chiose in valid_choises) :
            if player_chiose == "R":
                print("You choose Rock")
            elif player_chiose =="S":
                print(" You choose Scissors")
            elif player_chiose == "P":
                print("You choose Paper")
            valid2= False
        else: print("Sorry but that is not valid choose form (R P S) ")
        time.sleep(1)


    opponet_choise = random.choice(valid_choises)
    time.sleep(2)
    # game 2
    if opponet_choise =="R":
        print("I choose Rock")
    elif opponet_choise == "s":
        print("I choose Scissors")
    else:
        print("I choose Paper")

    
    if player_chiose == opponet_choise :
        print("Its a tiee!")
        valid= IsThePlayerReady()
    elif player_chiose == "P" and opponet_choise =="S":
        print("Scissors beats Paper, I win")
        comuter_points +=1
        valid= IsThePlayerReady()
    elif player_chiose == "S" and opponet_choise =="R":
        print("Rock beats Scissors, I win")
        comuter_points +=1
        valid= IsThePlayerReady()
    elif player_chiose == "R" and opponet_choise =="P":
        print("Paper beats Rock, I win")
        comuter_points +=1
        valid= IsThePlayerReady()
    else:
        print("You win!!")
        player_points +=1
        valid= IsThePlayerReady()
