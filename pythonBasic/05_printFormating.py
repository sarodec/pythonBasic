
print("Paul : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))

print('{0} and {1}'.format('Ramu', 'Shamu'))

print('I am {0} ,  from {other}.'.format('User', other ='Pune'))


# Note {<Position>:<number of Digit><type>}
print("UserId :{0:2d}, Average :{1:8.2f}".format(1247, 00.54647))

print("UserId :{1:2d}, Average :{0:8.2f}".format(1.0, 8))

print("User: {a:5d},  Percentage: {p:8.2f}".format(a = 453, p = 59.058))



tab = {'John': 4127, 'Jonny': 4098, 'Jonny': 420, 'Janardhan': 8637678}

# using format() in dictionary
#Note :  Jonny got replaced with the last value
print('User 1 : {0[John]:d}; User 2: {0[Jonny]:d}; '
      'User 3: {0[Janardhan]:d}'.format(tab))

data = dict(fun ="bravio", adj ="and Laptop")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))



cstr = "  I love India  "

# Printing the center aligned
print (cstr.center(40, '#'))

# Printing the left aligned
print (cstr.ljust(40, '-'))

# Printing the right aligned string
print (cstr.rjust(40, '-'))