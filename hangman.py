#I used random
import random
#I made list of words
listofwords = ["python", "turtle", "class", "bored" , "school"]
#This randomly picks one of the words out
secretword = random.choice(listofwords)
#my function
def get_guess():
# this is to make the dashes in the beginning and then be able to update them
    dashes = "-" * len(secretword)
# This is to give the number of guesses left
    guesses_left = 10
# I used a while loop to keep repeating until there are no guesses left
    while guesses_left > -1 and dashes != secretword:
        print(dashes)
        print "Guesses left: " + str(guesses_left)
        guess = input("Guess a letter:")
        if len(guess) != 1:
            print ("Your guess must have exactly one character!")
        elif guess==guess.upper():
            print "That letter has to be lowercase."
        elif guess in secretword:
            print ("That letter is in the secret word!")
            dashes = update_dashes(secretword, dashes, guess)
            guesses_left = guesses_left - 1
        else:
            print ("That letter is not in the secret word!")
            guesses_left = guesses_left - 1

    if guesses_left < 0:
        print ("You lose! The secret word is: " + str(secretword))
    else:
        print ("You win! The secret word is: " + str(secretword))
#This is the function to update the dashes
def update_dashes(secret, thedashes, letterguess):
    thedashes
    for i in range(len(secret)):
        if secret[i] == letterguess:
# I make result equal only to where the dash I am going to replace is and put the letter there. Then I also add the rest of the dashes.
            thedashes = thedashes[ :i] + letterguess + thedashes[i+1:]

    return thedashes
get_guess()
