import random

while True:
    try:
        lowerBound = int(input("Lower Bound: "))
        upperBound = int(input("Upper Bound: "))

        if(lowerBound >= upperBound):
            print("Upper Bound must be greater than Lower Bound. Try again.")
        else:
            break
    except ValueError:
        print("Please enter valid integers.")


number_to_guess = random.randint(int(lowerBound), int(upperBound))
print("You got 7 chances to guess the number I am thinking of. Let's start the game")

chances = 7
number_of_guesses = 0

while number_of_guesses < chances:
    number_of_guesses += 1

    try:
        users_guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter valid integers.")
        number_of_guesses -= 1
        continue

    if(users_guess == number_to_guess):
        print(f"Congratulations! You guessed the number!!")
        break

    elif(users_guess < number_to_guess):
        print('You guessed too small!!')

    else:
        print('You guessed too high!!')

    if(number_of_guesses == chances and users_guess != number_to_guess):
        print(f"Sorry, you used all your guesses. The correct number was {number_to_guess}.")
