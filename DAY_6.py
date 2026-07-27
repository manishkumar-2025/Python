import builtins

name = "manish"
builtins.print(len(name))
builtins.print(type(len(name)))


def print():
    builtins.print("Kalyani")
    return "hello"


print()
# Calls the function. "Kalyani" is printed because of builtins.print(),
# but the returned value "hello" is ignored since nothing is done with it.

builtins.print(print())
# First, print() is called and returns "hello".
# Then builtins.print() prints that returned value, so both "Kalyani" and "hello" appear.


# ----------------------------------------------
# Huddle Game
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# 1st --- My 1st own idea-
# def jump():
#     turn_left()
#     move()


# def forward():
#     turn_left()
#     turn_left()
#     turn_left()
#     move()


# move()
# jump()
# forward()
# forward()
# jump()
# jump()
# forward()
# forward()
# jump()
# jump()
# forward()
# forward()
# jump()
# jump()
# forward()
# forward()
# jump()
# jump()
# forward()
# forward()
# jump()
# jump()
# forward()
# forward()


# After seeing hint using loop


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def step():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# for one in range(6):
#     step()

# # using while loop
total = 6
# while total>0:
#     step()
#     total -= 1

# 2nd ---   By seeing answer

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def step():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while not at_goal():
#     step()


# # 3rd ---   By myself


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if not front_is_clear():
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#     else:
#         move()


# --- It's easier version by mentor

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def step():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#    if wall_in_front():
#        step()
#    else:
#        move()


# # 4th ---

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if front_is_clear():
#         move()
#         turn_right()
#     elif wall_in_front():
#         turn_left()

#  ---    Worst case this was as too much  = Due to time complexity

# My 2nd try

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front():
#         turn_left()
#     elif front_is_clear():
#         move()


# ---      in loop sequence matters a lot. If we rearrange the sequence order ibn random then its excecution result got in wrong way.


# -------------------------------------------------

# Project : 6 --- Escaping the Maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front():
#         turn_left()
#     elif front_is_clear():
#         move()

# #   ---   This was same as used in 4th   ---
