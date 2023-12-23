#import appropriate modules 
import random
#takes a random word from an online file with all the words in the english language
with open('all_english_words.txt') as f:
    all_words = f.read().splitlines()
word = random.choice(all_words)
print(word)
#six tries given
i = 0 
while i < 6:
    #creates a list of the characters in the random word
    charlist = list(word)
    #takes in a word
    inputted = input("Input a word: ")
    #creates a list of the characters in the inputted word
    inputtedlist = list(inputted)
    #makes an output list of 0 of length of the word 
    outputlist = [0]*len(inputted)
    #compares each letter, if the two letters match, then the output list is set to 2, and the corresponding letter is dropped from the random chosen words list
    #as to not be overwritten 
    #takes the minimum of the two lengths, as not to check for indexes that don't exist 
    for j in range(min(len(charlist),len(inputtedlist))):
        if charlist[j] == inputtedlist[j]:
            outputlist[j] = 2
            charlist[j] = ''
    #then, check for if the character isn't in the right spot, if so set output list to 1 and drop the corresponding letter 
    for k in range(len(inputtedlist)):
        #need to make sure that the item isn't already in the right spot, so check if outputlist at that location is equal to 2 
        if inputted[k] in charlist and outputlist[k] != 2:
            outputlist[k] = 1
            #as before, as not to let the character be overwritten 
            charlist[charlist.index(inputtedlist[k])] = ' '
    #corresponding outputs, green for right spot, yellow for exists but incorrect spot, red for does not exist in the word
    for l in outputlist:
        if l == 2:
            print("\U0001F7E9", end='')
        elif l == 1:
            print("\U0001F7E8", end='')
        else:
            print("\U0001F7E5", end='')
    print("")
    if len(inputted) < len(word):
        print("Not enough letters")
    elif len(inputted) > len(word):
        print("Too many letters")
    #if the sum of the outputlist is equal to 2 times the length of the outputlist, then all characters are correct 
    #set x to the number of tries and i to 7 to exist the loop 
    if sum(outputlist) == 2*len(outputlist):
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
