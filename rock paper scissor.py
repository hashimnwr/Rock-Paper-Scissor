import random

print("Hello and welcome to playing Rock Paper Scissor game")


rps = ["r", "p", "s"]

x = True

computer_score = 0
user_score = 0

while x:
    computer_choice = random.choice(rps)
    user_choice = input("Enter '0' to exit \nr - Rock \np - Paper \ns - Scissor? ").lower()
    if (computer_choice == "r" and user_choice == "s") or (computer_choice == "p" and user_choice == "r") or (computer_choice == "s" and user_choice == "p"):
        
        computer_score += 1

        print(f"You chose:      {user_choice}")
        print(f"Computer chose: {computer_choice}")

        print(f"Computer score: {computer_score}")
        print(f"User score:     {user_score}")

    elif (computer_choice == "r" and user_choice == "p") or (computer_choice == "p" and user_choice == "s") or (computer_choice == "s" and user_choice == "r"):
        
        user_score +=1

        print(f"You chose:      {user_choice}")
        print(f"Computer chose: {computer_choice}")

        print(f"Computer score: {computer_score}")
        print(f"User score:     {user_score}")

    elif (computer_choice == "r" and user_choice == "r") or (computer_choice == "p" and user_choice == "p") or (computer_choice == "s" and user_choice == "s"):
        
        print(f"You chose:      {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        print(f"Computer score: {computer_score}")
        print(f"User score:     {user_score}")
    
    elif user_choice == "0":
        print(f"Computer score: {computer_score}")
        print(f"User score:     {user_score}")

        if user_score == computer_score:
            print("Draw!")
        elif user_score > computer_score:
            print("User Wins!!!")
        else:
            print("Computer Wins :(")

        x = False

    else:

        print(f"You chose:      {user_choice}")
        print(f"Computer chose: {computer_choice}")

        print("Input missmatched!!!")
