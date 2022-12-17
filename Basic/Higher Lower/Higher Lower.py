from game_data import data
import art
import random
import time
from replit import clear

user_continue = 'y'
while user_continue == 'y':
    user_correct = True
    score = 0
    num1 = random.randint(0,len(data)-1)

    while user_correct == True:
        clear()
        print(art.logo)
        higher = ''
        num2 = random.randint(0,len(data)-1)
        person1 = data[num1]
        person2 = data[num2]
        if num1 == num2: #Exception
            num2 = random.randint(0,len(data)-1) #Choose another celeb
        print(f'Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}')
        print(art.vs)
        print(f'Compare B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}')

        user_guess = input('A or B: ').upper()
        if person1['follower_count'] > person2['follower_count']:
            higher = 'A'
            #num1 remains num1
        else:
            higher = 'B'
            num1 = num2

        if user_guess == higher:
            print('Correct!, Next Round!')
            score += 1
            print(f'Current Score {score}')
            time.sleep(2)
            continue
        else:
            print('Wrong!')
            print(f'Your Score is {score}')
            break
    user_continue=input('Wanna go again? type "y", or press enter to exit: ')
