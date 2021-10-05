
'''
Program to print the below pattern

Expected outPut
     *
   * * *
  * * * *
 * * * * *
* * * * * *

'''

def printPattern(number):
    for counter in range(0, number):                 # Number of rows to be print
        for inter in range(0, number-counter):        # print spaces , on each row spaces will be number of rows- current row count
            print(" ", end="")
        for inter1 in range(0, counter+1):
            print("* ", end="")                       # print the * with space
        print("\r")
printPattern(6)

