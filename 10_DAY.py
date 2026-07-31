# # First letter of word capatalization

# def format_name(f_name,l_name):
#     print(f_name.title() +" "+ l_name.title())
#     return f"{f_name} {l_name}"               # after this function is called off
# format_name("angElia", "yu")
# print(format_name("anGela", "yU"))

# def func_1(text):
#     return text+text

# def func_2(text):
#     return text.title()

# print(func_2(func_1("helLo")))

# def data(age,blood_group):
#     if age=="" or blood_group=="" :
#         return "Enter valid number"
#     return f"{age} and {blood_group}"

# print(data(int(input("Enter")),(input("Enter"))))

# # Leap year


# def is_leap_year(year):
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False


# print(is_leap_year(int(input("Enter any year to check leap year : "))))


# --------------

# PRoject 10 ---- The Calculator

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def multi(n1, n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
operations = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div
}
n1 = int(input("Enter first number : "))

print(operations)

should_continue = True

# while should_continue:
#     n1 = int(input("Enter first number : "))
#     n2 = int(input("Enter second number : "))
#     choice = input("Are you willing to continue! - If yes then type 'y', if no then 'n' : ")
#     print(operations)
#     op_ask = input("Type operations you want : ")
#     if choice=="y":
#         if op_ask=="+":
#             print(operations["+"](n1,n2))
#         elif op_ask=="-":
#             print(operations["-"](n1,n2))
#         elif op_ask=="*":
#             print(operations["*"](n1,n2))
#         elif op_ask=="/":
#             print(operations["/"](n1,n2))
#         else:
#             print("Make sure you typed correctly.")
#     elif choice=="n":
#         should_continue = False


while should_continue:
    op_ask = input("Type operations you want : ")
    n2 = int(input("Enter other number  : "))
    choice = input("Are you willing to continue! - If yes then type 'y', if no then 'n' : ")
    if choice=="y":
        if op_ask=="+":
            print(operations["+"](n1,n2))
        elif op_ask=="-":
            print(operations["-"](n1,n2))
        elif op_ask=="*":
            print(operations["*"](n1,n2))
        elif op_ask=="/":
            print(operations["/"](n1,n2))
        else:
            print("Make sure you typed correctly.")
    elif choice=="n":
        should_continue = False
