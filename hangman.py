import random


def main():
    lives = 5
    words = ["koulis", "kolotoumpa", "backpack", "sfurodrepano"]
    word = random.choice(words)
    print(word)
    choice = set(word)
    myWord = []
    guessedWord = []
    for letter in word:
        guessedWord.append("_")
    print(f"The word has {len(word)} letters")
    print(guessedWord)
    while lives > 0:
        myLetter = input("Your Letter: \n")
        if myLetter in choice:
            print("Letter is in word: {0} time(s)".format(word.count(myLetter)))
            for ind in find_indices(word, myLetter):
                guessedWord[ind] = myLetter
            print(guessedWord)
            myWord.append(myLetter)
            if len(myWord) == len(choice):
                print("You won!")
                break
        else:
            lives -= 1
            if lives > 0:
                print("Letter not in word")
                print(f"Lives remaining: {lives} ")
            else:
                print("You lost")
    print("Word was: " + word)


def find_indices(word, letter):
    indices = []
    for idx, value in enumerate(word):
        if value == letter:
            indices.append(idx)
    return indices


main()
