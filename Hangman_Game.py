# Initially created: 6/3/2020

import random
import urllib.request

# Get list of random words from this website, filter words later user picks settings
with urllib.request.urlopen("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain") as response:
    file = response.read().decode()
allWords = file.splitlines()

# Set maximum maxWordLength (just in case the website changes at all)
lengthLimit = 0
for word in allWords:
    if len(word) > lengthLimit:
        lengthLimit = len(word)

# Variables
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


# The game itself
print("Welcome to Hangman!")
while continuePlaying == True:

    # Changing the Difficulty Settings
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
                    if minWordLength == int and minWordLength > lengthLimit:
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
                    if type(maxWordLength) == int and maxWordLength > lengthLimit:
                        print("(The longest word available is only " + str(lengthLimit) + " letters long.)")
            break
        else:
            print("Invalid entry. Please try again.")

    # Generate the answer word based off of these requirements
    words = [word for word in allWords if (word.islower() and len(word) >= minWordLength and len(word) <= maxWordLength)]
    answer = words[random.randrange(len(words))]
    displayAnswer = []
    for i in answer:
        displayAnswer.append("_")
    
    # Final instructions before gameplay
    print("\nPerfect! Guess each letter in the word. Miss " + str(numLives) + " time(s) and you kill " + name + ".")
    #print("You get ??????????? hint(s). Type \"hint\" instead of a guess to request one.")                          # feature to add
    print("Also, enter \"choices\" to see what letters you have already guessed and what is still available.")
    print("If you ever need to see this menu again, enter \"help\" and you will in fact be helped.")
    print("This word has", len(answer), "letters. Good luck!")

    # The actual game begins here
    while numLives > 0:
        print("\n\n" + " ".join(displayAnswer) +"\n")

        # If the round has been completely solved
        if not "_" in displayAnswer:
            print("Congratulations, you saved " + name + "\nGo celebrate with his family :)")
            break

        # Getting user's letter guess / input
        ifNewGuess = False
        while ifNewGuess == False:
            guess = input("Enter your guess (or enter \"help\"): ")

            # If the input isn't in the alphabet 
            if not guess.isalpha():
                print("That doesn't make sense and you know it. Enter someting valid next time.")
                print("Let's try this again, shall we?")

            # If the input is to see what they can still guess
            elif guess == "choices":
                print("you've already guessed:\n    " + str(guessedLetters))
                print("you can still guess:\n    " + str(unguessedLetters))
            
            #elif guess == "hint":                                            # feature to add
            #    print("Will display a hint of some sort")
            #    # formulate and display a hint

            # If the user is asking for help
            elif guess == "help":
                print("\n Guess each letter in the word. If you miss " + str(numLives) + " time(s), you kill " + name + ".")
                #print("You get ??????????? hint(s). Type \"hint\" instead of a guess to request one.")                          # feature to add
                print("Also, enter \"choices\" to see what letters you have already guessed and what is still available.")
                print("If you ever need to see this menu again, enter \"help\" and you will in fact be helped.")
                print("This word has", len(answer), "letters. You got this!")

            # If the input is more than 1 character
            elif len(guess) > 1:
                print("I'm sure you know that just isn't allowed.")
                print("Please try again (and a little harder this time?")

            # Dealing with an actual letter guess
            elif guess in guessedLetters:
                print("You have already guessed this letter. Try something else.")

            else:
                ifNewGuess = True
                guessedLetters.append(guess)
                unguessedLetters.remove(guess)

        # If the guess is correct
        if answer.find(guess) != -1:
            if answer.count(guess) == 1:
                print("\nCorrect! There is 1 " + guess.capitalize() + " in this word.")
            else:
                print("\nCorrect! There are " + str(answer.count(guess)) + " " + guess.capitalize() + "s in this word.")
            updateDisplay(guess)

        # If the guess is incorrect
        else:
            numLives -= 1
            if numLives == 0:
                print("\n\nIncorrect! You have now killed " + name + ".")
                print("The word was " + answer + "!")
                print("Go tell their family and begin mourning.")
                break
            print("\nIncorrect! " + name + " is now one step closer to death...")
            print("Number of incorrect guesses remaining:", numLives)

    # Determine if playing another round
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

# Loop exited, game over
print("\nThanks for playing!\n")