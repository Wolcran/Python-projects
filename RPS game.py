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
import random
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
rps = (rock, paper, scissors)
computer = random.randint (0, len(rps)-1)

if 3> player >= 0:
    if player == 0:
        print (rock)
    elif player == 1:
        print (paper)
    elif player == 2:
        print (scissors)
    print ("Computer chose:")
    if computer == 0:
        print (rock)
    elif computer == 1:
        print (paper)
    elif computer == 2:
        print (scissors)
else:
    print ("Please select a valid option")

if player == computer:
    print ("It's a draw!")
if player == 0:
    if computer ==1:
        print ("Paper beats rock. You lose!")
    elif computer ==2:
        print ("Rock beats Scissors. You win!")
if player == 1:
    if computer ==0:
        print ("Paper beats rock. You win!")
    elif computer ==2:
        print ("Scissors beats paper. You lose!")
if player == 2:
    if computer ==0:
        print ("Rock beats Scissors. You lose!")
    elif computer ==1:
        print ("Scissors beats paper. You win!")

# Teacher's choice'
#I completely forgot to implement using the list to print the image, did it all manually.
#Apart from this, it functions the same way.
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")