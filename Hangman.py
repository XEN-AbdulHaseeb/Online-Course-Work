import random
word_list = ['baboon','biriyani','aldritch']
chosen_word = random.choice(word_list)
#print(chosen_word)
guess = input('Guess a letter: ').lower()

for i in range(0,len(chosen_word)):
    if guess == chosen_word[i]:
        print('Right')
    else:
        print('Wrong')
