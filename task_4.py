import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    for round in range(3):
        print("\nRound", round + 1)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer chooses:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("\nFinal Score:")
    print("You:", user_score)
    print("Computer:", computer_score)
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Sorry, you lost the game.")
    else:
        print("It's a tie!")

play_game()