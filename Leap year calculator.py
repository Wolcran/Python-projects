# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# My solution
if year % 4 >=1:
    print ("Not leap year.")
elif year % 4 ==0:
    if (year/100) % 4 >= 1 and year%100 ==0:
        print ("Not leap year.")
    elif year % 400 ==0:
        print ("Leap year.")
    else:
        print ("Leap year.")

# Teacher's solution:
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")