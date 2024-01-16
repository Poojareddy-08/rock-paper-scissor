import random

def play_rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors!")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Validate user input
        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"You chose {user_choice}, computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Current scores: You {user_score}, Computer {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nFinal scores: You {user_score}, Computer {computer_score}")
    print("Thanks for playing!")

play_rock_paper_scissors()
