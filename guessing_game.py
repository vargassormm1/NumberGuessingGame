import random

lowerBound = input("Lower Bound: ")
upperBound = input("Upper Bound: ")

number_to_guess = random.randint(int(lowerBound), int(upperBound))

print("You got 7 chances to guess the number I am thinking of. Let's start the game")

chances = 7
number_of_guesses = 0

while(number_of_guesses < chances):

    number_of_guesses += 1
    users_guess = input("Guess a number: ")

    if(int(users_guess) == number_to_guess):
        print(f"Congratulations! You guessed the number!!")
        break

    elif(int(users_guess) < number_to_guess):
        print('You guessed too small!!')

    elif(int(users_guess) > number_to_guess):
        print('You guessed too high!!')

