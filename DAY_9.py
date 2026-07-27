# # DICTIONARY

# sample_dic = {
#     "Bug" : "An error in a program that prevents the program from running as expected.",
#     "Function" : "A piece of code that you can easily call over and over again."
# }
# print(sample_dic)
# print()

# # Printing it's satement by using their key words
# print(sample_dic["Bug"])

# # Adding Key and its statement in existing dictionary
# sample_dic["Loop"] = "The action of doing something over and over again."
# print(sample_dic)

# empty_dic = {}
# print(empty_dic)
# # # Wipe an existing dictionary
# # sample_dic = {}
# # print(sample_dic)

# # Edit an item in an existing dictionary
# sample_dic["Bug"] = "A moth in your computer."
# print(sample_dic)

# print()

# # Loop through dictionary

# for key in sample_dic:
#     print(key)   # ---- its print only key value not its items in that was defined by key
#     print(sample_dic[key])

# # Grading categorization

# student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

# student_grades = {}

# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

# # Nested Lists and Dictionaries

# capital_dic = {
#     "Maharastra" : "Mumbai",
#     "Karnataka" : "Benguluru",
#     "Jharkhand" : "Ranchi",
#     "Bihar" : "Patna"
# }
# city_dic = {
#     "Jharkhand" : ["Ranchi", "Dumka", "Deoghar", "Bokaro", "Godda", "Dhanbad"],
#     "Bihar" : ["Bhagalpur", "Gaya", "Patna"],
#     "West Bengal" : ["Asansol", "Durgapur", "Kolkata", "Siliguri"]
# }

# print(f"I studied in the {city_dic["Jharkhand"][5]} city.")

# nested_list = ["A", "S", "D", ["q","w","e",["M","p"]]]
# print(f"My name start with the letter '{nested_list[3][3][0]}'.")

# travel_log = {
#     "Bihar": {
#         "total_visits": 12,
#         "cities_visited": ["Bhagalpur", "Banka", "Patna", "Samastipur"],
#     },
#     "West Bengal": {
#         "total_visits": 7,
#         "cities_visited": ["Asansol", "Durgapur", "Kolkata"],
#     },
# }

# print(travel_log["Bihar"]["cities_visited"][0])
# print(travel_log["West Bengal"]["cities_visited"][2])


# ------ Biding Game

print("Let's bid for new brand 'Robotic Watch'!")


bidding_dic = {}

name = input("Enter your name : ")
bid = int(input("Enter your biding price(in $) : "))

bidding_dic[name] = bid


def highest_bidder(bidding_dic):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is '{winner}' with a bid of $'{highest_bid}'.")


should_continue = True
while should_continue:

    ask = input(
        "Any other person who eager to bid in this opportunity. Type 'Yes' or 'No'. "
    )
    if ask.lower() == "no":
        should_continue = False
        highest_bidder(bidding_dic)
    elif ask.lower() not in ("yes", "no"):
        print("Make sure you type correctly.")
    else:
        print("\n"*7)
        name = input("Enter your name : ")
        bid = int(input("Enter your biding price(in $) : "))
    bidding_dic[name] = bid

# print(bidding_dic)

# max = bidding_dic[name]
# print(max)

# direct method
# win = max(bidding_dic, key=bidding_dic.get)
# print(win)




# Complete day task in ----- 27 July 2026
