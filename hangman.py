import random


def main():
    lives = 5
    # words = ["koulis", "kolotoumpa", "backpack", "sfurodrepano"]
    # choice = random.choice(words)
    choice = list("koulis")
    print(f"H leksh exei {len(choice)} grammata")
    while lives > 0:
        myWord = []
        myLetter = input("Dose Gramma\n")
        if myLetter in choice:
            myWord.append(myLetter)
            print(myWord)
        else:
            lives -= 1
            print(f"Apomenoun {lives} zwes")


main()
