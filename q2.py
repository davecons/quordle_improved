from string import ascii_uppercase as uppers, ascii_lowercase as lowers
from random import choice
from copy import deepcopy

flw2 = []#ranking system based on frequency of words
hits = ['','','','']#store correct answers

def word_score(word):
    if word in flw2:
        return size-flw2.index(word)
    else:
        return size

def best_guess(guess,color_score):#return the best word choice
    shortest = 5
    for pos in range(4):#word position
        for y in range(5):#letter
            if color_score[pos][y] == 'G':
                initials[pos] = [word for word in initials[pos] if word[y] == guess[y]]
            if color_score[pos][y] == 'Y':
                yflag = False
                dups = []
                for z in range(5):
                    if guess[z] == guess[y] and color_score[pos][z] == 'G' and z!= y:#there's a duplicate letter but one is already green
                        dups.append(z)
                        yflag = True
                if yflag:#this letter is elsewhere in the word:
                    initials[pos] = [word for word in initials[pos] if word[y] != guess[y] and y in dups]
                else:
                    initials[pos] = [word for word in initials[pos] if word[y] != guess[y] and guess[y] in word]
            if color_score[pos][y] == 'B':#THIS NOW WORKS
                flag = True
                for z in range(5):
                    if guess[z] == guess[y] and color_score[pos][z] != 'B' and z != y:
                        flag = False#the letter is elsewhere in the word just not at this spot
                if flag:#this letter isn't in the word
                    initials[pos] = [word for word in initials[pos] if guess[y] not in word]
                else:
                    initials[pos] = [word for word in initials[pos] if guess[y] != word[y]]#just delete that spot
    best = 100000
    for a in range(4):#go through the lists and find the shortest one
        if len(initials[a]) < best and len(initials[a]) > 0:
            best = len(initials[a])
            shortest = a
    for x in initials[shortest][0:10]:
        print(shortest,x,len(initials[0]))
    ret = initials[shortest][0]
    for a in range(4):#delete hits so they can be ignored
        if len(initials[a]) == 1:
            initials[a] = []
    return ret#return the first word of the shortest list

with open("words_final.txt","r") as f:
    for row in f:
         flw2.append(row[0:5])

initials = [deepcopy(flw2),deepcopy(flw2),deepcopy(flw2),deepcopy(flw2)]

guess = choice(flw2[0:300])
print("Initial Guess: "+guess)
if input("Do you want a different guess? (y/n): ").lower() == 'y':
    guess = input("What would you like to guess: ")

stored = []
loc = ['Top Left','Top Right','Bottom Left','Bottom Right']
for turns in range(8):
    keepers = []
    colors = [[],[],[],[]]
    for x in range(4):
        if hits[x] == '':
            colors[x] = input("Colors from "+loc[x]+" (G for green, Y for yellow, B for black): ")
        else:
            colors[x] = 'BBBBB'
        if colors[x] == 'GGGGG':
            hits[x] = guess
            initials[x] = []
    stored.append([guess,colors])
    guess = best_guess(guess,colors)
    print("Suggested Guess: "+guess)
    if input("Do you want a different guess? (y/n): ").lower() == 'y':
        guess = input("What would you like to guess: ")
