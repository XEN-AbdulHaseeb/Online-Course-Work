import random
word_list = ['baboon','biriyani','aldritch']
chosen_word = random.choice(word_list)
print(chosen_word)
blank_list = []

for i in chosen_word:
    blank_list += '_'
print(blank_list)

while '_' in blank_list:
    guess = input('Guess a letter: ').lower()
    for i in range(0,len(chosen_word)):
        if guess == chosen_word[i]:
            blank_list[i] = guess
    print(blank_list)
