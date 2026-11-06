import random
number_to_guess = random.randint(1, 100)
user_guess = 0
while user_guess != number_to_guess:
    user_guess = int(input('Enter your guess: '))
    if user_guess < number_to_guess:
        print('Too low! Try again.')
    elif user_guess > number_to_guess:
        print('Too high! Try again.')
    else:
        print('Congratulations! You guessed the correct number.')
