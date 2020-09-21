#this mini game was created on the 21st of september 2020 

name = []

#function for registering ones name 
def inputName():
    collect = []
    for i in range(1):
        collect = input('Enter your name to register')
    #appends one name to the name list 
    name.append(collect)
    game()

def game():
    EnterName = input('Enter name registered: ')
#verification to see if name entered is in list     
    if EnterName in name:
        print('Hello welcome to the game\n')
    
        print('(1) Roses are ______')
        print("(2) Ibukun's favourite musician is ______")
        print('(3) Whats more important ______')
        
        enterAnswers()
    else:
        print('Please register')
        inputName()
    
    
#function to prompt user for each answer and to verify each answer
def enterAnswers():
    result = 0
    try:
        firstAnswer = input("Enter answer to number 1")
        
        firstAnswer = firstAnswer.lower()
        if firstAnswer != 'red':
            print('Wow,That was really easy,you got that wrong,Answer is Red')
        else:
            print("You got that right,You're a genius")
            result+=1  
            
        secondAnswer = input("Enter answer to number 2")
        
        secondAnswer = secondAnswer.lower()
        if secondAnswer != 'the weeknd':
            print('Wow,That was really easy,you got that wrong,Answer is The Weeknd')
        else:
            print("You got that right,You're a genius")
            result+=1    
            
        thirdAnswer = input("Enter answer to number 3")
        
        thirdAnswer = thirdAnswer.lower()
        if thirdAnswer != 'python':
            print('Wow,That was really easy,you got that wrong,Answer is Python')
        else:
            print("You got that right,You're a genius")
            result+=1
        
        if result == 0:
            print("That's terrible") 
        elif result == 1:
            print('you can do better')
        elif result == 2:
            print('You are excellent')
        else:
            print('You are Great')
        
        print('You got',result)  
        
    except:
        print('Invalid input')
        
#function call to activate the whole game
inputName()
