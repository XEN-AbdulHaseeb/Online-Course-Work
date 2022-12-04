import random
word_list = ['baboon','biriyani','aldritch']
chosen_index = random.randint(0,2)
chosen_word = word_list[chosen_index]
print(chosen_word)
guess = input('Guess a letter: ')

for i in range(0,len(chosen_word)):
    if guess == chosen_word[i]:
        print('Right')
    else:
        print('Wrong')
