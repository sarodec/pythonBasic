
'''
Read multiple input and create list  and cast it to int
'''

x, y = [int(x) for x in input("Enter two value: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

x, y = [int(x) for x in input("Enter two value: ").split(",")]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

"""x = [int[x] for x in input("Enter list of values: ").split()]
print("List : ", x)
print()
"""