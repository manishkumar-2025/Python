# LOOP
animals = ['Tiger','Lion','Pather','Leopard','Jaguar']
for animal in animals:
    print(animal)
    print(animal+" Jinda Hai")
print(animals)

# SCORE
student_scores = [12,25,65,63,96,45,55,23,13,23,26,98,85,85,75,85]
s_s = student_scores
print(sum(s_s)) #Direct way of sum
sum = 0
for score in s_s:    #Sum using loop
    sum += score
print(sum)

print(max(s_s))
max = s_s[0]
for m_s in s_s:
    if m_s >= max:
        max = m_s
print(max)


# Range function with loop
for num in range (1,7):  #in range it prints 1 to 6, 7 not included
    print(num)
print("")
for num in range(2,12,2):
    print(num)
print("")
sum = 0
for num in (1,101):
    sum+=num
print(sum)

print("")

# Exercise
for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)



# ------------------------------------------------------------
# Project 5 - Password Generator

import random
print("Welcome to the PyPassword Generator!")

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
symbols = list("~!@#$%^&*()_-+={}[]|\\;:'\"<>?/")
numbers = list("1234567890")

let = int(input("Enter the number up to which you want letters in password : "))
sym = int(input("Enter the number up to which you want symbols in password : "))
num = int(input("Enter the number up to which you want numbers in password : "))

# EASY
pswd = ""

for char in range(0,let):
    pswd += random.choice(letters)

for char in range(0,sym):
    pswd += random.choice(symbols)

for char in range(0,num):
    pswd += random.choice(numbers)

print(f"Your Easy password is : {pswd}")

# Advanced

pswd_a = []

for char in range(0,let):
    pswd_a.append(random.choice(letters))

for char in range(0,sym):
    pswd_a.append(random.choice(symbols))

for char in range(0,num):
    pswd_a.append(random.choice(numbers))

random.shuffle(pswd_a)

pswd_l = ""
for char in pswd_a:
    pswd_l += char

print(f"Your Advanced password is : {pswd_l}")
