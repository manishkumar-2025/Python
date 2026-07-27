# def greet():
#     print("Are you wiiling to create a new universe?")
#     print("You are not just mad actually.....")
# greet()

# # Function that allows input

# def mad(name):
#     print(f"You({name}) are the craziest mad of the galaxy.")
# mad("RR")

# # here - name is "Parameter" and RR is "Argument"

# def user_info(name, location):
#     print(f"Hello {name}!")
#     print(f"You are live in {location}.")
# user_info("Angela", "UK")
# user_info(location="Switzerland", name="Yu")

# # Love Calculator

# def calculate_love_score(name_1, name_2):
#     n1 = name_1.lower()
#     n2 = name_2.lower()
#     n3 = n1 + n2
#     count1 = 0
#     count2 = 0
#     for i in n3:
#         if "t" == i or "r" == i or "u" == i or "e" == i:
#             count1 += 1
#         if "l" == i or "o" == i or "v" == i or "e" == i:
#             count2 += 1

#     print(count1 * 10 + count2)


# calculate_love_score("Ritik Taranum", "Reshma Majee")


# # Caesar Cipher Game
# # It's written by me without seeing solution

# inst = input("Write 'encode' to encrpt or 'decode' to decrypt of your message : ").lower()
# if inst=="encode":
#     msg = input("Enter your message for encryption : ")
#     shift = int(input("Enter shift number for encrption of message : "))
# elif inst=="decode":
#     msg = input("Enter your message for decryption : ")
#     shift = int(input("Enter shift number for decryption of message : "))

# alpha = list("abcdefghijklmnopqrstuvwxyz")

# def encrypt(msg1, shift1):
#     text1 = ""
#     for i in msg1:
#         ind = alpha.index(i) + shift1
#         if ind >= 26:  # best way to do by replacing 26 by len(alpha)
#             ind -= 26
#         text1 += alpha[ind]
#     print(f"The encrypted message is {text1}")

# def decrypt(msg2, shift2):
#     text2 = ""
#     for i in msg2:
#         ind = alpha.index(i) - shift2
#         # if ind < 0:
#         #     ind += 26  # best way to do by replacing 26 by len(alpha)

#         # another method by Instructor
#         ind %= len(alpha)

#         text2 += alpha[ind]
#     print(f"The encrypted message is {text2}")

# if inst=="encode":
#     encrypt(msg,shift)
# elif inst=="decode":
#     decrypt(msg,shift)
# else:
#     print("Sorry! Make sure you typed correct spelling of 'encode' and 'decode'.")


# CBackup

# def caesar():
#     inst = input(
#         "Write 'encode' to encrpt or 'decode' to decrypt of your message : ").lower()
#     # if inst not in "encode" or "decode":  # The second part, "decode", is a non-empty string, which is always considered True in a boolean context.
# if inst not in ("encode", "decode"):
#     print("Sorry! Make sure you typed correct spelling of 'encode' and 'decode'.")

#     if inst == "encode":
#         msg = input("Enter your message for encryption : ")
#         shift = int(input("Enter shift number for encrption of message : "))
#     elif inst == "decode":
#         msg = input("Enter your message for decryption : ")
#         shift = int(input("Enter shift number for decryption of message : "))

#     alpha = list("abcdefghijklmnopqrstuvwxyz")


#     def encrypt(msg1, shift1):
#         text1 = ""
#         for i in msg1:
#             ind = alpha.index(i) + shift1
#             if ind >= 26:  # best way to do by replacing 26 by len(alpha)
#                 ind -= 26
#             text1 += alpha[ind]
#         print(f"The encrypted message is {text1}")

#     def decrypt(msg2, shift2):
#         text2 = ""
#         for i in msg2:
#             ind = alpha.index(i) - shift2
#             # if ind < 0:
#             #     ind += 26  # best way to do by replacing 26 by len(alpha)

#             # another method by Instructor
#             ind %= len(alpha)

#             text2 += alpha[ind]
#         print(f"The encrypted message is {text2}")

#     if inst == "encode":
#         encrypt(msg, shift)
#     elif inst == "decode":
#         decrypt(msg, shift)
# caesar()


# In one functioon ------ Caesar Cipher game


def caesar(msg3, shift3, inst3):
    text3 = ""
    if inst3=="decode":
        shift3 *= -1
    for i in msg3:
        if i not in alpha:
            text3 += i
        else:
            ind = alpha.index(i) + shift3
            ind %= len(alpha)
            text3 += alpha[ind]
    print(f"The {inst3}d message is {text3}")

should_continue = True

while should_continue:
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    inst = input("Write 'encode' to encrpt or 'decode' to decrypt of your message : ").lower()

    if inst == "encode":
        msg = input("Enter your message for encryption : ")
        shift = int(input("Enter shift number for encrption of message : "))
    elif inst == "decode":
        msg = input("Enter your message for decryption : ")
        shift = int(input("Enter shift number for decryption of message : "))
    else:
        print("Sorry! Make sure you typed correct spelling of 'encode' and 'decode'.")
        should_continue = False


    if inst == "encode" or inst == "decode":
        caesar(msg, shift, inst)

    if inst == "encode" or inst == "decode":
        again = input("Type 'Yes' if you want to go agin. Otherwise type 'No'.\n").lower()
        if again=="no":
            print("You did wrong! Plz recontinue the game.")
            should_continue = False


# d
