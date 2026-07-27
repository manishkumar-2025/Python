# # Subscripting
# print("Hello"[1])

# # String
# print("123" + "456")

# # Integer
# print(123 + 456)

# # Large Integer
# print(123_456_789)

# # Float
# print(123.4 + 456.7)

# # Boolean
# print(True)
# print(False)

# # Printing another way
# import sys

# sys.stdout.write("Hello")
# sys.stdout.write("World\n") #Unlike print, sys.stdout.write does not add a new line at the end of the output.

# # len(123) # This will throw an error because len() expects a sequence (like a string, list, etc.), not an integer.

# a = len("What's going on!")
# b = type("What's going on!")
# print(a,"and", b)
# print(type("Learning"), type(123), type(123.4), type(True))

# # TYPE CONVERSION
# print(int("456") + int("789"))

# # TYPE CHECKING
# # print("Number of your letters in your name is : ")
# # print(len(input("Enter your name: "))) #I do mistake

# # name = input("Enter your name: ")
# # print("Number of your letters in your name is : " + len(name)))
# # Again mistake - SyntaxError

# print(type(input("Enter your name: ")))
# print(type(len(input("Enter your name: "))))

# #So, we need to change the type of len() to str() to avoid the error.

# #CORRECT ONE
# print("Number of your letters in your name is : " + str(len(input("Enter your name: "))))

# MATHEMATICAL OPERATORS
print(35 + 95)  # addition
print(7 - 44)  # subtraction
print(3 * 29)  # multiplication
print(17 / 3)  # division
print(17 // 3)  # floor division
print(20 % 3)  # modulo
print(2**3)  # exponentiation

# PEMDASLR - Parentheses, Exponents, Multiplication and Division, Addition and Subtraction, Left to Right
print(5 + 59 - 5 // 2 % 3**6 * 25 / 5 + (56 - 23))

# DATA MANIPULATION
bmi = 60 / 1.7**2
print(bmi)
print(int(bmi))  # type conversion
print(round(bmi))  # round off
print(round(bmi, 2))  # round off to 2 decimal places

#ASSIGNMENT OPERATOR
age = 18
print(age)
age += 1  # -= or *= or /= or //= or **= or %= or &= or |= or ^= or >>= or <<=
print(age)

#F-STRING
score = 50
subject = "Maths"
print("Your score in " + subject + " is " + str(score) + ".") # Concatenation
print(f"Your score in {subject} is {score}.") # F-string

#---------------------------------
#Project 2: TIP CALCULATOR

print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? : $"))
tip = int(input("How much do you want to pay for the tip? 10,20,30 or 40 : "))
split = int(input("How many people to split the bill? : "))
print(f"Each person should pay: ${(bill+tip)/split}")

