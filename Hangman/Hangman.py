import random
import Hangman_art
import Hangman_wordlist


stages = Hangman_art.stages
lives = 6
print(Hangman_art.logo)
word_list = Hangman_wordlist.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
blank_list = []


for i in chosen_word:
    blank_list += '_'
print(f"{' '.join(blank_list)}")


while '_' in blank_list:


    guess = input('Guess a letter: ').lower()

    if len(guess) > 1:
      print('One letter at a time!')
      continue

    if guess in blank_list:
      print('Already guessed UwU')
      continue


    if guess not in chosen_word:
        print(f'You guess {guess}, that is not in the word, you lose a life OwO')
        print(stages[lives])
        lives-=1
        if lives == -1:
            print('You Lose!')
            exit()


    for i in range(0,len(chosen_word)):
        if guess == chosen_word[i]:
            blank_list[i] = guess
    print(f"{' '.join(blank_list)}")


print('You Won!')
