import io
import time
'''
Author : Chetan Sarode 
Language : Learning Python
Topic : Learn how to use print statement for formatting output   
'''

# Helper function for demonstration
def pass_args(arg1, arg2):
    print("The first argument is : " + str(arg1))
    print("The second argument is : " + str(arg2))
def pass_args2(arg1, arg2):
    print("Print using tuple : " + str(arg1))
    print("Print using tuple : " + str(arg2))

# initialize list
test_list = [4, 5]

print("The original list is : " + str(test_list))
print('---------------------------------------------------')
pass_args(*test_list)
print('---------------------------------------------------')
one,two = tuple(test_list)
pass_args2(one, two)
print('---------------------------------------------------')

test_list = [4, 5, 8, 7, 89, 47, 52, 12, 65, 35, 28, 63, 74, 78]

maxElement = test_list[0]

for element in test_list:
    if element > maxElement:
        maxElement = element

print("Max element is ", maxElement)

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
    sum = sum+val

print("The sum is", sum)