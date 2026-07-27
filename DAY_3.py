# # CONDITIONAL STATEMENTS
# print("Welcome to check your eligibility for voting in India.")
# age = int(input("What is your age? : "))
# if age >= 18:
#     print("You are eligible to vote in India.")
# else:
#     print("You are not eligible to vote in India.")

# # COMPARISON OPERATORS
# # == : equal to
# # != : not equal to
# # < : less than
# # > : greater than
# # <= : less than or equal to
# # >= : greater than or equal to
# # Important : = is assignment operator, == is for equality operator.

# # CHECK ODD AND EVEN
# n = int(input("Enter a number to check if it is even or odd: "))
# if n%2==0:
#     print(f"{n} is an even number.")
# else:
#     print(f"{n} is an odd number.")

# # NESTED IF-ELSE AND ELIF AND MULTIPLE CONDITIONS AND LOGICAL OPERATORS
# print("Welcome for riding eligibility check of Horse Riding.")
# w = int(input("What is your weight in kg? : "))
# bill = 0
# if w<=100:
#     print("Yes, you are eligible to ride the horse.")
#     age = int(input("What is your age? : "))
#     if age >= 25:
#         if age >=45 and age<=55:
#             bill = 0
#             print("Your ticket price is Rs. 0 for the ride.")
#         else:
#             bill = 500
#             print("Your ticket price is Rs. 500 for the ride.")
#     elif age>=18 and age<25:
#         bill = 400
#         print("Your ticket price is Rs. 400 for the ride.")
#     else:
#         bill = 250
#         print("Your ticket price is Rs. 250 for the ride.")

#     photo = input("Do you want a photo with ticket? Y or N : ")
#     if photo == "Y":
#         bill += 100
#         print(f"Your final bill is Rs. {bill}.")
#     else:
#         print(f"Your final bill is Rs. {bill}.")

# else:
#     print("Sorry, you are not eligible to ride the horse.")

# A and B --- Both conditions should be true for the whole condition to be true.
# A or B --- If any one condition is true, then the whole condition will be true.
# not A --- If A is true, then not A will be false. If A is false, then not A will be true.

# #-----------ASSIGNMENT - 01
# print("Welcome to the Pizza Delivery Service.")
# bill = 0
# size = input("What size of pizza do you want to prefer? S, M or L : ")
# if size == "S":
#     bill += 150
#     print("You have selected Small size pizza. Price is Rs. 150.")
# elif size == "M":
#     bill += 250
#     print("You have selected Medium size pizza. Price is Rs. 250.")
# else:
#     bill += 350
#     print("You have selected Large size pizza. Price is Rs. 350.")

# var1 = input("Do you want to add extra cheese? Y or N : ")
# if var1 == "Y":
#     bill += 50
#     print("Extra cheese added. Price is Rs. 50.")
# var2 = input("Do you want to add pepperoni? Y or N : ")
# if var2 == "Y":
#     if size == "S":
#         bill += 50
#         print("Pepperoni added. Price is Rs. 50.")
#     else:
#         bill += 100
#         print("Pepperoni added. Price is Rs. 100.")
# print(f"Your final bill is Rs. {bill}.")


#---------------------------
#PROJECT 3 : TREASURE ISLAND
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input("You are at mid of the road and it divides into two paths. Which path you want to take? Left or Right : ")
if a == "Left":
    b = input("You have come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across. : ")
    if b == "wait":
        c = input("You arrive at the island unharmed.\nThere is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? : ")
        if c == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
