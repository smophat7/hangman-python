#Created 6/3/2020
#First mini project for Python. Everything else was me just fooling around figuring out how things work.

#This is a basic hangman game. It would be good practice to add a few more features, such as:
    #Helpful hints (you only get 2, and they are things like "There are no more vowels" or "first 8 letters of the
    #   alphabet" or something like that. Maybe use both to just request a free letter)
    #Create Single and Multiplayer options for a random word or a user entered one (maybe give suggestions)

    #Have multiple words instead of just one (create sentences or phrases, but that'd be a whole new website source)

#AMBITIOUS: If I really want to challenge myself, I could create a website or app to play with visuals and crap

import random
import urllib.request

#Get list of random words from this website, will filter words later once user picks settings
with urllib.request.urlopen("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain") as response:
    file = response.read().decode()
allwords = file.splitlines()

#Set maximum maxWordLength (don't know if this website ever change (probably not but it's the principle))
lengthLimit = 0
for word in allwords:
    if len(word) > lengthLimit:
        lengthLimit = len(word)

#initalizing variables (don't think this is a thing in Python, but it is conventional in C++)
name = ""
livesDesired = 0
numLives = 6
minWordLength = 7
maxWordLength = 12
guessedLetters = []
unguessedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guess = ""
difficulty = ""
ifDifficultySet = False
ifCorrectEntry = False
continuePlaying = True
              
def updateDisplay(letter):
    i = 0
    index = -1
    while i < answer.count(letter):
        index = answer.find(letter, index + 1)
        displayAnswer[index] = letter
        i += 1

#The game itself
print("Welcome to Hangman!")
while continuePlaying == True:

    #Changing the Difficulty Settings
    name = input("What would you like to name your hanging man? ")
    while ifDifficultySet == False:
        difficulty = input("What difficulty settings would you like to use? (Enter \"standard\" or \"custom\") ")
        if difficulty == "standard":
            livesDesired = 6
            numLives = livesDesired
            minWordLength = 7
            maxWordLength = 12
            break
        elif difficulty == "custom":
            while ifCorrectEntry == False:
                livesDesired = input("How many incorrect guesses would you like to allow? ")
                try:
                    livesDesired = int(livesDesired)
                except: pass
                if type(livesDesired) == int and livesDesired >= 0:
                    numLives = livesDesired
                    break
                else:
                    print("Invalid entry. Please try again.")
            while ifCorrectEntry == False:
                minWordLength = input("What would you like the minimum word length to be? ")
                try:
                    minWordLength = int(minWordLength)
                except: pass
                if type(minWordLength) == int and minWordLength <= lengthLimit:
                    break
                else:
                    print("Invalid entry. Please try again.")
                    if minWordLength > lengthLimit:
                        print("(The longest word available is only " + str(lengthLimit) + " letters long.)\n")
            while ifCorrectEntry == False:
                maxWordLength = input("What would you like the maximum word length to be? ")
                try:
                    maxWordLength = int(maxWordLength)
                except: pass
                if type(maxWordLength) == int and maxWordLength >= minWordLength and maxWordLength <= lengthLimit:
                    break
                else:
                    print("Invalid entry. Please try again.")
                    if maxWordLength > lengthLimit:
                        print("(The longest word available is only " + str(lengthLimit) + " letters long.)")
            break
        else:
            print("Invalid entry. Please try again.")

    #Generate answer word based off of these requirements
    words = [word for word in allwords if (word.islower() and len(word) >= minWordLength and len(word) <= maxWordLength)]
    answer = words[random.randrange(len(words))]
    displayAnswer = []
    for i in answer:
        displayAnswer.append("_")
    
    #Final instructions before gameplay
    print("\nPerfect! Guess each letter in the word. Miss " + str(numLives) + " time(s) and you kill " + name + ".")
    print("You get ??????????? hint(s). Type \"hint\" instead of a guess to request one.")           #finish this one up
    print("Also, enter \"choices\" to see what letters you have already guessed and what is still available")
    print("This word has", len(answer), "letters. Good luck!")

    #The actual game begins here
    while numLives > 0:
        print("\n\n" + " ".join(displayAnswer) +"\n")

        #If the round has been completely solved
        if not "_" in displayAnswer:
            print("Congratulations, you saved " + name + "\nGo celebrate with his family :)")
            break

        #Getting user's letter guess / input
        ifNewGuess = False
        while ifNewGuess == False:
            guess = input("Enter your guess: ")

            #If the input is a "hint" or "show guesses" type request
            if guess == "hint":
                print("Will display a hint of some sort")                               #DELETE ME and finish this
                #formulate and display a hint
            elif guess == "choices":
                print("You've already guessed:\n    " + str(guessedLetters))
                print("You can still guess:\n    " + str(unguessedLetters))
            
            #Dealing with an actual letter guess
            elif guess in guessedLetters:
                print("You have already guessed this letter. Try something else.")
            else:
                ifNewGuess = True
                guessedLetters.append(guess)
                unguessedLetters.remove(guess)

        #If the guess is correct
        if answer.find(guess) != -1:
            if answer.count(guess) == 1:
                print("\nCorrect! There is 1 " + guess.capitalize() + " in this word.")
            else:
                print("\nCorrect! There are " + str(answer.count(guess)) + " " + guess.capitalize() + "s in this word.")
            updateDisplay(guess)

        #If the guess is incorrect
        else:
            numLives -= 1
            if numLives == 0:
                print("\n\nIncorrect! You have now killed " + name + ".")
                print("The word was " + answer + "!")
                print("Go tell their family and begin mourning.")
                break
            print("\nIncorrect! " + name + " is now one step closer to death...")
            print("Number of incorrect guesses remaining:", numLives)

    #Determine if playing another round
    print("\nThanks for playing!\n")
    playAgain = input("Would you like to play again? (Enter \"yes\" or \"no\") ")
    if playAgain == "yes":
        continuePlaying = True
        guessedLetters = []
        unguessedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        changeDifficulty = input("Would you like to adjust the difficulty settings? (Enter \"yes\" or \"no\") ")
        if changeDifficulty == "yes":
            ifDifficultySet = False
        else:
            ifDifficultySet = True
            numLives = livesDesired
        print("\n\nWelcome back!")
    else:
        print("Well fine, then. Hope you had a good time.")
        continuePlaying = False

#Loop exited, game over
print("\nThanks for playing!\n")