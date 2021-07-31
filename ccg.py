import random
#Declare computer_score and player_score as variables
#show colors choices to user to choose & enter a color value number:

print("Winning rules of the colors choices game as follows : "+ "\nEnter a number from one to five and match computer choice to win the computer.")
computer_score = 0
player_score = 0

while True:
    print("red = 1 \nyellow = 2\norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ")

    #take the input from user
    player_choice = int(input("User turn: "))

    while player_choice > 5 and player_choice < 1:
        player_choice = int(input("enter valid input : "))

    if player_choice == 1:
        choice_col = 'red'
    elif player_choice == 2:
        choice_col = 'yellow' 
    elif player_choice == 3:
        choice_col = 'orange'          
    elif player_choice == 4:
        choice_col = 'green'
    else:
        choice_col = 'blue'


    #print user choice
    print("user color choice is: "+ choice_col)
    print("\nNow its computer turn to choose a color.....")

    #computer chooses randomly any number
    #among 1 to 5 using randint method of random module
    computer_choice = random.randint(1,5)

    #looping until comp_choice is equal to the player choice 
    while computer_choice == player_choice:
        computer_choice = random.randint(1,5)

    #initializing the value of comp_choice_col var corresponding to the computer_choice value
    if computer_choice == 1:
        compu_choice_col = 'red'
    elif computer_choice == 2:
        compu_choice_col = 'yellow'
    elif computer_choice == 3:
        compu_choice_col = 'orange'
    elif computer_choice == 4:
        compu_choice_col = 'green'
    else:
        compu_choice_col = 'blue'
    print("computer color  choice is : " + compu_choice_col)

    #conditions of Winning
    if(choice_col == compu_choice_col):
        player_score += 1
        print("player_score : "+str(player_score))
        print("computer_score: "+str(computer_score))
    else:
        computer_score += 1

        print("player_score : "+str(player_score))
        print("computer_score: "+str(computer_score))


    answer = input("Do you want to play again? (Y/N)")
    if answer == 'n' or answer == 'N':
        break

    #after coming out of the while loop
if computer_score == player_score:
    print("Game is Tied")
    print("\nThanks for playing")
elif computer_score < player_score:
    print("Player is Victorious")
    print("\nThanks for playing")
elif computer_score > player_score:
    print("\n<== Computer wins ==>")
    print("\nPlayer is Defeated")
    print("\nThanks for playing")
    
                           
