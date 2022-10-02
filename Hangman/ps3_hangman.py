# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "edx_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    myset = set()
    for letter in secretWord:
      myset.add(letter)
    
    for l in lettersGuessed:
      if l in myset:
        continue
      else:
        return False
    return True
        

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    fill = []
    for i in range(len(secretWord)):
      if secretWord[i] in lettersGuessed:
        fill.append(secretWord[i])
      else:
        fill.append('_')
    total = ' '.join(fill)
    return total


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    not_guessed_letters = []
    for letter in alphabet:
      if letter in lettersGuessed:
        continue
      else:
        not_guessed_letters.append(letter)
    final = ''.join(not_guessed_letters)
    return final

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    totalguesses = 8
    lettersGuessed = []
    print()
    print('The secret word contains',len(secretWord), 'letters')
    while totalguesses > 0:
      print(f'You have {totalguesses} guesses left.')
      print('Available letters:',getAvailableLetters(lettersGuessed))
      guess = input('Enter one letter guess per round: ').lower().strip()
      if len(guess) != 1:
        print('Enter One Letter')
        print('-----------------------------------------')
        continue
      if guess in lettersGuessed:
        print('You have already guessed this letter.')
        print('-----------------------------------------')
        continue
      lettersGuessed.append(guess)
      if secretWord == ''.join(getGuessedWord(secretWord, lettersGuessed)):
        print('You got the word! The word was', secretWord)
      if guess in secretWord:
        print('Good guess!')
      else:
        print('oops letter not in my word, try again!')
        totalguesses -= 1
      print(getGuessedWord(secretWord, lettersGuessed))
      print('------------------------------------------')
    if totalguesses == 0:
      print('You ran out of guesses. The word was', secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

