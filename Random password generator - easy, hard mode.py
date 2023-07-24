# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

number = int(random.randint (0,len(numbers)-1))

symbol = int(random.randint (0,len(symbols)-1))

letter = int(random.randint (0,len(letters)-1))

# Easy solution

for a in range (1, nr_letters+1):
#     Here I originally only specified "nr_letters" - this lead to an undiscovered calculation error. Fixed.
    print (random.choice(letters), end ="")
for b in range(1,nr_numbers+1):
    print(random.choice(numbers), end="")
for c in range (1,nr_symbols+1):
    print (random.choice(symbols), end ="")


# Hard solution
password = []

for a in range(1,nr_letters+1):
    password.append(random.choice(letters))
for b in range(1,nr_numbers+1):
    password.append(random.choice(numbers))
for c in range(1,nr_symbols+1):
    password.append(random.choice(symbols))

  ## shuffling the resultant password
random.shuffle(password)

print (''.join (password))

# Teacher's solution:

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")

# Questions that came up? What is the difference between these two for loops?
# Answer:

# for a in range(nr_letters):
#     print (a)
# for char in range(1, nr_letters):
#     print (char)

# 0Although there are some useful algorithmic explanations here, I think it may help to add some simple 'real life' reasoning as to why it works this way, which I have found useful when introducing the subject to young newcomers:
#
# With something like 'range(1,10)' confusion can arise from thinking that pair of parameters represents the "start and end".
#
# It is actually start and "stop".
#
# Now, if it were the "end" value then, yes, you might expect that number would be included as the final entry in the sequence. But it is not the "end".
#
# Others mistakenly call that parameter "count" because if you only ever use 'range(n)' then it does, of course, iterate 'n' times. This logic breaks down when you add the start parameter.
#
# So the key point is to remember its name: "stop". That means it is the point at which, when reached, iteration will stop immediately. Not after that point.
#
# So, while "start" does indeed represent the first value to be included, on reaching the "stop" value it 'breaks' rather than continuing to process 'that one as well' before stopping.
#
# One analogy that I have used in explaining this to kids is that, ironically, it is better behaved than kids! It doesn't stop after it supposed to - it stops immediately without finishing what it was doing. (They get this ;) )
#
# Another analogy - when you drive a car you don't pass a stop/yield/'give way' sign and end up with it sitting somewhere next to, or behind, your car. Technically you still haven't reached it when you do stop. It is not included in the 'things you passed on your journey'.
#
# # I hope some of that helps in explaining to Pythonitos/Pythonitas!
