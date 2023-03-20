import random
import supportFiles.hangman_words as sup
import supportFiles.hangman_arts as art

print(art.logo)

chosen_word = random.choice(sup.word_list)
dead = False
win = False
guess_status = None
guess_word = []
hang_man = 0
for i in range(len(chosen_word)):
    guess_word.append('_')



print(chosen_word)
while dead is not True and win is not True:
    guess = input('please guess a letter from the word \n')

    # if aleady entered:
    if guess in guess_word:
        print('You Have Already Guessed it!! try again with different letter')
    else:
        for letter in range(len(chosen_word)):
            needed = chosen_word[letter]
            if guess.lower == needed.lower:
                guess_status = True
                guess_word[letter] = guess

        if guess_status is True:
            print('Good work your guess is right')
            if '_' not in guess_word:
                print('Congratulations you have completed the word!')
                win = True

        else:
            hang_man += 1
            print('Incorrect, please try again')
            print(art.stages[7- hang_man])
            if hang_man == 7:
                dead = True
                print('Hanged!!!!')
    
        for i in range(len(guess_word)):
            print(guess_word[i],end=' ')
    
        guess_status = None

        



