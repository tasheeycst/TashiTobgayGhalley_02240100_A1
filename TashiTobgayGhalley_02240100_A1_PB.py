import random

def guess_number():
    """
    Plays a number guessing game where the user tries to guess a randomly chosen number 
    between 1 and 100. Provides hints if the guess is too high or too low.
    """
    print("GUESS NUMBER GAME !")
    lower = 1
    upper = 100
    HiddenNumber  = random.randint(lower , upper)
    print (f"select number range from {lower} to {upper}")
    attempts =0

    while True:
        attempts += 1
        guess = int(input("Guess a Number : "))
        if guess < HiddenNumber:
            print("Your Guess is  Low! ")
        elif guess > HiddenNumber:
            print("Your Guess is High! ")
        elif guess == HiddenNumber:
            print("You Won!")
            break
            
        else :
            print("YOU WON!!!!!!")
    print(f' ATTEMPTED : {attempts} times . ')


def rock_paper_scissors():
    """
    Plays a game of Rock, Paper, Scissors against the computer. The user selects their choice,
    and the computer randomly selects its choice. The game runs for a specified number of rounds.
    """
  
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose 'rock', 'paper', or 'scissors'.")
    wins = {"rock":"scissors","scissors":"paper","paper":"rock"}
    rounds = int(input("ENTER THE ROUNDS OF GAME YOU WANT TO PLAY ! : "))

    user_score = 0
    computer_score = 0
    TIE = 0

    for i in range (rounds):
        while True:
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
            
            if user_choice not in choices:
                print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            else:
                break

       
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")
       

        if user_choice == computer_choice:
            print("It's a tie!")
            TIE += 1
        elif user_choice == wins[computer_choice]:
            print("You LOSE")
            computer_score +=1
        else:
            print("You win")
            user_score += 1
       
        print(f"Your Score : {user_score}  VS  computer_score : {computer_score}     TIE : {TIE}")

    final = (f"FINAL : You : {user_score}  Computer : {computer_score}    TIE : {TIE}")
    if user_score > computer_score:
        print("You WON")
    elif user_score == computer_score :
        print("TIE")
    else :
        print("You LOST")

    print(final)

       

    
def main ():
    """
    The main function providing a menu for the user to select between the Guess Number Game,
    Rock Paper Scissors Game, or exiting the program.
    """
    while True:
        print("1 . Guess Number Game !! ")
        print("2 . Rock ,Paper and Scissors Game !! ")
        print("3 . EXIT !! ")
        choose = input("Choose a Number for Gaming (1 to 3) : ")

    
        if choose  == '1':
            guess_number()
        elif choose == '2':
            rock_paper_scissors()
        elif choose == '3':
            print("EXITING THE PROGRAM !! ")
            break
        else:
            print("invalid")
            return
        choose = input ("do yuo want to continue with game (yes/no) : ")
        if choose != 'yes':
            print("Exiting the program. Goodbye!")
            break
if __name__ == "__main__":
    main()





