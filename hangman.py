import random

# Pictures for the hangman stages
HANGMAN_PICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# List of words to choose from
words = 'ant bat bear cat dog duck frog goat lion monkey mouse owl panda rabbit shark snake tiger whale zebra'.split()

# This function picks a random word
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

# This function shows the current state of the game
def displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = ''
    for letter in secretWord:
        if letter in correctLetters:
            blanks += letter
        else:
            blanks += '_'

    for letter in blanks:
        print(letter, end=' ')
    print()

# This function gets the player's guess
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter one letter.')
        elif guess in alreadyGuessed:
            print('You already guessed that letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess

# This function asks if the player wants to play again
def playAgain():
    print('Do you want to play again? (yes or no)')
    answer = input().lower()
    return answer.startswith('y')

# Main game loop
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        # Check if the player has guessed all the letters
        foundAllLetters = True
        for letter in secretWord:
            if letter not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The word was "' + secretWord + '"! You win!')
            gameIsDone = True
    else:
        missedLetters += guess

        # Check if player lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)
            print('You ran out of guesses!')
            print('The word was "' + secretWord + '"')
            gameIsDone = True

    # Ask if player wants to play again
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
