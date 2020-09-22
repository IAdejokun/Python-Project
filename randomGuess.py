#this is a basic guessing game made by adejokun Ibukunoluwa on September 22,2020
import random

#to accept all number entered into a list
numberEntered = []
count = 0
#function to call user to input
def numInput():
    global userNumber
    userNumber = int(input('guess an integer between 1 to 6: '))
    numberEntered.append(userNumber)
    
#welcome message        
print('welcome to the guessing game,read the mind of the computer lmao')

#game to run ten times

for runTime in range(1,11):
    print("======================\n")
    numInput()
    #computer to generate a random number between 1 to 6
    guess = random.randint(1,6)
    if userNumber < 1 or userNumber > 6:
        print('OUT OF BOUNDS!!..ENTER A NUMBER BETWEEN 1 - 6')
    else:
        if userNumber == guess:
            count+= 1
            print('You are awesome,You really got some super powers in guessing')
            print('You are correct,the answer is also',guess)
            continue
        else:
            print('Wrong guess,Try guessing again')
            print('The right answer is',guess)
            continue
if len(numberEntered) == 10:
    print('End of game')
    print('================')
    print('You got',count,'right')
    if count > 0 and count < 6 :
        print('you can do better')
    else:
        print('You are a really good guesser')
    print('The list of numbers you entered:',numberEntered)
    quit()       




