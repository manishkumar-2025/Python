# # --------
# # BlackJack Game


# # This is my try to make it seems to be very long
# import random

# rnd_int = []
# deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# player_deck = []
# computer_deck = []
# should_continue = True

# while should_continue:
#     ask_1 = input("Are you eager to play BlackJack Game. Type yes or no : ")
#     if ask_1.lower()=="yes":
#         p1 = player_deck.append(random.choice(deck))
#         p2 = player_deck.append(random.choice(deck))
#         c1 = computer_deck.append(random.choice(deck))
#         c2 = computer_deck.append(random.choice(deck))
#         print(player_deck)
#         print(f"[{computer_deck[0]}]")
#         while should_continue:
#             choice = input("Are you willing to continue! - If yes then type 'hit', if no then 'stand' : ")
#             sum_check1 = sum(player_deck)
#             sum_check2 = sum(computer_deck)
#             if choice.lower()=="hit":
#                 p1 = player_deck.append(random.choice(deck))
#                 c1 = computer_deck.append(random.choice(deck))
#                 # if sum_check1>21 or sum_check2>21:
#                 #     if p1==11:
#                 #         player_deck.pop()
#                 #         player_deck.append(1)
#                 #     elif c1==11:
#                 #         computer_deck.pop()
#                 #         computer_deck.append(1)
#                 sum_check1 = sum(player_deck)
#                 sum_check2 = sum(computer_deck)
#                 if sum_check1 > 21:
#                     if p1==11:
#                         player_deck.pop()
#                         player_deck.append(1)
#                     print(f"Player deck card's : {player_deck}")
#                     print(f"Computer deck card's : {computer_deck}")
#                     print("Computer Win! Better Luck next time.-1")
#                     should_continue = False
#                 elif sum_check2 > 21:
#                     print(f"Player deck card's : {player_deck}")
#                     print(f"Computer deck card's : {computer_deck}")
#                     print("You won!-2")
#                     should_continue = False
#                 else:
#                     print(f"Player deck card's : {player_deck}")
#                     print(f"Computer deck card's : {computer_deck[:-1]}") # This will takes all items from list except last one
#             elif choice.lower() == "stand":
#                 if sum_check1 > 21 or sum_check2 > sum_check1:
#                     print(f"Player deck card's : {player_deck}")
#                     print(f"Computer deck card's : {computer_deck}")
#                     print("Computer Win! Better Luck next time.-3")
#                     should_continue = False
#                 elif sum_check1==sum_check2:
#                     print(f"Player deck card's : {player_deck}")
#                     print(f"Computer deck card's : {computer_deck}")
#                     print("Tie-4")
#                     should_continue = False
#                 else:
#                     print(f"Player deck card's : {player_deck}")
#                     print(f"Computer deck card's : {computer_deck}")
#                     print("You Won!-5")
#                 should_continue=False
#             else:
#                 print("Make sure you typed correctly.")
#     elif ask_1.lower()=="no":
#         should_continue = False
#     else:
#         print("Make sure you typed correctly.")

# # while should_continue:
# #     ask_1 = input("Are you eager to play BlackJack Game. Type yes or no : ")
# #     if ask_1.lower()=="yes":
# #         rnd_int1 = random.randint(1,10)
# #         rnd_int2 = random.randint(1,10)
# #         rnd_int3 = random.randint(1,10)
# #         rnd_int4 = random.randint(1,10)
# #         print(f"Your moves points are [{rnd_int1},{rnd_int2}].")
# #         print(f"Computer move is [{rnd_int3}].")
# #         ask_2 = input("Are you want to play again another card? Type yes or no : ")
# #         if ask_2 == "yes":
# #             print(f"Your moves points are [{rnd_int1},{rnd_int2}{rnd_int3}].")
# #         elif ask_2=="no":
# #             print(f"Computer move is [{rnd_int3}{rnd_int4}].")
# #     elif ask_1.lower()=="no":
# #         should_continue = False
# #     else:
# #         print("Make sure you typed correctly.")


# -----------------------

# BlackJack Game by Angela Mam

import random
from string import capwords
from xml.dom.minidom import ElementInfo

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent has BlackJack"
    elif u_score == 0:
        return "Win, You have BlackJack"
    elif u_score>21:
        return "You went over. You lose"
    elif c_score>21:
        return "Opponent went over. You Win"
    elif u_score>c_score:
        return "You Win"
    else:
        return "You lose"
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"Computer's first card : [{computer_cards[0]}]")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'hit' to get another card, type 'stand' to pass : ")
            if user_should_deal=="hit":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score<17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of BlackJack? Type 'yes' or 'no' : ") == "yes":
    play_game()


# Complete day task in ----- 29 to 31 July 2026
