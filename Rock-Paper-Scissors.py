import random
print("Welcome to rock paper scissor")
user_choice_number = input("Enter 0 for rock 1 for paper 2 for scissors")
computer_choice_number = random.randint(0,2)
user_choice,computer_choice = "",""
if user_choice_number == 0:
    user_choice = "rock"
elif user_choice_number == 1:
    user_choice = "paper"
else:
    user_choice = "scissors"
if computer_choice_number == 0:
    computer_choice = "rock"
elif computer_choice_number == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"
if user_choice == computer_choice:
    print(f"Both choose same {user_choice}... DRAW!!!!")
elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
    print(f"You loose the game as your choice is {user_choice} and computer choice is {computer_choice}")
else:
    print(f"You Won the GAME...! your choice is {user_choice} and computer choice is {computer_choice}")
