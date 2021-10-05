
'''
Program to print the below pattern

Expected outPut
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

def printPattern(number):
    for counter in range(0, number):
        for inter in range(1, counter+1):
            print(inter, end="")
        print("\r")
printPattern(6)

