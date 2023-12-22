#import appropriate modules 
import random
#takes a random five letter word from an online file with all the words in the english language
def have_a_word(l):
    with open('all_english_words.txt') as f:
        all_words = f.read().splitlines()
        return random.choice([i for i in all_words if len(i) == l])

word = have_a_word(5)
#six tries given
i = 0 
while i < 6:
    #creates a list of the characters in the random word
    charlist = list(word)
    #takes in a five letter word, must be five letters
    inputted = input("Input a five letter word: ")
    if len(inputted) != 5:
        print("That's not a five letter word")
        i = i
    else: 
        #creates a list of the characters in the inputted word
        inputtedlist = list(inputted)
        outputlist = [0, 0, 0, 0, 0]
        #compares each letter, if the two letters match, then the output list is set to 2, and the corresponding letter is dropped from the random chosen words list
        #as to not be overwritten 
        for j in range(5):
            if charlist[j] == inputtedlist[j]:
                outputlist[j] = 2
                charlist[j] = ''
        #then, check for if the character isn't in the right spot
        for k in range(len(inputtedlist)):
            if inputted[k] in charlist:
                outputlist[k] = 1
                #as before, as not to let the character be overwritten 
                charlist[charlist.index(inputtedlist[k])] = ''
        #corresponding outputs, green for right spot, yellow for exists but incorrect spot, red for does not exist in the word
        for l in outputlist:
            if l == 2:
                print("\U0001F7E9", end='')
            elif l == 1:
                print("\U0001F7E8", end='')
            else:
                print("\U0001F7E5", end='')
        print("")
        #if the sum of the outputlist is equal to 10, then all characters are correct 
        #set x to the number of tries and i to 7 to exist the loop 
        if sum(outputlist) == 10:
            x = i + 1
            i = 7
        else:
            i += 1
#if i is 6, then the word wasn't guessed, so output the failure message
if i == 6:
    print(f'You Failed, the word was {word}.')
#otherwise, output the congratulatory message and the number of tries it took 
else: 
    print('Congratulations!!')
    if x == 1: 
        print(f'It took you 1 try.')
    else: 
        print(f'It took you {x} tries.')
