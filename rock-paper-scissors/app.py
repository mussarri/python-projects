import random

exit = False
score = 0

while exit == False:
    options = ["rock","paper","scissors"]
    user_choice = input("Select <R>ock, <P>aper, <S>cissors, <E>xit ")
    computer_choice = random.choice(options)
    if user_choice == "" or user_choice[0].lower() == "e" :
        print(f"Your score: {score}")
        exit = True
        break
    if user_choice[0].lower() == "r":
        if computer_choice[0].lower() == "r":
                print('You: Rock', "Computer: Rock", "Tie")
        elif computer_choice[0].lower() == "p":
                print('You: Rock', "Computer: Paper", "Computer Win")
                score = score - 1
        elif computer_choice[0].lower() == "s":
                print('You: Rock', "Computer: Scissors", "You Win")
                score = score + 1
    elif user_choice[0].lower() == "p":
        if computer_choice[0].lower() == "r":
                print('You: Paper', "Computer: Rock", "You Win")
                score = score + 1
        elif computer_choice[0].lower() == "p":
                print('You: Paper', "Computer: Paper", "Tie")
        elif computer_choice[0].lower() == "s":
                print('You: Paper', "Computer: Scissors", "Computer Win")
                score = score - 1
    elif user_choice[0].lower() == "s":
        if computer_choice[0].lower() == "r":
                print('You: Scissors', "Computer: Rock", "Computer Win")
                score = score - 1
        elif computer_choice[0].lower() == "p":
                print('You: Scissors', "Computer: Paper", "You Win")
                score = score + 1
        elif computer_choice[0].lower() == "s":
                print('You: Scissors', "Computer: Scissors", "Tie")
    else:
        print("Invalid input")
    
    