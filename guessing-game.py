from random import randint
import json
'''
This program is a random number guessing game. Its should include a seperate file called userscores.json
This file can be created and be left blank.
'''


#PROGRAM FUNCITONS:
def save_scores(score_dictionary):
    #How to write the data to a JSON (This will overwrite the userscores.json each time for now)
    with open("userscores.json", "w+") as outfile:
        json.dump(score_dictionary, outfile, indent=4)
    return

def load_scores():
    #How to read the data into a Dict from a JSON
    try:
        with open("userscores.json") as infile:
            scoreDict = json.load(infile)
        return scoreDict
    except:
        print("The JSON file does not exist. Please create a userscores.json")

def high_scores(username, guess):
    try:
        #How we will check for high scores and also save all information back to the userscores.json
        score = load_scores()
        try:
            if username in score:
                if guess < score[username]:
                    #guess < That users prev guesses
                    print('You got a new High Score!')
                    score[username] = guess
                    #Assigning the user their new "guess count"
                    save_scores(score)
                else:
                    print(f'You did not beat your high score of {score[username]}.')
            else:
                #If the user does not exist in json, create them an assign their guess
                score[username] = guess
                save_scores(score)
        except:
            #Somthing broke when updating the high scores.
            print("Error updating High Score")
        print(score)
        return
    except:
        print("Could not save score or update High Score.")

def greetUser(username):
    try:
        savedscore = load_scores()
        if username in savedscore:
            return username
        else:
            savedscore[username] = 0
        return
    except:
        print("Error Greeting User - Check of JSON file exist.")



randomNumber = randint(1,10)
loop = True
guess = 0
username = input("What is your Username? ")
greetUser(username)

while loop:
    num = int(input("Enter a number: "))
    if num <= 10:
        if num == randomNumber:
            print(f"Congratulation {username.title()}! You picked the correct number")
            loop = False
            guess = guess + 1
            print(f'It took you {guess} guess(es)!')
            high_scores(username.upper(), guess)

        elif num < randomNumber:
            print(f'{num} is less than the Random Number.  Please try again')
            guess = guess + 1
        elif num > randomNumber:
            print(f'{num} is greater than the Random Number. Please try again')
            guess = guess + 1
        else:
            print('You picked a number greater than 10')




