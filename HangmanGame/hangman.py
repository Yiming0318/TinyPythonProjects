'''
Yiming Ge
CS 5001, Fall 2021
HW04 -- Problem 2

This is a program that implement a version of the game Hangman:
The user will  attempt to guess a secret word one letter at a time
and play three rounds against the computer.
'''


def underscore_word(word):
    '''
        Function -- underscore_word
            Transfer the word to secret word with underscore "_"
        Parameters:
            word -- the word that user needs to guess
        Return:
            Return the underscores which has the same length as the given word
    '''
    return len(word) * "_"


def complete_word(guess, word, secret_word):
    '''
        Function -- complete_word
            Replace secret word's underscore with
            the right letter that user guessed
        Parameters:
            guess -- the letter that user guessed
            word -- the word that user needs to guess
            secret_word -- the secre word with underscores
        Return:
            Return the secret word which has right letters user guessed
    '''
    # convert secret_word to a list
    # since string object does not support item assignment
    secret_word = list(secret_word)
    # create an index_list to collect all the indices (location) that
    # the real letter in the word is equal to the guessing letter (value)
    index_list = [i for i, letter in enumerate(word) if letter == guess]
    # based on the indices in the index_list,
    # replace the underscore with the right letter user guessed
    for index in index_list:
        secret_word[index] = guess
    # convert list to string
    return "".join(secret_word)


def check_correctness(correctness, word):
    '''
        Function -- check_correctness
            determine whether the user wins the game
        Parameters:
            correctness -- Ture or False (boolean), True means the user wins
                        False menas the user loses
            word -- the word that the user needs to guess
        Return:
            Return 1 & "You win" if the user correctly guesses the word
            otherwise return 0 & (the user loses)
    '''
    if correctness is True:   # user correctly guesses the word
        return 1, "You win!"    # 1 means 1 victory
    else:   # user loses
        return 0, "You lose! The word was {}".format(word)  # 0 means 0 victory


def main():
    # three words for three rounds
    # the word that user needs to guess in the first round
    WORD_ONE = "APPLE"
    # the word that user needs to guess in the second round
    WORD_TWO = "OBVIOUS"
    # the word that user needs to guess in the third round
    WORD_THREE = "XYLOPHONE"
    # create a victory list to collect the outcome of each round
    victory_list = []
    # create a list having all three words that user
    # needs to guess in three rounds
    word_list = [WORD_ONE, WORD_TWO, WORD_THREE]
    # iterate over the word_list
    for word in word_list:
        # set defaults
        correctness = False
        TOTAL_TRIES = 6    # 6 total tries
        remaining_tries = TOTAL_TRIES
        secret_word = underscore_word(word)
        print(secret_word)
        # create a list to collect letters that the user guessed
        guessed_list = []
        while not correctness and remaining_tries > 0:
            guess = input("Enter a letter or word: ").upper()
            if len(guess) == 1:     # user enters a letter
                # user has already guessed the letter
                if guess in guessed_list:
                    print("You've already guessed that letter!")
                elif guess in word:
                    # since the guess is in the word (right letter)
                    # use function complete_word to
                    # reaveal the right letter in the secret word
                    secret_word = complete_word(guess, word, secret_word)
                    # check whether the revealed word is the answer
                    # eg: 'a', 'p', 'l', 'e' for 'apple', you win
                    if secret_word == word:
                        correctness = True
                        break  # Just print out "You win!"
                    # add the letter to guessed_list
                    guessed_list.append(guess)
                    remaining_tries -= 1  # spend 1 try
                # wrong letter and user has not already guessed this letter
                else:
                    # add the letter to guessed_list
                    guessed_list.append(guess)
                    remaining_tries -= 1  # spend 1 try
                # When user does not have any tries,
                # directly print "You lose! The word was xxxx"
                if remaining_tries == 0:
                    break
                print(secret_word)
                print("Your guesses so far: {}".format("".join(guessed_list)))
            elif len(guess) == len(word):   # user enters a word
                if guess == word:
                    # user correctly guesses the word
                    # let correctness be True
                    # make while loop end
                    correctness = True
                else:  # user dose not enter the correct answer
                    print("Incorrect word guess")
            else:   # user enters invalid word
                print("Invalid word guess")
        victory, conclusion = check_correctness(correctness, word)
        print(conclusion)
        # add the outcome to the victory list
        victory_list.append(victory)
    # sum the three rounds outcome (victory or not)
    print("You won {} out of 3".format(sum(victory_list)))


if __name__ == "__main__":
    main()
