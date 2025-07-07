#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/7/2025
#Description:prompts the user for an integer that the player will try to guess. If the player's guess is higher than the target integer, the program should display "too high" If the user's guess is lower than the target integer, the program should display "too low"
print("Enter the integer for the player to guess.")
numberToGuess = int(input())
guesses = 0
print("Enter your guess.")
guess = numberToGuess + 1
if guesses == 0:
    while int(guess) != numberToGuess:
        guess = int(input())
        guesses += 1
        if guess > numberToGuess :
            print("Too high - try again.")
        if guess < numberToGuess :
            print("Too low - try again.")
if guess == numberToGuess:
    if guesses == 1:
        print("You guessed it in 1 try.")
    else:
        print("You guessed it in " + str(guesses) + " tries.")