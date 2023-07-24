print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#My solution:
direction = input("After a day of travel, you reach the edge of a forest. The roads splits here. Which way do you want to go? Left or Right?").lower()
direction = direction.lower()
# Shortcut: direction = input("After a day of travel, you reach the edge of a forest. The roads splits here. Which way do you want to go? Left or Right?").lower()
if direction == "left":
    print("This path is really quiet, the other seemed much more vibrant. Not a single sound anywhere. You reach a lake after some walking.")
    lake = input("What do you do? Swim or Wait?")
    lake = lake.lower()
    if lake == "swim":
        print("You decide to be brave and swim across. The lake is full of piranhas. Bad luck. Game over.")
    elif lake == "wait":
        print("You decide to wait and enjoy nature. You spot a cozy little cottage in the distance with its windows shining invitingly. It is getting late. You decide it would be wise to head in that direction.")
        print ("The house looks even better even from a close distance, you wonder who lives here? You enter and see three doors in front of you.")
        door = input("Which door would you like to enter? Red, Blue or Yellow?")
        door = door.lower()
        if door == "red":
          print("The door was a mimic, it bites your head off instantly. Game over.")
        elif door == "blue":
          print("The forest hag turns around as you open the kitchen's door where she was cooking and turns you into a broccoli. She hates broccolis. Game over.")
        elif door == "yellow":
          print("You are welcomed by a dimly lit room that has a chest full of gold coins and jewels in it. Congratulations, you win!")
        else:
          print("Pick a door. The owner might come home any minute. Red, Blue or Yellow?")
    else:
        print("Swim or wait. Make up your mind pal', there are only so many things to do in a forest.")
elif direction == "right":
    print("This part of the forest is really vibrant. The birds are singing beautifully. You are not paying attention to where you step and end up in a bear trap. You bleed to death. Game over.")
else:
    print("Please enter left or right. This is not a time to get creative.")
#Teacher's solution:
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

