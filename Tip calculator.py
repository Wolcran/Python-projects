#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Version 1 - Step by step
print ("Welcome to the tip calculator!")
Bill= float(input("What was your total bill?"))
Percentage = int(input("What percentage tip would you like to give? 10,12 or 15?"))
People = int(input("How many people to split the bill?"))
Bill_with_tip = Bill * (1+Percentage/100)
Split_bill= round(Bill_with_tip/People, 2)
print (f"The bill is going to be ${Split_bill} per person")

#Version 2 - Compressed
print ("Welcome to the tip calculator!")
Bill= input("What was your total bill?")
Percentage = input("What percentage tip would you like to give? 10,12 or 15?")
People = input("How many people to split the bill?")
Total =round((float(Bill)/int(People)*(1+int(Percentage)/100)),2)
print (Total)

