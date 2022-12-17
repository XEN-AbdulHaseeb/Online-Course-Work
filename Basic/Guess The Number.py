import random
from replit import clear
user_continue = 'y'
while user_continue == 'y':
    clear()
    num = random.randint(0,101)
    print(num)
    attempts = 10
    difficulty = 'easy'
    print('Guess a number between 0 and 100!')
    difficulty = input('Press enter for 10 attempts or type "hard" for 5 attempts: ')
    if difficulty == 'hard':
        attempts = 5

    while attempts > 0:
        print(f'You have {attempts} attempts left\n')
        guess_num = int(input('Make a guess: '))

        if guess_num == num:
            print('Correct! You Win!!')
            break

        elif guess_num < num:
            print('Too Low!')
            attempts -= 1
            continue

        else:
            print('Too High')
            attempts -= 1
            continue

    print('Game Over')
    user_continue = input('Want to play again? type "y" or press enter to exit')

