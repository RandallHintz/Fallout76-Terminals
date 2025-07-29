import sys
import string

words = []

def choice(num, wordlen):
    global words
    while(True):
        chosen_word = input("\n[Attempt #" + str(num) + "] Enter chosen word: ")
        if chosen_word in words:
            break
        else:
            print("WARNING: Entered word is not in list. Try again.")
    
    while(True):
        likeness = input("[Attempt #" + str(num) + "] 'Enter the resulting Likeness= ")
        try:
            if (int(likeness) < wordlen):
                break
            elif (int(likeness) == wordlen):
                print("Puzzle solved, congratulations. Exiting app.")
                sys.exit()
            else:
                print("WARNING: Number exceeds word length. Try again.")
        except:
            print("WARNING: Not a number. Try again.")

    return(chosen_word, int(likeness))

#Displays all the remaining potential words
def printlist():
    global words
    print("\nREMAINING WORDS:\n----------------")
    for word in words:
        print(word)

#Determines how many letters match between two words
def compare(word1, word2):
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches

#Remove words from our list that fail the criteria
def prunelist(chosen_word, likeness):
    global words
    removelist = []
    print()
    
    for word in words:
        matches = compare(word, chosen_word)
        if matches != likeness:
            print(chosen_word + " vs " + word + ": likeness=" + str(matches) + " --> removing " + word)
            removelist.append(word)
        else:
            print(chosen_word + " vs " + word + ": likeness=" + str(matches) + " --> keeping " + word)

    for word in removelist:
        words.remove(word)
    printlist()

def main():
    global words
    print("****************************************")
    print("**     Fallout 76 Terminal Hacker     **")
    print("****************************************\n")
    print("Enter list of words (press Enter between each word):")
    print("(press Enter again when done entering words)\n")

    #Prompt for list of words
    word = input()
    wordlen = len(word)
    while(True):
        if (len(word) == 0):
            printlist()
            break
        elif (len(word) != wordlen):
            print("WARNING: Invalid word length. Ignoring entry. Try Again.")
            continue
        words.append(word)
        word = input()
        
    if len(words) == 0:
        print("WARNING: Word list is empty. Exiting.")
        sys.exit()

    print("\nChoose a word and enter it in game. If 'Entry denied', enter the number of correct displayed")

    #Loop for each attempt at guessing the correct word
    attempt = 0
    while(True):
        attempt += 1
        chosen_word,likeness = choice(attempt, wordlen)
        prunelist(chosen_word,likeness)
        if (len(words) == 1):
            print("The answer is: " + words)
            break
        elif(len(words) == 2):
            print("The answer is either: " + words[0] + " or " + words[1])
            break
        elif (len(words) < 1):
            print("ERROR: There are no possible solutions. Check if you entered the data correctly and try again.")
            break
    
main()
