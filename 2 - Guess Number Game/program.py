import random

print('------------------------------')
print('    Guess that Number Game')
print('------------------------------')

the_number = random.randint(0, 100)
# Sets an unguessable variable for the guess variable.
guess = -1

while guess != the_number:
    # Next two lines go inside the while loop to avoid infinite loop!
    number_guess = input('Guess the number between 0 - 100: ')
    guess = int(number_guess)

    # Start of the if/elif/else loop
    if guess > the_number:
        print('Too high. Try again.')
    elif guess < the_number:
        print('Too low. Try again.')
    else:
        print('Congratulations. You win!')

# Game over!
print('GAME OVER...')
