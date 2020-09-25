import math
#this functions are used to collect users options 
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def product(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def exponent(num1,num2):
    return pow(num1,num2)

print('HELLO PLEASE INPUT CALCULATIONS BELOW')

#collect input of x
try:
    x = input('Enter first number')
    x = float(x)
except:
    if x != type(float):
        print('wrong input')
        quit()

#User input to enter function needed
ops = input('Enter operation symbol needed:')
opsLst = ['+','-','/','*','^']
if ops not in opsLst:
    print('NOT AN OPERATOR')


#collect input of y
try:
    y = input('Enter second number')
    y = float(x)
except:
    if y != type(float):
        print('wrong input')
        quit()

if ops == '+':
    print(x,'plus',y, 'is',add(x,y))

if ops == '-':
    print(x,'minus',y, 'is',sub(x,y))

if ops == '*':
    print(x,'multiplied',y, 'is',product(x,y))

if ops == '/':
    print(x,'divided by',y, 'is',divide(x,y))

if ops == '^':
    print(x,'to the power of',y, 'is',exponent(x,y))