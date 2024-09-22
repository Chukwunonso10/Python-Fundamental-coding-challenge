"""python code to ask the user for a number and determine whether the number is prime or not
Name: Chukwunonso
For example,to check if 17 is prime, you only need to check if it's divisible by numbers from 1 to 4 (the square root of 17 is approximately 4.12).
Since 17 is not divisible by 2, 3, or 4, it's considered a prime number.
"""

def number_Is_Prime(number):
    #functin that checks for the primality of a number
    if number <= 1:
        return False
    
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:  #checking all numbers of the form 6k ± 1, 
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True
while True:   
    try:
        number = int(input("Enter a primeNumber "))
        if number_Is_Prime(number) == True:
            print("Number is a prime Number ")
        else:
            print("number is not a prime number")
    except ValueError:
        print(" Enter a string pls...")
        
    user = input("do you wish to check again? (yes/No) ")
    if user.lower() != "yes":
        break
       
        


        

