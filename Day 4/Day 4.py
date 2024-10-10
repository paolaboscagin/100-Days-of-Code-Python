import random




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


items = ["rock", "paper", "scissors"]


choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choice1 == 0:
    print("Your choice is Rock" + rock)
elif choice1 == 1:
    print("Your choice is Paper" + paper)
else:
    print("Your choice is Scissors" + scissors)


computer_pick = random.randint(0,2)


if computer_pick == 0:
    print("Computer's choice is Rock" + rock)
elif computer_pick == 1:
    print("Computer's choice is Paper" + paper)
else:
    print("Computer's choice is Scissors" + scissors)


if choice1 == 0 and computer_pick == 2:
    print("You win!")
elif choice1 == 0 and computer_pick == 1:
    print("You lose!")
elif choice1 == 1 and computer_pick == 0:
    print("You win!")
elif choice1 == 1 and computer_pick == 2:
    print("You lose!")
elif choice1 == 2 and computer_pick == 1:
    print("You win!")
elif choice1 == 2 and computer_pick == 0:
    print("You lose!")
else:
    print("It's a draw!")

