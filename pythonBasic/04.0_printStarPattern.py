
'''
Program to print the below pattern

Expected outPut
*
* *
* * *
* * * *
* * * * *
'''

def printPattern(number):
    for counter in range(number):
        for spaceCounter in range(0, counter):
            print("* ", end="")
        print("\r")

printPattern(5)


def printpattern2(number):
    mylist=[]
    for counter in range(0, number):
       mylist.append("* "*counter)
    print("\n".join(mylist))

printpattern2(5)