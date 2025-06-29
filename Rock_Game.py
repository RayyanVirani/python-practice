import random

Options = ["rock" , "paper" , "scissors"]
computer_score = 0
player_score = 0

outcomes = {
        ("rock" , "rock"): "draw",
        ("rock" , "paper"): "computer",
        ("rock" , "scissors"): "user",
        ("paper" , "rock"): "user",
        ("paper" , "paper"): "draw",
        ("paper" , "scissors"): "computer",
        ("scissors" , "rock"): "computer",
        ("scissors" , "paper"): "user",
        ("scissors" , "scissors"): "draw",
    }

print("Are you ready to play Rock Paper Scissors!")

def Game():

    global player_score
    global computer_score

    computer_choice = random.choice(Options)

    while True:

        try:
            
            print("Choose either rock or paper or scissors")
            user_choice = str(input("Enter your choice: "))

            result = outcomes[(user_choice , computer_choice)]

            if result == "draw":
                print("I choose: " + computer_choice)
                print("We both tied lol, so no one gets a point.")
            elif  result == "user":
                print("I choose: " + computer_choice)
                print("You won this round, so you get a point")
                player_score = player_score + 1
            else:
                print("I choose: " + computer_choice)
                print("I won this round, So I get the point")
                computer_score = computer_score + 1

            break    
        except KeyError:
            print("Invalid Input, try again")

keep_playing = True
Game()
while keep_playing == True:
    print("Do you want to continue playing? Type yes or no")
    ask = str(input("Your answer: "))
    try:
        if ask == "yes":
            Game()
        elif ask == "no":
            print("The game has been terminated")
            print(f"Your score is {player_score}")
            print(f"Computer Score is {computer_score}")
            if computer_score == player_score:
                print("We both tied")
            elif computer_score > player_score:
                print("Yay! I won.") 
            else:
                print("Whooo! You Won!")  
            keep_playing = False 
        else:
            print("Invalid Input, Try Again")    
    except:
        print("Invalid input. Try again. yes or no only")