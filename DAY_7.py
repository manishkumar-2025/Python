import random
fruits = ["apple","mango","blackberry","leopard","cosmic","laptop","dhurandhar","tulasi","god","friend"]

random_word = random.choice(fruits)
length = len(random_word)
random_letter = random.choice(random_word)

print("Welcome to the Word-Antakshari!")

# if y == z:
#     print("Right")
# else:
#     print("Wrong")

# for let in x:
#     if x==z:
#         print("Right")
#     else:
#         print("Wrong")

robot = [
"""
    _________
    |       |
            |
            |
            |
            |
            |
            |
____________|
"""
,
"""
    _________
    |       |
   [_]      |
            |
            |
            |
            |
            |
____________|
"""
,
"""
    _________
    |       |
   [_]      |
    |       |
            |
            |
            |
            |
____________|
"""
,
"""
    _________
    |       |
   [_]      |
    |       |
  [___]     |
            |
            |
            |
____________|
"""
,
"""
    _________
    |       |
   [_]      |
    |       |
 /[___]\    |
            |
            |
            |
____________|
"""
,
"""
    _________
    |       |
   [_]      |
    |       |
 /[___]\    |
   / \      |
            |
  !DIE!!    |
____________|
"""
]


p = ""
for c in range(0,length):
    p += "_"
print(p)
# print(random_word)

lives = 6

print(f"Your total lifespan is {lives}")

game_over = False
s = []
while not game_over:
    guess_word = input("Guess a word to step up in to save you robobt's life : ").lower()

    display=""
    for w in random_word:
        if w==guess_word:
            display += w
            s.append(w)
        elif w in s:
            display += w
        else:
            display += "_"
    print(display)

    if guess_word not in random_word:
        lives -= 1
        print(f"You guessed '{guess_word}', that's not in the word. You step down of your robot' life.")
        if lives==0:
            game_over = True
            print("You Lose!😔")

    if "_" not in display:
        game_over = True
        print("You Saved life of your lifeline : Robot😍")

    print(robot[-lives-1])
    print(f"Your robot lifespan left is {lives}")


    #     _________
    #     |       |
    #             |
    #             |
    #             |
    #             |
    #             |
    #             |
    # ____________|


    #     _________
    #     |       |
    #    [_]      |
    #             |
    #             |
    #             |
    #             |
    #             |
    # ____________|


    #     _________
    #     |       |
    #    [_]      |
    #     |       |
    #             |
    #             |
    #             |
    #             |
    # ____________|

    #     _________
    #     |       |
    #    [_]      |
    #     |       |
    #   [___]     |
    #             |
    #             |
    #             |
    # ____________|

    #     _________
    #     |       |
    #    [_]      |
    #     |       |
    #  /[___]\    |
    #             |
    #             |
    #             |
    # ____________|

    #     _________
    #     |       |
    #    [_]      |
    #     |       |
    #  /[___]\    |
    #    / \      |
    #             |
    #   !DIE!!    |
    # ____________|
