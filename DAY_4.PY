# # RANDOM MODULE
# import random

# random_integer = random.randint(1, 25)
# print(random_integer)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# # TOSS
# a = random.randint(0, 1)
# if a == 0:
#     print("Heads")
# else:
#     print("Tails")

# # LIST
# states = ["Sikkim","Nagaland","Arunachal Pradesh","Mizoram","Tripura","Meghalaya"]
# print(states)
# states.append("Assam")
# states.remove("Sikkim")
# states[0] = "Sikkim"
# states.extend(["Assam","Manipur"])
# print(states)

# #Who will pay the bill?
# import random
# friends = ["Riya","Rohit","Ritik","Reshma","Rohini","Roshan"]
# # option-1
# print(random.choice(friends))
# # option-2
# option = random.randint(0,5)
# print(friends[option])


# -----------------------------------------------

# Project 4 : Rock-Paper-Scissors

print("""Welcome to Game Rock-Paper-Scissors!
Best of luck!""")
do = int(input("It's play time!..... Choose 1 for Rock, 2 for Paper and 3 for Scissors : "))

if do == 1 or do == 2 or do == 3:

#Another way
#if do in (1,2,3):

# print("""

#     _____)
# ----_________)
#     _________)
#     _________)
# ----_________)



#     _____)
# ----_______________)
#     _______________)
#     _________)
# ----_________)



#     ______)
# ----________________)
#     ________________)
#     ________________)
# ----________________)

# """)

    if do == 1:
        print(""" Rock :

        _____)
    ----_________)
        _________)
        _________)
    ----_________)

    """)

    elif do == 3:
        print(""" Scissor :

        _____)
    ----_______________)
        _______________)
        _________)
    ----_________)

    """)

    else:
        print(""" Paper :

        ______)
    ----________________)
        ________________)
        ________________)
    ----________________)

    """)

    import random
    rnd_int = random.randint(1,3)
    print("Computer's choose : ")
    if rnd_int == 1:
        print(""" Rock :

        _____)
    ----_________)
        _________)
        _________)
    ----_________)

    """)

    elif rnd_int == 3:
        print(""" Scissor :

        _____)
    ----_______________)
        _______________)
        _________)
    ----_________)

    """)

    else:
        print(""" Paper :

        ______)
    ----________________)
        ________________)
        ________________)
    ----________________)

    """)

    if rnd_int == do:
        print("DRAW")
    elif do==1 and rnd_int==2 or do==2 and rnd_int==3 or do==3 and rnd_int==1:
        print("YOU - LOSE!")
    else:
        print("YOU - WIN!")

else:
    print("Make sure you enter valid number i.e., 1, 2 or 3.")
