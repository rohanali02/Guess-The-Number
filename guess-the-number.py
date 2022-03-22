import random

num = int(input('Enter Number Range: '))
n1 = random.randint(0, num)
n = n1

turn = 9
while turn >= 1:
    turn = turn - 1
    guessnum = int(input("Enter the Number: "))
    if guessnum < n:
        print("Your Number is too low\n")
        print("You have " + str(turn) + " turns left")
    elif guessnum > n:
        print("Your Number is too High\n")
        print("You have " + str(turn) + " turns left")
    else:
        print("\nYour Number is Correct You've Won the Game.")
        print("You have Guess The Number is Just " + str(9 - turn) + " turns")
        break
if turn <= 0:
    print("\nGame Over.")
    print(str(turn) + " Guesses left")
    print(str(n) + " Was the right number")
