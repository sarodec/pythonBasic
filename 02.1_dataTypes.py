perDayWage = 500
daysOfWorkPerMonth = 31
salary = perDayWage * daysOfWorkPerMonth
print('Salary for month is ', salary)

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)


a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))
print(a, "is of int type", isinstance(a, int))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

a = [5, 10, 15, 20, 25, 30, 35, 40, 74, 56, 58]


print("a[2] = ", a[2])  # Print the element at index 2

print("a[0:3] = ", a[0:3]) # Print the list from index 0 to 3 , 3 exclusion

print("a[5:] = ", a[5:])   # Print the list from index 5 onwards, inclusion 5

t = (5, 'program', 1+3j)
print("t[1] = ", t[1])

print("t[0:3] = ", t[0:3])

# Generates error
#t[0] = 10   # Tuples are immutable

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# s[5] ='d' # Strings are immutable in Python