import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "paper" and comp_choice == "rock") or
        (user_choice == "scissors" and comp_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
    print()