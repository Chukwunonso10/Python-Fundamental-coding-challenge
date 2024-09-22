"""Name: Chukwunonso kuzue  
   a guessing game 
"""
import random

def guess_function(user_input):
    """function that prints out a guess result"""

    random_number = random.randint(1, 9)
    #print(random_number)
    if user_input < 1 or user_input > 9:
        print("enter a value between (1 and 9) ")
    elif user_input == random_number:
        print("you got it exactly right! ")
    elif user_input < random_number:
        print("you guessed too low ")
    else:
        print("you guessed too high ")


count = 0
while True:
    try:
        user_input = (input("Enter a  number (1 - 9) "))
        if user_input.lower() == 'exit':
            print("Exiting... ")
            print(f"you have {count} guess counts")
            break
        user_input = int(user_input)
        guess_function(user_input)
        count = count + 1
        
    except:
        print("valueError, enter a valid number")
