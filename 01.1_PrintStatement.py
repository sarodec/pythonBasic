import io
import time
'''
Author : Chetan Sarode 
Language : Learning Python
Topic : Learn how to use print statement for formatting output   
'''
print("Hello World..! \n  This is print statement with new line Char")
print('''Hello World..! 
        This is print statement
        with out new line char''')
print("Hello World..!", end="***")  # you can observe here than print is not returning to new line
print('Hello India..!')
print("Hello India..!")

country = 'India'
print("Hello", country, "..!")      # formatting multiple statements in a single print() function


count_seconds = 30
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='..', flush=True)
        time.sleep(1)
    else:
        print('Start')

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello India , This is to write string into File and read it back...!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()