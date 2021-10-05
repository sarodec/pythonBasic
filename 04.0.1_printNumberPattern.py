
'''
Program to print the below pattern

Expected outPut
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''

def printPattern(number):
    counter = 1
    for numberRange in range(0, number):
        for inter in range(0, numberRange):
            print(counter, end=" ")
            counter = counter+1
        print("\r")
printPattern(15)

