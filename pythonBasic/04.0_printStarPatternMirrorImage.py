
'''
Program to print the below pattern

Expected outPut
*****
****
***
**
*
     *
    **
   ***
  ****
 *****
'''

def printPattern(number):
    for counter in (range(0, number)):

        for outerCouter in range(0, number):
            print(end="*")

        number = number-1
        print("")

printPattern(5)

def printPattern2(number):
    numberCounter = number
    for counter in (range(0, number)):

        for outerCouter in range(0, numberCounter):
            print(end=" ")

        numberCounter = numberCounter-1

        for innerCounter in (range(0,counter+1)):
            print("*", end="")

        print("\r")
printPattern2(5)