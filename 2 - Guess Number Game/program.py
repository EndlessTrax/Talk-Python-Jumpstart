import random

print('------------------------------')
print('    Guess that Number Game')
print('------------------------------')

the_number = random.randint(0, 100)
# Sets an unguessable variable for the guess variable.
guess = -1
name = input('What is your name? ')

while guess != the_number:
    # Next two lines go inside the while loop to avoid infinite loop!
    number_guess = input('Guess the number between 0 - 100: ')
    guess = int(number_guess)

    # Start of the if/elif/else loop
    if guess > the_number:
        print('Sorry {}, that guess was too HIGH.'.format(name))
    elif guess < the_number:
        print('Sorry {}, that guess was too LOW.'.format(name))
    else:
        print('Congratulations, {}. The number was indeed {}.  You won!'.format(name, the_number))

# Game over!
print('GAME OVER...')
